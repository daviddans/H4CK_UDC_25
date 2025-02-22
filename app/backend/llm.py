
from transformers import pipeline
import requests
import json
import os 

def ask_deepseek(prompt):
    #Lanzar pregunta a deepseek a traves de la api de openrouter
    response = requests.post(
        url=os.getenv("OPENROUTER_URL"),
        headers={
            "Authorization": "Bearer " + os.getenv("OPENROUTER_API_KEY"),
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "deepseek/deepseek-chat:free",
            "messages": [
                {"role": "user", "content": prompt}
            ],
        })
    )
    return response


def emotionRecognition(text:str):
    #Reconocer las emociones de un texto utilizando un modelo basado en roberta
    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
    model_outputs = classifier(text)
    return model_outputs