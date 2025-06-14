"""
Características Únicas de Python
Lo que hace especial a Python vs otros lenguajes
"""

import sys
import types
import operator
from functools import partial, reduce
from itertools import islice, cycle, chain
from collections import defaultdict, Counter, namedtuple
import ast

def demonstrate_everything_is_object():
    """Demostrar que todo en Python es un objeto"""
    print("=== Everything is an Object ===")
    
    # Funciones son objetos
    def greet(name):
        return f"Hello {name}"
    
    print(f"Función: {greet}")
    print(f"Tipo: {type(greet)}")
    print(f"ID en memoria: {id(greet)}")
    print(f"Atributos: {dir(greet)[:5]}...")  # Primeros 5 atributos
    
    # Agregar atributos a funciones
    greet.version = "1.0"
    greet.author = "Python Developer"
    print(f"Versión de la función: {greet.version}")
    print(f"Autor: {greet.author}")
    
    # Métodos son objetos
    class Person:
        def __init__(self, name):
            self.name = name
        
        def say_hello(self):
            return f"Hi, I'm {self.name}"
    
    person = Person("Alice")
    method = person.say_hello
    print(f"\nMétodo: {method}")
    print(f"Resultado: {method()}")
    
    # Clases son objetos
    print(f"\nClase Person: {Person}")
    print(f"Tipo de la clase: {type(Person)}")
    print(f"Bases: {Person.__bases__}")
    
    # Módulos son objetos
    print(f"\nMódulo sys: {sys}")
    print(f"Tipo: {type(sys)}")
    sys.custom_attribute = "Added at runtime"
    print(f"Atributo personalizado: {sys.custom_attribute}")
    
    # Números son objetos
    number = 42
    print(f"\nNúmero: {number}")
    print(f"Métodos del número: {[m for m in dir(number) if not m.startswith('_')][:5]}")
    print(f"Número como binario: {number.bit_length()} bits")
    
    print()

def demonstrate_multiple_assignment():
    """Demostrar asignación múltiple y unpacking"""
    print("=== Multiple Assignment & Unpacking ===")
    
    # Asignación múltiple básica
    a, b, c = 1, 2, 3
    print(f"a={a}, b={b}, c={c}")
    
    # Intercambio sin variable temporal
    a, b = b, a
    print(f"Después del intercambio: a={a}, b={b}")
    
    # Unpacking con *
    first, *middle, last = [1, 2, 3, 4, 5, 6, 7]
    print(f"first={first}, middle={middle}, last={last}")
    
    # Unpacking anidado
    data = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
    names, ages = zip(*data)  # Transponer
    print(f"Nombres: {names}")
    print(f"Edades: {ages}")
    
    # Unpacking en loops
    print("\nUnpacking en loops:")
    pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
    for number, letter in pairs:
        print(f"  {number} -> {letter}")
    
    # Unpacking con enumerate
    words = ['python', 'java', 'javascript']
    for i, (index, word) in enumerate(enumerate(words)):
        print(f"  {i}: index={index}, word={word}")
    
    # Unpacking en funciones
    def calculate(x, y, z):
        return x + y * z
    
    values = (10, 5, 2)
    result = calculate(*values)
    print(f"\nResultado con unpacking: {result}")
    
    # Unpacking de diccionarios
    def introduce(name, age, city):
        return f"I'm {name}, {age} years old, from {city}"
    
    person_data = {'name': 'Diana', 'age': 28, 'city': 'Madrid'}
    introduction = introduce(**person_data)
    print(f"Introducción: {introduction}")
    
    print()

def demonstrate_comprehensions():
    """Demostrar list, dict, set comprehensions"""
    print("=== Comprehensions ===")
    
    # List comprehension básica
    squares = [x**2 for x in range(10)]
    print(f"Cuadrados: {squares}")
    
    # Con condición
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"Cuadrados pares: {even_squares}")
    
    # Comprehension anidada
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [item for row in matrix for item in row]
    print(f"Matriz aplanada: {flattened}")
    
    # Dict comprehension
    word_lengths = {word: len(word) for word in ['python', 'java', 'javascript']}
    print(f"Longitud de palabras: {word_lengths}")
    
    # Dict comprehension con condición
    long_words = {word: len(word) for word in ['python', 'java', 'javascript'] if len(word) > 4}
    print(f"Palabras largas: {long_words}")
    
    # Set comprehension
    unique_lengths = {len(word) for word in ['hello', 'world', 'python', 'hello']}
    print(f"Longitudes únicas: {unique_lengths}")
    
    # Generator expression (no es comprehension pero similar)
    squares_gen = (x**2 for x in range(1000000))  # No consume memoria hasta usar
    first_five_squares = list(islice(squares_gen, 5))
    print(f"Primeros 5 cuadrados (generator): {first_five_squares}")
    
    # Comprehension compleja
    # Crear diccionario de estudiantes con sus notas promedio
    students = [
        ('Alice', [85, 90, 78]),
        ('Bob', [92, 88, 94]),
        ('Charlie', [76, 82, 89])
    ]
    
    averages = {name: sum(grades)/len(grades) for name, grades in students}
    print(f"Promedios: {averages}")
    
    # Comprehension con múltiples condiciones
    divisible_by_3_and_5 = [x for x in range(100) if x % 3 == 0 and x % 5 == 0]
    print(f"Divisibles por 3 y 5: {divisible_by_3_and_5[:5]}...")
    
    print()

def demonstrate_context_managers():
    """Demostrar context managers (with statement)"""
    print("=== Context Managers ===")
    
    # Context manager básico con archivos
    import tempfile
    import os
    
    # Crear archivo temporal para demostración
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write("Hello, World!\n")
        f.write("Python context managers are awesome!")
        temp_filename = f.name
    
    print(f"Archivo temporal creado: {temp_filename}")
    
    # Leer con context manager
    with open(temp_filename, 'r') as f:
        content = f.read()
        print(f"Contenido: {content}")
    
    # Múltiples context managers
    with open(temp_filename, 'r') as input_file, \
         tempfile.NamedTemporaryFile(mode='w', delete=False) as output_file:
        
        # Procesar línea por línea
        for line_num, line in enumerate(input_file, 1):
            output_file.write(f"Línea {line_num}: {line}")
        
        output_filename = output_file.name
    
    print(f"Archivo procesado creado: {output_filename}")
    
    # Context manager personalizado
    class Timer:
        def __enter__(self):
            import time
            self.start = time.time()
            print("⏱️  Timer iniciado")
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            import time
            elapsed = time.time() - self.start
            print(f"⏱️  Timer: {elapsed:.4f} segundos")
            if exc_type:
                print(f"⚠️  Excepción ocurrida: {exc_type.__name__}")
            return False  # No suprimir excepciones
    
    # Usar context manager personalizado
    with Timer():
        # Simular trabajo
        import time
        time.sleep(0.1)
        total = sum(range(100000))
        print(f"Suma calculada: {total}")
    
    # Context manager con contextlib
    from contextlib import contextmanager
    
    @contextmanager
    def suppress_prints():
        import sys
        from io import StringIO
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            yield
        finally:
            sys.stdout = old_stdout
    
    print("Antes de suprimir prints")
    with suppress_prints():
        print("Este print no se verá")
        print("Este tampoco")
    print("Después de suprimir prints")
    
    # Limpiar archivos temporales
    os.unlink(temp_filename)
    os.unlink(output_filename)
    
    print()

def demonstrate_generators():
    """Demostrar generators y yield"""
    print("=== Generators y Yield ===")
    
    # Generator básico
    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    # Usar generator
    fib = fibonacci()
    first_10_fib = [next(fib) for _ in range(10)]
    print(f"Primeros 10 Fibonacci: {first_10_fib}")
    
    # Generator con parámetros
    def countdown(n):
        print(f"Iniciando countdown desde {n}")
        while n > 0:
            yield n
            n -= 1
        yield "¡Despegue!"
    
    for value in countdown(5):
        print(f"  {value}")
    
    # Generator expression
    squares_gen = (x**2 for x in range(10))
    print(f"Generator expression: {squares_gen}")
    print(f"Cuadrados: {list(squares_gen)}")
    
    # Generator para procesamiento de archivos grandes
    def read_large_file_chunks(filename, chunk_size=1024):
        """Leer archivo grande en chunks"""
        try:
            with open(filename, 'r') as f:
                while True:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    yield chunk
        except FileNotFoundError:
            print(f"Archivo {filename} no encontrado")
            return
    
    # Simular archivo grande
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        for i in range(1000):
            f.write(f"Línea {i}: Esta es una línea de ejemplo en un archivo grande.\n")
        large_file = f.name
    
    # Procesar archivo en chunks
    chunk_count = 0
    total_chars = 0
    for chunk in read_large_file_chunks(large_file, 512):
        chunk_count += 1
        total_chars += len(chunk)
        if chunk_count <= 3:  # Mostrar solo primeros 3 chunks
            print(f"Chunk {chunk_count}: {len(chunk)} caracteres")
    
    print(f"Total: {chunk_count} chunks, {total_chars} caracteres")
    
    # Cleanup
    os.unlink(large_file)
    
    # Yield from (delegating generators)
    def generator1():
        yield 1
        yield 2
        yield 3
    
    def generator2():
        yield 'a'
        yield 'b'
        yield 'c'
    
    def combined_generator():
        yield from generator1()
        yield from generator2()
        yield "final"
    
    combined = list(combined_generator())
    print(f"Generator combinado: {combined}")
    
    # Send values to generators
    def echo_generator():
        while True:
            value = yield
            if value is None:
                break
            print(f"Echo: {value}")
    
    echo = echo_generator()
    next(echo)  # Inicializar generator
    echo.send("Hello")
    echo.send("World")
    echo.send("Python")
    echo.send(None)  # Terminar
    
    print()

def demonstrate_decorators():
    """Demostrar decorators"""
    print("=== Decorators ===")
    
    # Decorator básico
    def timing_decorator(func):
        def wrapper(*args, **kwargs):
            import time
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            print(f"⏱️  {func.__name__} tardó {elapsed:.4f}s")
            return result
        return wrapper
    
    @timing_decorator
    def slow_function():
        import time
        time.sleep(0.1)
        return sum(range(100000))
    
    result = slow_function()
    print(f"Resultado: {result}")
    
    # Decorator con parámetros
    def retry(max_attempts=3):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for attempt in range(max_attempts):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        if attempt == max_attempts - 1:
                            raise
                        print(f"Intento {attempt + 1} falló: {e}")
                        import time
                        time.sleep(0.5)
            return wrapper
        return decorator
    
    @retry(max_attempts=3)
    def unreliable_function():
        import random
        if random.random() < 0.7:  # 70% probabilidad de fallar
            raise Exception("Función falló")
        return "¡Éxito!"
    
    try:
        result = unreliable_function()
        print(f"Resultado: {result}")
    except Exception as e:
        print(f"Falló definitivamente: {e}")
    
    # Decorator de clase
    class CountCalls:
        def __init__(self, func):
            self.func = func
            self.count = 0
        
        def __call__(self, *args, **kwargs):
            self.count += 1
            print(f"📞 {self.func.__name__} llamada #{self.count}")
            return self.func(*args, **kwargs)
    
    @CountCalls
    def greet(name):
        return f"Hello {name}!"
    
    print(greet("Alice"))
    print(greet("Bob"))
    print(greet("Charlie"))
    
    # Múltiples decorators
    def uppercase(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result.upper() if isinstance(result, str) else result
        return wrapper
    
    def add_exclamation(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{result}!" if isinstance(result, str) else result
        return wrapper
    
    @add_exclamation
    @uppercase
    @timing_decorator
    def shout_greeting(name):
        import time
        time.sleep(0.05)  # Simular trabajo
        return f"hello {name}"
    
    result = shout_greeting("World")
    print(f"Resultado final: {result}")
    
    print()

def demonstrate_metaclasses():
    """Demostrar metaclasses básicas"""
    print("=== Metaclasses (Conceptos Básicos) ===")
    
    # Toda clase tiene una metaclass
    class RegularClass:
        pass
    
    print(f"Tipo de RegularClass: {type(RegularClass)}")
    print(f"Metaclass de RegularClass: {RegularClass.__class__}")
    
    # Metaclass personalizada
    class SingletonMeta(type):
        _instances = {}
        
        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]
    
    class Singleton(metaclass=SingletonMeta):
        def __init__(self, value):
            self.value = value
    
    # Probar singleton
    s1 = Singleton("first")
    s2 = Singleton("second")  # Esto no cambiará el valor
    
    print(f"s1.value: {s1.value}")
    print(f"s2.value: {s2.value}")
    print(f"s1 is s2: {s1 is s2}")
    
    # Metaclass para auto-registro
    class AutoRegisterMeta(type):
        registry = {}
        
        def __new__(mcs, name, bases, attrs):
            cls = super().__new__(mcs, name, bases, attrs)
            mcs.registry[name] = cls
            return cls
    
    class Plugin(metaclass=AutoRegisterMeta):
        pass
    
    class DatabasePlugin(Plugin):
        name = "database"
    
    class CachePlugin(Plugin):
        name = "cache"
    
    print(f"Plugins registrados: {list(AutoRegisterMeta.registry.keys())}")
    
    # Crear clases dinámicamente
    def make_class(name, methods):
        def __init__(self, value):
            self.value = value
        
        attrs = {'__init__': __init__}
        attrs.update(methods)
        
        return type(name, (), attrs)
    
    # Crear clase dinámicamente
    DynamicClass = make_class('DynamicClass', {
        'get_value': lambda self: self.value,
        'double_value': lambda self: self.value * 2
    })
    
    obj = DynamicClass(42)
    print(f"Clase dinámica - valor: {obj.get_value()}")
    print(f"Clase dinámica - doble: {obj.double_value()}")
    
    print()

def demonstrate_advanced_features():
    """Demostrar características avanzadas únicas"""
    print("=== Características Avanzadas Únicas ===")
    
    # 1. Descriptors
    class LoggedAttribute:
        def __init__(self, name):
            self.name = name
            self.private_name = f'_{name}'
        
        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            value = getattr(obj, self.private_name, None)
            print(f"📖 Accediendo a {self.name}: {value}")
            return value
        
        def __set__(self, obj, value):
            print(f"✏️  Estableciendo {self.name}: {value}")
            setattr(obj, self.private_name, value)
    
    class Person:
        name = LoggedAttribute('name')
        age = LoggedAttribute('age')
        
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    person = Person("Alice", 30)
    print(f"Nombre: {person.name}")
    person.age = 31
    
    # 2. Properties avanzadas
    class Temperature:
        def __init__(self, celsius=0):
            self._celsius = celsius
        
        @property
        def celsius(self):
            return self._celsius
        
        @celsius.setter
        def celsius(self, value):
            if value < -273.15:
                raise ValueError("Temperatura por debajo del cero absoluto")
            self._celsius = value
        
        @property
        def fahrenheit(self):
            return (self._celsius * 9/5) + 32
        
        @fahrenheit.setter
        def fahrenheit(self, value):
            self.celsius = (value - 32) * 5/9
        
        @property
        def kelvin(self):
            return self._celsius + 273.15
    
    temp = Temperature(25)
    print(f"\n🌡️  Temperatura: {temp.celsius}°C = {temp.fahrenheit:.1f}°F = {temp.kelvin:.1f}K")
    temp.fahrenheit = 100
    print(f"🌡️  Después cambio: {temp.celsius:.1f}°C = {temp.fahrenheit}°F = {temp.kelvin:.1f}K")
    
    # 3. Slots para optimización
    class Point:
        __slots__ = ['x', 'y']
        
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def distance_to_origin(self):
            return (self.x**2 + self.y**2)**0.5
    
    point = Point(3, 4)
    print(f"\n📍 Punto con slots: ({point.x}, {point.y})")
    print(f"📍 Distancia: {point.distance_to_origin()}")
    
    # No se puede agregar atributos dinámicamente
    try:
        point.z = 5
    except AttributeError as e:
        print(f"❌ Error con slots: {e}")
    
    # 4. __call__ para objetos llamables
    class Multiplier:
        def __init__(self, factor):
            self.factor = factor
        
        def __call__(self, value):
            return value * self.factor
    
    double = Multiplier(2)
    triple = Multiplier(3)
    
    print(f"\n🔢 Objeto callable - double(5): {double(5)}")
    print(f"🔢 Objeto callable - triple(7): {triple(7)}")
    
    # 5. Operator overloading
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)
        
        def __mul__(self, scalar):
            return Vector(self.x * scalar, self.y * scalar)
        
        def __repr__(self):
            return f"Vector({self.x}, {self.y})"
        
        def __abs__(self):
            return (self.x**2 + self.y**2)**0.5
    
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    v3 = v1 + v2
    v4 = v1 * 2
    
    print(f"\n➡️  Vector1: {v1}")
    print(f"➡️  Vector2: {v2}")
    print(f"➡️  Suma: {v3}")
    print(f"➡️  Multiplicación: {v4}")
    print(f"➡️  Magnitud v1: {abs(v1):.2f}")
    
    print()

if __name__ == "__main__":
    print("=== Características Únicas de Python ===")
    print("Lo que hace especial a Python comparado con otros lenguajes\n")
    
    demonstrate_everything_is_object()
    demonstrate_multiple_assignment()
    demonstrate_comprehensions()
    demonstrate_context_managers()
    demonstrate_generators()
    demonstrate_decorators()
    demonstrate_metaclasses()
    demonstrate_advanced_features()
    
    print("=== ¿Por qué Python es único? ===")
    unique_aspects = [
        "🐍 Indentación significativa (fuerza legibilidad)",
        "🧘 Filosofía consistente (Zen of Python)",
        "🔧 Introspección poderosa (todo es objeto)",
        "🎯 Sintaxis expresiva (comprensible para humanos)",
        "🔄 Duck typing (flexibilidad sin complejidad)",
        "📦 Batteries included (biblioteca estándar rica)",
        "🌍 Comunidad enfocada en usabilidad",
        "⚡ Prototipado rápido pero escalable",
        "🔗 Interoperabilidad excepcional",
        "📚 Curva de aprendizaje amigable pero profunda"
    ]
    
    for aspect in unique_aspects:
        print(aspect)
    
    print("\n=== Comparación con Otros Lenguajes ===")
    comparisons = [
        ("Java", "Python: menos verbose, duck typing, REPL"),
        ("C++", "Python: gestión automática de memoria, sintaxis simple"),
        ("JavaScript", "Python: indentación significativa, mejor organización"),
        ("Ruby", "Python: una forma obvia de hacer las cosas"),
        ("Go", "Python: más expresivo, ecosistema más maduro"),
        ("Rust", "Python: más simple, menos enfoque en seguridad de memoria")
    ]
    
    for lang, diff in comparisons:
        print(f"vs {lang:12}: {diff}")
    
    print(f"\n🎉 Python: {sys.version_info.major}.{sys.version_info.minor} - ¡Sigue evolucionando!")