import json
from datetime import datetime

def crear_entrada_diario(fecha, campo1, campo2, campo3):
    """
    Crea un diccionario que representa una entrada del diario.
    
    Parámetros:
    - fecha: string con la fecha (ej: "2025-02-23") o puede generarse automáticamente.
    - campo1, campo2, campo3: valores de los campos que se quieran almacenar.
    
    Retorna:
    - dict con la entrada del diario.
    """
    entrada = {
        "fecha": fecha,
        "campo1": campo1,
        "campo2": campo2,
        "campo3": campo3
    }
    return entrada

def guardar_entradas_diario(entradas, archivo="diario.json"):
    """
    Guarda una lista de entradas en un archivo JSON con una indentación para legibilidad.
    
    Parámetros:
    - entradas: lista de diccionarios (cada uno una entrada del diario).
    - archivo: nombre del archivo donde se guardará la información.
    """
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(entradas, f, ensure_ascii=False, indent=4)

def obtener_entrada_por_fecha(fecha, archivo="diario.json"):
    """
    Busca y devuelve la entrada del diario correspondiente a la fecha dada.
    
    Parámetros:
    - fecha: string en formato "YYYY-MM-DD" que indica la fecha buscada.
    - archivo: ruta del archivo JSON donde se encuentran las entradas del diario.
    
    Retorna:
    - El diccionario de la entrada si se encuentra; de lo contrario, None.
    """
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            entradas = json.load(f)
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
        return None

    # Buscar la entrada que coincida con la fecha
    for entrada in entradas:
        if entrada.get("fecha") == fecha:
            return entrada

    # Si no se encuentra ninguna entrada con la fecha indicada
    return None