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
    context = "Ten en cuenta el siguiente contexto antes de contestar:"
    + " De pequeño me cai, estuve triste"
    + "Me levante y me puse feliz"
    + "Paciente con marco psicolofico inestable"
    + "Emocional"
    act = "Actua como un experto en psicología respondiendo amablemente a la consulta de tu paciente:"

    prompt = act + context + "Mensaje del usuario: " + text

    #Capturamos respuesta del llm
    llmResponse = llm.ask_deepseek(prompt)
    #Guardamos la peticion a la bd para tenerlo como contexto
    bd = VectorDB()
    bd.addValue(text=text, emotion=emotion, emotionVector=emotionVector)
    bd.closeConnection()
    return llmResponse
