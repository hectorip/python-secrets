"""
Interoperabilidad de Python con otros sistemas
Ejemplos de ctypes, subprocess, multiprocessing y más
"""

import ctypes
import subprocess
import multiprocessing
import time
import os
import sys
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import platform

def demonstrate_ctypes():
    """Demostrar el uso de ctypes para llamar bibliotecas C"""
    print("=== ctypes - Llamar bibliotecas C ===")
    
    try:
        # Determinar la biblioteca C según el sistema
        if platform.system() == "Windows":
            libc = ctypes.CDLL("msvcrt.dll")
            libm = ctypes.CDLL("msvcrt.dll")  # En Windows, math está en msvcrt
        elif platform.system() == "Darwin":  # macOS
            libc = ctypes.CDLL("libc.dylib")
            try:
                libm = ctypes.CDLL("libm.dylib")
            except:
                libm = ctypes.CDLL("libm.dylib")
        else:  # Linux y otros Unix
            libc = ctypes.CDLL("libc.so.6")
            libm = ctypes.CDLL("libm.so.6")
        
        print("✅ Bibliotecas C cargadas exitosamente")
        
        # Ejemplo 1: Usar printf de C
        print("\n1. Usando printf de C:")
        libc.printf(b"Hola desde C con printf!\n")
        
        # Ejemplo 2: Funciones matemáticas de C
        print("\n2. Funciones matemáticas de C:")
        
        # Configurar tipos para cos()
        if hasattr(libm, 'cos'):
            libm.cos.argtypes = [ctypes.c_double]
            libm.cos.restype = ctypes.c_double
            
            angle = 0.0  # 0 radianes
            cos_result = libm.cos(angle)
            print(f"cos(0) desde C: {cos_result}")
        
        # Ejemplo 3: Trabajar con memoria
        print("\n3. Trabajando con memoria:")
        
        # Alocar memoria
        size = 1024
        ptr = libc.malloc(size)
        print(f"Memoria alocada en: 0x{ptr:x}")
        
        # Liberar memoria
        libc.free(ptr)
        print("Memoria liberada")
        
        # Ejemplo 4: Estructuras C
        print("\n4. Estructuras C:")
        
        class Point(ctypes.Structure):
            _fields_ = [("x", ctypes.c_double),
                       ("y", ctypes.c_double)]
        
        point = Point(3.0, 4.0)
        print(f"Punto: ({point.x}, {point.y})")
        
        # Calcular distancia al origen
        distance = (point.x**2 + point.y**2)**0.5
        print(f"Distancia al origen: {distance}")
        
    except Exception as e:
        print(f"❌ Error con ctypes: {e}")
        print("Nota: ctypes puede no funcionar en todos los sistemas")
    
    print()

def demonstrate_subprocess():
    """Demostrar subprocess para ejecutar programas externos"""
    print("=== subprocess - Ejecutar programas externos ===")
    
    # Ejemplo 1: Comando simple
    print("1. Comando simple:")
    try:
        result = subprocess.run(['echo', 'Hola desde subprocess'], 
                              capture_output=True, text=True)
        print(f"Salida: {result.stdout.strip()}")
        print(f"Código de retorno: {result.returncode}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Ejemplo 2: Comando con shell
    print("\n2. Comando con shell:")
    try:
        if platform.system() == "Windows":
            cmd = 'echo "Contando archivos" && dir /b | find /c /v ""'
        else:
            cmd = 'echo "Contando archivos" && ls -1 | wc -l'
        
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(f"Salida:\n{result.stdout}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Ejemplo 3: Pipeline de comandos
    print("3. Pipeline de comandos:")
    try:
        if platform.system() != "Windows":
            # Crear datos de prueba
            p1 = subprocess.Popen(['echo', 'manzana\nbanana\nnaranja\nmanzana'], 
                                 stdout=subprocess.PIPE, text=True)
            p2 = subprocess.Popen(['sort'], stdin=p1.stdout, 
                                 stdout=subprocess.PIPE, text=True)
            p1.stdout.close()  # Permite que p1 reciba SIGPIPE si p2 sale
            p3 = subprocess.Popen(['uniq', '-c'], stdin=p2.stdout, 
                                 stdout=subprocess.PIPE, text=True)
            p2.stdout.close()
            
            output, _ = p3.communicate()
            print(f"Resultado del pipeline:\n{output}")
        else:
            print("Pipeline no disponible en Windows")
    except Exception as e:
        print(f"Error en pipeline: {e}")
    
    # Ejemplo 4: Ejecutar Python desde Python
    print("\n4. Ejecutar código Python externo:")
    python_code = '''
import sys
print(f"Python version: {sys.version}")
print("Ejecutándose desde subprocess")
for i in range(3):
    print(f"Contador: {i}")
'''
    
    try:
        result = subprocess.run([sys.executable, '-c', python_code], 
                              capture_output=True, text=True)
        print(f"Salida:\n{result.stdout}")
    except Exception as e:
        print(f"Error: {e}")
    
    print()

def cpu_intensive_task(n):
    """Tarea que usa mucho CPU para demostrar multiprocessing"""
    total = 0
    for i in range(n * 1000000):
        total += i ** 2
    return total

def io_intensive_task(delay):
    """Tarea que simula I/O para demostrar threading"""
    time.sleep(delay)
    return f"Tarea completada después de {delay}s"

def demonstrate_multiprocessing():
    """Demostrar multiprocessing para paralelismo real"""
    print("=== multiprocessing - Paralelismo real ===")
    
    # Obtener número de CPUs
    cpu_count = multiprocessing.cpu_count()
    print(f"CPUs disponibles: {cpu_count}")
    
    # Ejemplo 1: Pool básico
    print("\n1. Pool de procesos básico:")
    
    tasks = [100, 200, 300, 400]
    
    # Ejecución secuencial
    start_time = time.time()
    sequential_results = [cpu_intensive_task(task) for task in tasks]
    sequential_time = time.time() - start_time
    
    # Ejecución paralela
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        parallel_results = pool.map(cpu_intensive_task, tasks)
    parallel_time = time.time() - start_time
    
    print(f"Tiempo secuencial: {sequential_time:.2f}s")
    print(f"Tiempo paralelo: {parallel_time:.2f}s")
    print(f"Speedup: {sequential_time/parallel_time:.2f}x")
    
    # Ejemplo 2: ProcessPoolExecutor
    print("\n2. ProcessPoolExecutor:")
    
    with ProcessPoolExecutor(max_workers=cpu_count) as executor:
        start_time = time.time()
        futures = [executor.submit(cpu_intensive_task, task) for task in tasks]
        results = [future.result() for future in futures]
        executor_time = time.time() - start_time
    
    print(f"Tiempo con ProcessPoolExecutor: {executor_time:.2f}s")
    
    # Ejemplo 3: Comparar con threading para I/O
    print("\n3. Threading vs Multiprocessing para I/O:")
    
    io_tasks = [0.5, 0.5, 0.5, 0.5]
    
    # Threading para I/O
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        thread_futures = [executor.submit(io_intensive_task, task) for task in io_tasks]
        thread_results = [future.result() for future in thread_futures]
    thread_time = time.time() - start_time
    
    # Multiprocessing para I/O (menos eficiente)
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        process_futures = [executor.submit(io_intensive_task, task) for task in io_tasks]
        process_results = [future.result() for future in process_futures]
    process_time = time.time() - start_time
    
    print(f"Threading para I/O: {thread_time:.2f}s")
    print(f"Multiprocessing para I/O: {process_time:.2f}s")
    print("→ Threading es mejor para I/O, multiprocessing para CPU")
    
    print()

def demonstrate_system_integration():
    """Demostrar integración con el sistema"""
    print("=== Integración con el Sistema ===")
    
    # Información del sistema
    print("1. Información del sistema:")
    print(f"Plataforma: {platform.platform()}")
    print(f"Sistema: {platform.system()}")
    print(f"Versión: {platform.version()}")
    print(f"Arquitectura: {platform.architecture()}")
    print(f"Procesador: {platform.processor()}")
    print(f"Nombre del host: {platform.node()}")
    
    # Variables de entorno
    print("\n2. Variables de entorno importantes:")
    env_vars = ['PATH', 'HOME', 'USER', 'SHELL', 'PYTHONPATH']
    for var in env_vars:
        value = os.environ.get(var, 'No definida')
        if var == 'PATH':
            print(f"{var}: {len(value.split(os.pathsep))} directorios")
        else:
            print(f"{var}: {value}")
    
    # Información de procesos
    print(f"\n3. Información del proceso:")
    print(f"PID: {os.getpid()}")
    print(f"PPID: {os.getppid()}")
    print(f"UID: {os.getuid() if hasattr(os, 'getuid') else 'N/A'}")
    print(f"Directorio de trabajo: {os.getcwd()}")
    
    # Recursos del sistema
    print(f"\n4. Recursos:")
    if hasattr(os, 'getloadavg'):
        load = os.getloadavg()
        print(f"Load average: {load}")
    
    print(f"Memoria disponible para Python: {sys.maxsize} bytes")
    
    print()

def demonstrate_foreign_function_interface():
    """Ejemplo avanzado de FFI"""
    print("=== Foreign Function Interface Avanzado ===")
    
    try:
        # Crear una función C simple en memoria (solo Linux/macOS)
        if platform.system() in ['Linux', 'Darwin']:
            print("Ejemplo de creación de función C en memoria:")
            
            # Este es un ejemplo teórico - en la práctica necesitarías
            # un compilador JIT como numba o compilar C código
            print("Normalmente usarías:")
            print("- numba para JIT compilation")
            print("- Cython para código Python-like que compila a C")
            print("- cffi para interface más amigable con C")
            print("- pybind11 para C++")
            
            # Ejemplo con cffi (si estuviera instalado)
            example_cffi = '''
from cffi import FFI

ffi = FFI()
ffi.cdef("""
    int add(int a, int b);
""")

# Código C inline
lib = ffi.verify("""
    int add(int a, int b) {
        return a + b;
    }
""")

result = lib.add(5, 3)
print(f"5 + 3 = {result}")
'''
            print("\nEjemplo con cffi:")
            print(example_cffi)
        
        else:
            print("FFI avanzado es más limitado en Windows")
    
    except Exception as e:
        print(f"Error en FFI: {e}")
    
    print()

def demonstrate_python_c_extensions():
    """Información sobre extensiones C de Python"""
    print("=== Extensiones C de Python ===")
    
    # Mostrar módulos que son extensiones C
    print("Módulos C integrados en Python:")
    import sys
    
    builtin_modules = []
    for name in sys.builtin_module_names:
        builtin_modules.append(name)
    
    print(f"Total de módulos built-in: {len(builtin_modules)}")
    print("Algunos ejemplos:")
    for module in sorted(builtin_modules)[:10]:
        print(f"  - {module}")
    
    # Información sobre extensiones cargadas
    print(f"\nMódulos cargados: {len(sys.modules)}")
    
    # Ejemplos de módulos populares que son extensiones C
    c_extensions = {
        'numpy': 'Computación numérica',
        'pandas': 'Análisis de datos',
        'lxml': 'Procesamiento XML',
        'Pillow': 'Procesamiento de imágenes',
        'psycopg2': 'PostgreSQL driver',
        'sqlite3': 'SQLite database (built-in)',
    }
    
    print("\nExtensiones C populares:")
    for ext, desc in c_extensions.items():
        try:
            __import__(ext)
            status = "✅ Instalado"
        except ImportError:
            status = "❌ No instalado"
        print(f"  {ext:12} - {desc} ({status})")
    
    print()

if __name__ == "__main__":
    print("=== Interoperabilidad de Python ===")
    print("Demostrando cómo Python interactúa con otros sistemas\n")
    
    demonstrate_ctypes()
    demonstrate_subprocess()
    demonstrate_multiprocessing()
    demonstrate_system_integration()
    demonstrate_foreign_function_interface()
    demonstrate_python_c_extensions()
    
    print("=== Casos de Uso Comunes ===")
    print("1. ctypes: Llamar bibliotecas C existentes")
    print("2. subprocess: Ejecutar herramientas de línea de comandos")
    print("3. multiprocessing: Paralelismo para tareas CPU-intensivas")
    print("4. threading: Concurrencia para I/O")
    print("5. Extensiones C: Máximo rendimiento para código crítico")
    print("6. FFI: Integración con bibliotecas nativas")
    
    print("\n=== Herramientas Recomendadas ===")
    print("- numba: JIT compilation para Python")
    print("- Cython: Python-like syntax que compila a C")
    print("- cffi: Interface más amigable con C")
    print("- pybind11: Binding fácil con C++")
    print("- ctypes: Built-in, bueno para bibliotecas simples")