import os
from dotenv import load_dotenv
from weaviate_client import get_context
from deepseek_client import ask_deepseek
import json

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Definir la pregunta del usuario
query_text = "¿Cuál es el significado de la vida?"

# Obtener contexto relevante desde Weaviate
weaviate_url = os.getenv("WEAVIATE_URL", "http://localhost:8080")
contexto = get_context(query_text, weaviate_url=weaviate_url)

# Construir el prompt combinando el contexto y la pregunta
prompt = f"""Contexto:
{contexto}

Pregunta: {query_text}
Respuesta:"""

# Enviar el prompt a la API de Deepseek mediante OpenRouter
base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")

response = ask_deepseek(prompt, base_url, api_key)

# Procesar y mostrar la respuesta
if response.status_code == 200:
    try:
        data = response.json()
        answer = data["choices"][0]["message"]["content"]
        print("Respuesta de Deepseek:")
        print(answer)
    except Exception as e:
        print("Error al parsear la respuesta:", e)
else:
    print("Error en la solicitud. Código de estado:", response.status_code)
    print(response.text)
