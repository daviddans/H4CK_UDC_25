#Import dependencies
import socketio
import llm
from vectordb import VectorDB
from dotenv import load_dotenv

load_dotenv()


def main():
    sio = socketio.Client()


def on_chat_question(text:str):
    print("empezando")
    #Extaer emociones
    emotionVector=llm.emotionRecognition(text=text)
    print("emociones reconocidas")
    #Generar el prompt
    prompt = text

    #Capturamos respuesta del llm
    llmResponse = llm.ask_deepseek(prompt)
    print("gepeto responde")
    #Guardamos la peticion a la bd para tenerlo como contexto
    bd = VectorDB()
    #bd.addValue(text=text, emotion=emotionVector)
    bd.closeConnection()
    print("Contexto actualizado")
    return llmResponse
