#Import dependencies
import socketio
from flask import Flask
import eventlet
import eventlet.wsgi
import llm
from jsondb import *
from vectordb import VectorDB
from dotenv import load_dotenv
import json
from datetime import date

load_dotenv()

# Crea la instancia del servidor Socket.IO
sio = socketio.Server(cors_allowed_origins="*")

# Crea la aplicación Flask
app = Flask(__name__)
# Integra Socket.IO con Flask
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

@sio.on('preguntaUser')
def on_chat_question(sid, data):
    #Creamos una refecencia para uasr la bd
    bd = VectorDB()

    text = data.get('mensaje', '')
    print("Mensaje recibido de", sid, ":", text)
    #Extaer emociones
    emotion,emotionVector =llm.emotionRecognition(text=text)

    #Generar el prompt
    #Recuperar contexto relevante

    query = bd.semanticSearch(text=text,emotionVector=emotionVector,max=5) #Recuperar los 5 contextos mas relevantes

    context = "Ten en cuenta el siguiente contexto expresado en json antes de contestar:" 

    act = "Actua como un experto en psicología respondiendo amablemente y brebemente a la consulta de tu paciente pero de forma causal."

    prompt = context + query + act + "Mensaje del usuario: " + text

    #Guardamos la peticion a la bd para tenerlo como contexto
    
    bd.addValue(text=text, emotion=emotion, emotionVector=emotionVector, date=date.today().strftime("%d/%m/%Y"))

    #Capturamos respuesta del llm
    llmResponse = llm.ask_deepseek(prompt)
    textResponse = llmResponse["choices"][0]["message"]["content"] #capturamos el mensaje del llm para mostrarlo
    
    #Cerramos conexion a weaviate
    bd.closeConnection()

    sio.emit('llmResponse', {'llmResponse': textResponse}, room=sid)

# leer json
@sio.on('cargaDiario')
def on_load_diary(sid, data):
    fecha = data.get("fecha")
    if not fecha:
        sio.emit('jsonResponse', {'error': 'Fecha no proporcionada'}, room=sid)
        return

    entrada = obtener_entrada_por_fecha(fecha)
    if entrada is None:
        sio.emit('jsonResponse', {'error': f'No se encontró entrada para la fecha {fecha}'}, room=sid)
    else:
        sio.emit('jsonResponse', {'jsonResponse': entrada}, room=sid)
    
        
# guardar json local
# guardar contexto
@sio.on('guardarDiario')
def on_save_diary(sid, data):
    
    try:
        #guardar en json
        #data debe tener la estructura: { "fecha", "entrada", "respuestas": { "q1", "q2" } }
        guardar_entradas_diario(data)
        """
        #guardar en bdvectorial
        textos = [
            ("entrada", data.get("entrada", "")),
            ("q1", data.get("respuestas", {}).get("q1", "")),
            ("q2", data.get("respuestas", {}).get("q2", ""))
        ]
        bd = VectorDB()
        for texto in enumerate(textos, start=1):
            # Realizar análisis para cada texto
            emotion,emotionVector =llm.emotionRecognition(text=texto)
            bd.addValue(text=texto, emotion=emotion, emotionVector=emotionVector, date=date.today().strftime("%d/%m/%Y"))

        #Cerramos conexion a weaviate
        bd.closeConnection()
        """
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "error": str(e)}
        

    

if __name__ == '__main__':
    # Levanta el servidor con eventlet en el puerto 5000
    print("###STARTING-BACKEND###")
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
