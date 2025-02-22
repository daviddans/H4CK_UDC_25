import weaviate
from sentence_transformers import SentenceTransformer
from weaviate.classes.init import Auth 
from weaviate.classes.config import Configure,  Property, DataType
from os import environ



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
                    ]
                )
            
    def addValue(self, text: str, emotion):
        embeding = self.model.encode(text)
        collection = self.connection.collections.get(self.collectionName)
        collection.data.insert(properties={
            "text":text,
                },
            vector={
                "textEmbeding": embeding,
                "emotion": emotion
            }
        )

    def closeConnection(self):
        self.connection.close()
    #FALTAN BUSQUEDAS Y POSIBLE ELIMINACINES?