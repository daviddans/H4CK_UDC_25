#Import dependencies
import socketio
import llm
from vectordb import VectorDB
from dotenv import load_dotenv

load_dotenv()


def main():
    sio = socketio.Client()


def on_chat_question(text:str):
    #Extaer emociones
    emotion,emotionVector =llm.emotionRecognition(text=text)
    #Generar el prompt
    context = "Ten en cuenta el siguiente contexto antes de contestar:" + "Le tengo panico a los peces" 
    act = "Actua como un psicologo"
    prompt = context + text
    print(prompt)
    #Capturamos respuesta del llm
    llmResponse = llm.ask_deepseek(prompt)
    #Guardamos la peticion a la bd para tenerlo como contexto
    bd = VectorDB()
    bd.addValue(text=text, emotion=emotion, emotionVector=emotionVector)
    bd.closeConnection()
    return llmResponse
