"""
Ejemplo de functools.singledispatch
Sobrecarga de funciones basada en el tipo del primer argumento
"""

from functools import singledispatch
from typing import List, Dict
import json

@singledispatch
def serialize(data):
    """Función genérica para serializar datos"""
    return str(data)

@serialize.register
def _(data: int):
    """Serializar enteros con información adicional"""
    return f"INTEGER:{data}"

@serialize.register
def _(data: str):
    """Serializar strings con comillas"""
    return f'STRING:"{data}"'

@serialize.register
def _(data: list):
    """Serializar listas como JSON"""
    return f"LIST:{json.dumps(data)}"

@serialize.register
def _(data: dict):
    """Serializar diccionarios con formato especial"""
    items = [f"{k}={v}" for k, v in data.items()]
    return f"DICT:{{{','.join(items)}}}"

@serialize.register
def _(data: float):
    """Serializar floats con precisión específica"""
    return f"FLOAT:{data:.2f}"

# Ejemplos de uso
if __name__ == "__main__":
    print("=== Ejemplos de singledispatch ===")
    
    test_data = [
        42,
        "hello world",
        [1, 2, 3, 4],
        {"name": "Python", "version": 3.9},
        3.14159,
        True,  # bool es subclase de int
        None
    ]
    
    for data in test_data:
        result = serialize(data)
        print(f"{type(data).__name__:>8}: {data} -> {result}")
    
    # Ver todas las implementaciones registradas
    print(f"\nImplementaciones registradas: {len(serialize.registry)}")
    for type_key in serialize.registry:
        print(f"  - {type_key}")