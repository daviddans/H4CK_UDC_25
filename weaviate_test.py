import weaviate
from sentence_transformers import SentenceTransformer
from weaviate.classes.init import Auth 
from weaviate.classes.config import Configure,  Property, DataType
import os

# Configurar la conexión con Weaviate Cloud Service
client = weaviate.connect_to_weaviate_cloud(
    cluster_url="https://8ngqp4mstgwa8b0p9fujvg.c0.europe-west3.gcp.weaviate.cloud",  # Reemplaza con tu instancia
    auth_credentials=Auth.api_key("GoYX1RKaXvZ5vzFLD8SJ8pILJHKbndIDBTSr")  # Reemplaza con tu API key
)


# Recuperar coleccion 
question = client.collections.exists("Pajaritos")

"""
model = SentenceTransformer("all-MiniLM-L6-v2")
embeding = model.encode("ADIOS")

question.data.insert({
    "prompt" : "ADIOS",
    "emotion" : "felis",
    "embeding": [1,1,1]
},
vector=embeding)

qvector = model.encode("Adiosito")
response = question.query.near_vector(
    near_vector=qvector,
    limit=2
)


print(response)

"""
print(question)
# Cerrar la conexión
client.close()