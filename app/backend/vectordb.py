import weaviate
import numpy
from sentence_transformers import SentenceTransformer
from weaviate.classes.init import Auth 
from weaviate.classes.config import Configure,  Property, DataType
from os import environ
import numpy


class VectorDB: 
    
    def __init__(self):
    # Conectar con la api 
        self.connection = weaviate.connect_to_weaviate_cloud(
                 cluster_url=environ["WEAVIATE_URL"],
                 auth_credentials=Auth.api_key(environ["WEAVIATE_API_KEY"])  
                )

    # Seleccionar modelo para crear embedings
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
    # Iniciar la coleccion
        self.collectionName = "EmotionContext"
        if(not self.connection.collections.exists(self.collectionName)):
            self.connection.collections.create(
                name=self.collectionName,
                vectorizer_config=Configure.Vectorizer.none(),
                properties=[
                    Property(name="text", data_type=DataType.TEXT),
                    Property(name="emotion", data_type=DataType.TEXT),
                    Property(name="date", data_type=DataType.TEXT)
                    ]
                )   
            
    def addValue(self, text: str, emotion, emotionVector, date):
        
        embeding = self.model.encode(text)
        collection = self.connection.collections.get(self.collectionName)
        collection.data.insert(properties={
            "text":text,
            "emotion":emotion,
            "date": date
                },
            vector= numpy.append(embeding, emotionVector)
        )

    def closeConnection(self):
        self.connection.close()

    def semanticSearch(self, text):
        textEmbeding = self.model.encode(text)