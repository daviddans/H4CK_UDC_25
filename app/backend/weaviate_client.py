import weaviate

def get_context(query_text, class_name="Document", fields=["title", "content"], weaviate_url="http://localhost:8080"):
    client = weaviate.Client(weaviate_url)
    result = client.query.get(class_name, fields).with_near_text({
        "concepts": [query_text]
    }).do()
    
    contexto = ""
    for doc in result.get("data", {}).get("Get", {}).get(class_name, []):
        contexto += f"Título: {doc.get('title')}\nContenido: {doc.get('content')}\n\n"
    return contexto
