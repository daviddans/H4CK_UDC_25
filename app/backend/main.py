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

load_dotenv()

# Crea la instancia del servidor Socket.IO
sio = socketio.Server(cors_allowed_origins="*")

# Crea la aplicación Flask
app = Flask(__name__)
# Integra Socket.IO con Flask
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

def main():
    print("###STARTING-BACKEND###")
    socketio.Client()

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
    
    bd.addValue(text=text, emotion=emotion, emotionVector=emotionVector, date="01/01/2000")

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

    textResponse = obtener_entrada_por_fecha(fecha)
    if textResponse is None:
        sio.emit('jsonResponse', {'error': f'No se encontró entrada para la fecha {fecha}'}, room=sid)
    else:
        sio.emit('jsonResponse', {'jsonResponse': textResponse}, room=sid)
    
        
# guardar json local
# guardar contexto
@sio.on('gaurdarDatos')
def on_save_diary(sid, data):
    #guardar en json
    guardar_entradas_diario(data)

    #guardar en bdvectorial
    fecha = data.get("fecha")
    text = data.get('mensaje', '')
    bd = VectorDB()
    emotion,emotionVector =llm.emotionRecognition(text=text)
    bd.addValue(text=text, emotion=emotion, emotionVector=emotionVector, date="01/01/2000")

    #Cerramos conexion a weaviate
    bd.closeConnection()
    

    sio.emit('ackGuardar', {'Status':'ok'}, room=sid)
        

    def on_load_profile():
        #leer json

    def on_save_profile():
        #guardar json

    def on_generate_profile():
        #cluster data
        #Generate a personaloty class
        #using a debug variable

    def on_generate_tasks():
        #generate tasks on context
        #using a debug variable

if __name__ == '__main__':
    # Levanta el servidor con eventlet en el puerto 5000
   
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
