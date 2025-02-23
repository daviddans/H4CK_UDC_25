#Import dependencies
import socketio
from flask import Flask
import eventlet
import eventlet.wsgi
import llm
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


    def on_load_diary():
        # leer json

    def on_save_diary():
        # guardar json local
        # guardar contexto

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
