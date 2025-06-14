"""
Secretos del intérprete de Python
Características ocultas y optimizaciones internas
"""

import sys
import dis
import gc

def demonstrate_underscore_repl():
    """
    El underscore (_) en el REPL guarda el último resultado
    Este ejemplo simula el comportamiento (en REPL real funciona automáticamente)
    """
    print("=== Underscore en REPL ===")
    print("En el REPL interactivo:")
    print(">>> 5 + 3")
    print("8")
    print(">>> _ * 2")
    print("16")
    print(">>> result = _")
    print(">>> result")
    print("16")
    print()

def demonstrate_string_interning():
    """Demostrar el internado de strings en Python"""
    print("=== String Interning ===")
    
    # Strings pequeños y identificadores se internan automáticamente
    a = "hello"
    b = "hello"
    print(f"a = 'hello', b = 'hello'")
    print(f"a is b: {a is b}")  # True
    print(f"id(a): {id(a)}, id(b): {id(b)}")
    
    # Strings con espacios normalmente no se internan
    c = "hello world"
    d = "hello world"
    print(f"\nc = 'hello world', d = 'hello world'")
    print(f"c is d: {c is d}")  # Puede ser False
    print(f"id(c): {id(c)}, id(d): {id(d)}")
    
    # Forzar internado con sys.intern
    e = sys.intern("hello world")
    f = sys.intern("hello world")
    print(f"\ne = sys.intern('hello world'), f = sys.intern('hello world')")
    print(f"e is f: {e is f}")  # True
    print(f"id(e): {id(e)}, id(f): {id(f)}")
    print()

def demonstrate_small_integer_caching():
    """Python cachea enteros pequeños (-5 a 256)"""
    print("=== Small Integer Caching ===")
    
    # Enteros pequeños se cachean
    x = 100
    y = 100
    print(f"x = 100, y = 100")
    print(f"x is y: {x is y}")  # True
    print(f"id(x): {id(x)}, id(y): {id(y)}")
    
    # Enteros grandes no se cachean
    big_x = 1000
    big_y = 1000
    print(f"\nbig_x = 1000, big_y = 1000")
    print(f"big_x is big_y: {big_x is big_y}")  # False
    print(f"id(big_x): {id(big_x)}, id(big_y): {id(big_y)}")
    
    # Límites del caché
    print(f"\nLímites del caché de enteros:")
    for i in [-6, -5, -4, 0, 1, 255, 256, 257]:
        a = i
        b = i
        print(f"  {i}: {a is b}")
    print()

def demonstrate_debug_variable():
    """La variable __debug__ cambia con optimizaciones"""
    print("=== Variable __debug__ ===")
    print(f"__debug__ = {__debug__}")
    
    if __debug__:
        print("Ejecutándose en modo debug")
        print("Este código se elimina con python -O")
    else:
        print("Ejecutándose en modo optimizado")
    
    # Ejemplo de uso
    def expensive_assertion_check():
        return all(x > 0 for x in range(1000000))
    
    if __debug__:
        print("Realizando verificaciones de debug...")
        # Este código se elimina completamente con -O
        assert expensive_assertion_check(), "Falló la verificación"
    
    print()

def demonstrate_mro():
    """Method Resolution Order en herencia múltiple"""
    print("=== Method Resolution Order (MRO) ===")
    
    class A:
        def method(self):
            return "A"
    
    class B(A):
        def method(self):
            return "B"
    
    class C(A):
        def method(self):
            return "C"
    
    class D(B, C):
        pass
    
    # Mostrar MRO
    print("Jerarquía de clases:")
    print("    A")
    print("   / \\")
    print("  B   C")
    print("   \\ /")
    print("    D")
    
    print(f"\nMRO de D: {[cls.__name__ for cls in D.__mro__]}")
    
    d = D()
    print(f"d.method() retorna: '{d.method()}'")
    
    # Llamar método específico usando super()
    class E(B, C):
        def method(self):
            return f"E -> {super().method()}"
    
    e = E()
    print(f"e.method() retorna: '{e.method()}'")
    print()

def demonstrate_bytecode():
    """Demostrar el bytecode de Python"""
    print("=== Bytecode de Python ===")
    
    def simple_function(x, y):
        z = x + y
        return z * 2
    
    def optimized_function(x, y):
        return (x + y) * 2
    
    print("Función simple:")
    print("def simple_function(x, y):")
    print("    z = x + y")
    print("    return z * 2")
    print()
    dis.dis(simple_function)
    
    print("\nFunción optimizada:")
    print("def optimized_function(x, y):")
    print("    return (x + y) * 2")
    print()
    dis.dis(optimized_function)

def demonstrate_gc_info():
    """Información sobre el garbage collector"""
    print("=== Garbage Collection ===")
    
    # Información sobre el GC
    print(f"Generaciones de GC: {len(gc.get_stats())}")
    print(f"Objetos rastreados: {len(gc.get_objects())}")
    print(f"Contadores de GC: {gc.get_count()}")
    
    # Crear referencias circulares
    class Node:
        def __init__(self, value):
            self.value = value
            self.children = []
            self.parent = None
        
        def add_child(self, child):
            child.parent = self
            self.children.append(child)
    
    # Crear estructura circular
    root = Node("root")
    child1 = Node("child1")
    child2 = Node("child2")
    
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(root)  # Referencia circular
    
    objects_before = len(gc.get_objects())
    
    # Eliminar referencias
    del root, child1, child2
    
    objects_after = len(gc.get_objects())
    
    print(f"Objetos antes: {objects_before}")
    print(f"Objetos después: {objects_after}")
    
    # Forzar garbage collection
    collected = gc.collect()
    objects_final = len(gc.get_objects())
    
    print(f"Objetos recolectados: {collected}")
    print(f"Objetos finales: {objects_final}")
    print()

def demonstrate_sys_info():
    """Información útil del módulo sys"""
    print("=== Información del Sistema ===")
    
    print(f"Versión de Python: {sys.version}")
    print(f"Plataforma: {sys.platform}")
    print(f"Tamaño máximo de enteros: {sys.maxsize}")
    print(f"Recursión máxima: {sys.getrecursionlimit()}")
    print(f"Encoding por defecto: {sys.getdefaultencoding()}")
    
    # Información de memoria
    import tracemalloc
    tracemalloc.start()
    
    # Crear algunos objetos
    data = [i**2 for i in range(10000)]
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"Memoria actual: {current / 1024 / 1024:.2f} MB")
    print(f"Memoria pico: {peak / 1024 / 1024:.2f} MB")
    
    tracemalloc.stop()
    print()

if __name__ == "__main__":
    demonstrate_underscore_repl()
    demonstrate_string_interning()
    demonstrate_small_integer_caching()
    demonstrate_debug_variable()
    demonstrate_mro()
    demonstrate_bytecode()
    demonstrate_gc_info()
    demonstrate_sys_info()
    
    print("=== Consejos ===")
    print("1. Usa python -O para optimizar (elimina asserts y __debug__)")
    print("2. Usa python -OO para optimizar más (elimina docstrings)")
    print("3. Usa python -m dis script.py para ver bytecode")
    print("4. Usa python -X dev para modo desarrollador")
    print("5. Usa PYTHONPATH para agregar directorios al path")