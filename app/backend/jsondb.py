import json
import os

def guardar_entradas_diario(nueva_entrada, archivo="diario.json"):
    """
    Guarda o actualiza una entrada en el diario.
    
    Si ya existe una entrada con la fecha dada, se actualiza.
    Si no, se añade una nueva entrada.
    
    Parámetros:
    - nueva_entrada: diccionario con la entrada del diario, con claves:
        - "fecha" (YYYY-MM-DD)
        - "entrada"
        - "respuestas" (ej: {"q1": "...", "q2": "..."})
    - archivo: nombre del archivo donde se guardará la información.
    """
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            try:
                entradas = json.load(f)
            except json.JSONDecodeError:
                entradas = []
    else:
        entradas = []
    
    fecha = nueva_entrada.get("fecha")
    actualizado = False
    for i, entrada in enumerate(entradas):
        if entrada.get("fecha") == fecha:
            entradas[i] = nueva_entrada
            actualizado = True
            break
    if not actualizado:
        entradas.append(nueva_entrada)
    
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(entradas, f, ensure_ascii=False, indent=4)

def obtener_entrada_por_fecha(fecha, archivo="diario.json"):
    """
    Devuelve la entrada del diario correspondiente a la fecha dada.
    
    Parámetros:
    - fecha: string en formato "YYYY-MM-DD".
    - archivo: ruta del archivo JSON donde se guardan las entradas.
    
    Retorna:
    - El diccionario de la entrada si se encuentra, o None si no se encuentra.
    """
    if not os.path.exists(archivo):
        return None
    
    with open(archivo, "r", encoding="utf-8") as f:
        try:
            entradas = json.load(f)
        except json.JSONDecodeError:
            return None
    
    for entrada in entradas:
        if entrada.get("fecha") == fecha:
            return entrada
    return None
