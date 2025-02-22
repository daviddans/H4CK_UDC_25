
from transformers import pipeline
import requests
import json
import os 
import numpy

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
    response = response.json()
    return response


def emotionRecognition(text:str):
    #Reconocer las emociones de un texto utilizando un modelo basado en roberta
    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
    model_outputs = classifier(text)
    model_outputs = model_outputs[0] #Linea estupida porque el modelo por algun motivo devuelve un array de un solo elemento
    model_outputs.sort(key=lambda item: item["label"]) #Asegurar orden alfabetico por label
    #Extraemos el vector de valores y la emocion mas probable
    max = 0
    emotion = ""
    outputList=[]
    for out in model_outputs:
        last = len(outputList) -1
        outputList.append(out.get("score"))
        if(max < outputList[last]):
            max = outputList[last]
            emotion = out.get("label")
    
    outputVector = numpy.asarray(outputList, dtype=numpy.float32)

    return (emotion,outputVector)
