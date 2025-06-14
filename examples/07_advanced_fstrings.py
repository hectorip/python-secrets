"""
f-strings avanzados: Más que simple interpolación
Características poco conocidas de los f-strings
"""

import datetime
import math

def demonstrate_basic_formatting():
    """Formateo básico con f-strings"""
    print("=== Formateo Básico ===")
    
    name = "Python"
    version = 3.9
    pi = 3.14159265359
    
    # Formateo básico
    print(f"Lenguaje: {name}")
    print(f"Versión: {version}")
    
    # Especificadores de formato
    print(f"Pi con 2 decimales: {pi:.2f}")
    print(f"Pi en notación científica: {pi:e}")
    print(f"Pi con 8 dígitos totales: {pi:8.3f}")
    
    print()

def demonstrate_alignment_and_padding():
    """Alineación y padding"""
    print("=== Alineación y Padding ===")
    
    words = ["Python", "Java", "JavaScript", "Go", "Rust"]
    
    print("Alineación a la izquierda (por defecto):")
    for word in words:
        print(f"'{word:<15}' - {len(word)} caracteres")
    
    print("\nAlineación a la derecha:")
    for word in words:
        print(f"'{word:>15}' - {len(word)} caracteres")
    
    print("\nAlineación centrada:")
    for word in words:
        print(f"'{word:^15}' - {len(word)} caracteres")
    
    print("\nPadding con caracteres personalizados:")
    for word in words:
        print(f"'{word:*^15}'")
    
    print()

def demonstrate_number_formatting():
    """Formateo de números"""
    print("=== Formateo de Números ===")
    
    number = 1234567.89
    
    print(f"Número original: {number}")
    print(f"Con separadores de miles: {number:,}")
    print(f"Como porcentaje: {number/100:.2%}")
    print(f"Notación científica: {number:e}")
    print(f"Formato fijo: {number:.2f}")
    print(f"Formato general: {number:g}")
    
    # Números binarios, octales, hexadecimales
    num = 255
    print(f"\nNúmero: {num}")
    print(f"Binario: {num:b}")
    print(f"Octal: {num:o}")
    print(f"Hexadecimal: {num:x}")
    print(f"Hexadecimal mayúsculas: {num:X}")
    
    # Con prefijos
    print(f"Binario con prefijo: {num:#b}")
    print(f"Octal con prefijo: {num:#o}")
    print(f"Hex con prefijo: {num:#x}")
    
    print()

def demonstrate_debug_feature():
    """Característica de debug (Python 3.8+)"""
    print("=== Característica de Debug (Python 3.8+) ===")
    
    name = "Alice"
    age = 30
    salary = 75000.50
    
    # Debug automático con =
    print(f"{name=}")
    print(f"{age=}")
    print(f"{salary=}")
    
    # Combinado con formateo
    print(f"{salary=:,.2f}")
    print(f"{age=:>5}")
    
    # Con expresiones
    numbers = [1, 2, 3, 4, 5]
    print(f"{len(numbers)=}")
    print(f"{sum(numbers)=}")
    print(f"{max(numbers)=}")
    
    # Con cálculos
    x, y = 10, 20
    print(f"{x + y=}")
    print(f"{x * y=}")
    print(f"{x / y=:.2f}")
    
    print()

def demonstrate_expressions_in_fstrings():
    """Expresiones complejas en f-strings"""
    print("=== Expresiones Complejas ===")
    
    # Operaciones matemáticas
    radius = 5
    print(f"Radio: {radius}")
    print(f"Área del círculo: {math.pi * radius**2:.2f}")
    print(f"Circunferencia: {2 * math.pi * radius:.2f}")
    
    # Condicionales
    temperature = 25
    print(f"Temperatura: {temperature}°C ({'Caliente' if temperature > 30 else 'Agradable' if temperature > 20 else 'Frío'})")
    
    # List comprehensions
    numbers = range(1, 6)
    print(f"Números: {list(numbers)}")
    print(f"Cuadrados: {[n**2 for n in numbers]}")
    print(f"Suma de cuadrados: {sum(n**2 for n in numbers)}")
    
    # Llamadas a funciones
    text = "hello world"
    print(f"Texto original: '{text}'")
    print(f"Capitalizado: '{text.title()}'")
    print(f"Palabras: {len(text.split())}")
    
    print()

def demonstrate_datetime_formatting():
    """Formateo de fechas y horas"""
    print("=== Formateo de Fechas y Horas ===")
    
    now = datetime.datetime.now()
    birthday = datetime.date(1991, 12, 25)
    
    print(f"Ahora: {now}")
    print(f"Fecha: {now:%Y-%m-%d}")
    print(f"Hora: {now:%H:%M:%S}")
    print(f"Fecha completa: {now:%A, %B %d, %Y}")
    print(f"Formato ISO: {now:%Y-%m-%dT%H:%M:%S}")
    
    # Diferentes formatos
    print(f"\nCumpleaños: {birthday}")
    print(f"Formato US: {birthday:%m/%d/%Y}")
    print(f"Formato europeo: {birthday:%d/%m/%Y}")
    print(f"Formato largo: {birthday:%B %d, %Y}")
    print(f"Día de la semana: {birthday:%A}")
    
    # Cálculos con fechas
    age_days = (now.date() - birthday).days
    print(f"Días vividos: {age_days}")
    print(f"Años aproximados: {age_days / 365.25:.1f}")
    
    print()

def demonstrate_nested_formatting():
    """Formateo anidado y dinámico"""
    print("=== Formateo Anidado y Dinámico ===")
    
    # Formateo dinámico
    data = [
        ("Nombre", "Alice", 10),
        ("Edad", 30, 5),
        ("Ciudad", "Madrid", 15),
        ("Profesión", "Desarrolladora", 20)
    ]
    
    print("Formateo dinámico:")
    for label, value, width in data:
        print(f"{label}: {value:<{width}}")
    
    # Formateo anidado con diccionarios
    print("\nFormateo con diccionarios:")
    person = {
        'name': 'Bob',
        'age': 25,
        'city': 'Barcelona'
    }
    
    template = "Nombre: {name:<10} | Edad: {age:>3} | Ciudad: {city}"
    formatted = template.format(**person)
    print(formatted)
    
    # Con f-strings
    print(f"Nombre: {person['name']:<10} | Edad: {person['age']:>3} | Ciudad: {person['city']}")
    
    print()

def demonstrate_performance_comparison():
    """Comparación de rendimiento entre métodos de formateo"""
    print("=== Comparación de Rendimiento ===")
    
    import timeit
    
    name = "Python"
    version = 3.9
    
    # Definir diferentes métodos
    methods = [
        ("% formatting", "'Lenguaje: %s, Versión: %.1f' % (name, version)"),
        (".format()", "'Lenguaje: {}, Versión: {:.1f}'.format(name, version)"),
        ("f-string", "f'Lenguaje: {name}, Versión: {version:.1f}'"),
        ("Concatenación", "'Lenguaje: ' + name + ', Versión: ' + str(version)"),
    ]
    
    print("Tiempo de ejecución (por 1M iteraciones):")
    for method_name, code in methods:
        # Preparar el código con las variables
        setup = "name = 'Python'; version = 3.9"
        time_taken = timeit.timeit(code, setup=setup, number=1000000)
        print(f"{method_name:>15}: {time_taken:.4f} segundos")
    
    print("\n¡Los f-strings son generalmente los más rápidos!")
    print()

def demonstrate_advanced_tricks():
    """Trucos avanzados con f-strings"""
    print("=== Trucos Avanzados ===")
    
    # Formateo de múltiples variables con el mismo formato
    numbers = [1.23456, 2.34567, 3.45678, 4.56789]
    print("Números con 2 decimales:")
    for num in numbers:
        print(f"  {num:.2f}")
    
    # Formateo condicional
    def format_status(is_active):
        return f"Estado: {'🟢 Activo' if is_active else '🔴 Inactivo'}"
    
    print(f"\n{format_status(True)}")
    print(f"{format_status(False)}")
    
    # Formateo de estructuras de datos
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("\nMatriz:")
    for row in matrix:
        print(f"  {' '.join(f'{num:>3}' for num in row)}")
    
    # Formateo de bytes
    sizes = [1024, 1048576, 1073741824]
    print(f"\nTamaños en bytes:")
    for size in sizes:
        print(f"  {size:>12,} bytes = {size/1024**2:>8.1f} MB")
    
    # Formateo con clases personalizadas
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __format__(self, format_spec):
            if format_spec == 'polar':
                r = math.sqrt(self.x**2 + self.y**2)
                theta = math.atan2(self.y, self.x)
                return f"({r:.2f}, {theta:.2f})"
            return f"({self.x}, {self.y})"
    
    point = Point(3, 4)
    print(f"\nPunto cartesiano: {point}")
    print(f"Punto polar: {point:polar}")
    
    print()

if __name__ == "__main__":
    print("=== f-strings Avanzados ===")
    print("Explorando las capacidades ocultas de los f-strings\n")
    
    demonstrate_basic_formatting()
    demonstrate_alignment_and_padding()
    demonstrate_number_formatting()
    demonstrate_debug_feature()
    demonstrate_expressions_in_fstrings()
    demonstrate_datetime_formatting()
    demonstrate_nested_formatting()
    demonstrate_performance_comparison()
    demonstrate_advanced_tricks()
    
    print("=== Consejos ===")
    print("1. f-strings son generalmente más rápidos que otros métodos")
    print("2. Usa {variable=} para debug rápido (Python 3.8+)")
    print("3. Puedes usar expresiones complejas dentro de {}")
    print("4. Los especificadores de formato son muy poderosos")
    print("5. Implementa __format__ en tus clases para formateo personalizado")