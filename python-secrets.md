# Secretos de Python: Características Poco Conocidas

## Características de su biblioteca estándar

### 1. `collections.ChainMap`
Permite combinar múltiples diccionarios en una sola vista.
```python
from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)
print(chain['a'])  # 1
print(chain['b'])  # 2 (primer diccionario tiene prioridad)
```

### 2. `functools.singledispatch`
Permite crear funciones con diferentes implementaciones según el tipo del primer argumento.
```python
from functools import singledispatch

@singledispatch
def process(arg):
    print(f"Processing {arg}")

@process.register
def _(arg: int):
    print(f"Processing integer: {arg * 2}")

@process.register
def _(arg: str):
    print(f"Processing string: {arg.upper()}")
```

### 3. `itertools.accumulate`
Genera valores acumulados usando una función.
```python
import itertools
import operator

numbers = [1, 2, 3, 4, 5]
# Suma acumulada
print(list(itertools.accumulate(numbers)))  # [1, 3, 6, 10, 15]
# Producto acumulado
print(list(itertools.accumulate(numbers, operator.mul)))  # [1, 2, 6, 24, 120]
```

### 4. `pathlib` vs `os.path`
Una API moderna y orientada a objetos para manejo de rutas.
```python
from pathlib import Path

# Forma moderna
path = Path.home() / "documents" / "file.txt"
if path.exists():
    content = path.read_text()
    
# Crear directorios
path.parent.mkdir(parents=True, exist_ok=True)
```

### 5. `dataclasses.field()` con factory
Para valores mutables por defecto en dataclasses.
```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Person:
    name: str
    hobbies: List[str] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
```

### 6. `contextlib.contextmanager`
Crear context managers con decoradores.
```python
from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        print(f"Tiempo transcurrido: {time.time() - start:.2f}s")

with timer():
    time.sleep(1)
```

### 7. `operator` module
Funciones para operadores como objetos.
```python
from operator import attrgetter, itemgetter, methodcaller

# Obtener atributos de objetos
students = [Student('Alice', 85), Student('Bob', 90)]
get_grade = attrgetter('grade')
grades = map(get_grade, students)

# Ordenar por múltiples campos
data = [('Alice', 25, 85), ('Bob', 30, 90)]
sorted_data = sorted(data, key=itemgetter(1, 2))  # Por edad y luego por score
```

## Características de sus intérpretes

### 1. REPL mejorado con `_` (underscore)
El underscore almacena el último resultado en el REPL.
```python
>>> 5 + 3
8
>>> _ * 2
16
>>> result = _
>>> result
16
```

### 2. CPython's `sys.intern()`
Internado de strings para optimización de memoria.
```python
import sys
a = sys.intern("hello world")
b = sys.intern("hello world")
print(a is b)  # True - misma referencia en memoria
```

### 3. `__debug__` variable global
Variable especial que es False cuando se ejecuta con -O.
```python
if __debug__:
    print("Modo debug activado")
    # Código de debugging que se elimina con -O
```

### 4. Optimizaciones de CPython
- Small integer caching (-5 a 256)
- String interning para identificadores
- Peephole optimizer para bytecode

### 5. `dis` module - Desensamblador de bytecode
```python
import dis

def example():
    x = 1
    y = 2
    return x + y

dis.dis(example)
```

### 6. Multiple inheritance y Method Resolution Order (MRO)
```python
class A:
    def method(self): print("A")

class B(A):
    def method(self): print("B") 

class C(A):
    def method(self): print("C")

class D(B, C):
    pass

print(D.__mro__)  # Muestra el orden de resolución
```

## Tooling

### 1. `python -m` para ejecutar módulos
```bash
python -m http.server  # Servidor HTTP simple
python -m json.tool file.json  # Formatear JSON
python -m pdb script.py  # Debugger
python -m timeit "sum(range(100))"  # Timing
python -m zipfile -c archive.zip file1.py file2.py  # Crear ZIP
```

### 2. `f-strings` avanzados
```python
name = "Python"
value = 42.123456
# Formateo con especificadores
print(f"{name:>10}")  # Alineación a la derecha
print(f"{value:.2f}")  # 2 decimales
print(f"{value:e}")   # Notación científica

# Debugging (Python 3.8+)
print(f"{name=}")  # name='Python'
print(f"{value=:.2f}")  # value=42.12
```

### 3. `breakpoint()` función built-in (Python 3.7+)
```python
def complex_function():
    x = 42
    breakpoint()  # Pausa aquí automáticamente
    return x * 2
```

### 4. `__pycache__` y optimización de imports
Python compila automáticamente módulos a bytecode para importaciones más rápidas.

### 5. Virtual environments con `venv`
```bash
python -m venv myenv
source myenv/bin/activate  # Unix
myenv\Scripts\activate  # Windows
```

### 6. `pip` características avanzadas
```bash
pip install -e .  # Instalación en modo desarrollo
pip freeze > requirements.txt  # Generar requirements
pip install -r requirements.txt  # Instalar desde requirements
pip show package  # Información detallada del paquete
```

## Filosofía

### 1. The Zen of Python
```python
import this
```
- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Readability counts
- There should be one obvious way to do it

### 2. Duck Typing
"If it walks like a duck and quacks like a duck, it's a duck"
```python
class Duck:
    def quack(self): return "Quack!"

class Person:
    def quack(self): return "I'm quacking!"

def make_it_quack(thing):
    return thing.quack()  # No importa el tipo, solo que tenga quack()
```

### 3. EAFP vs LBYL
**EAFP (Easier to Ask for Forgiveness than Permission)**
```python
# Pythonic way
try:
    value = dictionary[key]
except KeyError:
    value = default_value

# vs LBYL (Look Before You Leap)
if key in dictionary:
    value = dictionary[key]
else:
    value = default_value
```

### 4. Batteries Included
Python viene con una biblioteca estándar muy completa que cubre la mayoría de casos de uso comunes.

### 5. Expresividad y Legibilidad
```python
# Pythonic
result = [x**2 for x in range(10) if x % 2 == 0]

# vs imperativo
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x**2)
```

## Interoperabilidad

### 1. C Extensions con `ctypes`
```python
import ctypes

# Cargar biblioteca C
libc = ctypes.CDLL("libc.so.6")  # Linux
# libc = ctypes.CDLL("msvcrt.dll")  # Windows

# Llamar función C
libc.printf(b"Hello from C!\n")
```

### 2. `cffi` - C Foreign Function Interface
```python
from cffi import FFI

ffi = FFI()
ffi.cdef("int printf(const char *format, ...);")
C = ffi.dlopen(None)
C.printf(b"Hello %s!\n", b"World")
```

### 3. Cython - Python con speed de C
```python
# archivo: fast_math.pyx
def fibonacci(int n):
    cdef int a = 0
    cdef int b = 1
    cdef int i
    
    for i in range(n):
        a, b = b, a + b
    return a
```

### 4. `subprocess` para ejecutar programas externos
```python
import subprocess

# Ejecutar comando y capturar salida
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(result.stdout)

# Ejecutar con shell
result = subprocess.run('echo "Hello World"', shell=True, capture_output=True, text=True)
```

### 5. `multiprocessing` para paralelismo real
```python
from multiprocessing import Pool

def square(x):
    return x ** 2

with Pool() as pool:
    results = pool.map(square, range(10))
    print(results)
```

### 6. Python C API
```c
#include <Python.h>

static PyObject* hello_world(PyObject* self, PyObject* args) {
    return PyUnicode_FromString("Hello from C!");
}

static PyMethodDef module_methods[] = {
    {"hello_world", hello_world, METH_NOARGS, "Returns hello world"},
    {NULL, NULL, 0, NULL}
};
```

## Desarrollos hechos por la comunidad

### 1. FastAPI - Framework web moderno
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

### 2. Pydantic - Validación de datos con type hints
```python
from pydantic import BaseModel, validator
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None
    
    @validator('age')
    def validate_age(cls, v):
        if v < 0:
            raise ValueError('Age must be positive')
        return v
```

### 3. Rich - Terminal con estilo
```python
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()
console.print("Hello", style="bold red")

table = Table(title="Star Wars Movies")
table.add_column("Released", style="cyan")
table.add_column("Title", style="magenta")
table.add_row("1977", "A New Hope")
```

### 4. Typer - CLI con type hints
```python
import typer

def main(name: str, age: int = 25):
    """
    Say hello to someone.
    """
    typer.echo(f"Hello {name}, you are {age} years old")

if __name__ == "__main__":
    typer.run(main)
```

### 5. Streamlit - Web apps para data science
```python
import streamlit as st
import pandas as pd

st.title('My First Streamlit App')

data = pd.DataFrame({
    'x': range(10),
    'y': range(10, 20)
})

st.line_chart(data)
```

### 6. Jupyter Notebooks - Programación interactiva
Revolucionó la forma de hacer data science y prototipado.

### 7. NumPy/SciPy/Pandas - Ecosistema científico
```python
import numpy as np
import pandas as pd

# NumPy - arrays eficientes
arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)

# Pandas - análisis de datos
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df.describe())
```

### 8. AsyncIO y bibliotecas asíncronas
```python
import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ['http://example.com', 'http://google.com']
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results
```

### 9. Type checking con mypy
```python
from typing import List, Optional

def process_items(items: List[str]) -> Optional[str]:
    if not items:
        return None
    return items[0].upper()

# Ejecutar: mypy script.py
```

### 10. Packaging moderno con Poetry
```toml
[tool.poetry]
name = "my-project"
version = "0.1.0"
description = ""

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.25.1"

[tool.poetry.dev-dependencies]
pytest = "^6.2.2"
```

## Características únicas de Python

### 1. Indentación significativa
Python es uno de los pocos lenguajes donde la indentación es parte de la sintaxis.

### 2. Everything is an object
```python
# Incluso las funciones son objetos
def greet():
    return "Hello"

print(greet.__name__)  # 'greet'
greet.custom_attr = "I'm a function attribute"
```

### 3. Multiple assignment y unpacking
```python
a, b = 1, 2
a, b = b, a  # Swap sin variable temporal

*first, last = [1, 2, 3, 4, 5]  # first = [1, 2, 3, 4], last = 5
```

### 4. List/Dict/Set comprehensions
```python
# List comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]

# Dict comprehension
square_dict = {x: x**2 for x in range(5)}

# Set comprehension
unique_squares = {x**2 for x in range(-5, 6)}
```

### 5. Context managers (with statement)
```python
with open('file.txt', 'r') as f:
    content = f.read()
# Archivo se cierra automáticamente
```

### 6. Generators y yield
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print(next(fib))  # 0
print(next(fib))  # 1
print(next(fib))  # 1
```

### 7. Decorators
```python
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.2f}s")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(1)
    return "Done"
```

Estas características hacen de Python un lenguaje único en el ecosistema de programación, combinando simplicidad, expresividad y potencia de una manera que pocos lenguajes logran.