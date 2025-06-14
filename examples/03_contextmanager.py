"""
Ejemplo de contextlib.contextmanager
Crear context managers usando decoradores
"""

from contextlib import contextmanager
import time
import sqlite3
import tempfile
import os

@contextmanager
def timer(description="Operación"):
    """Context manager para medir tiempo de ejecución"""
    print(f"Iniciando: {description}")
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"Completado: {description} en {elapsed:.3f} segundos")

@contextmanager
def temporary_database():
    """Context manager para base de datos temporal"""
    # Crear archivo temporal
    fd, path = tempfile.mkstemp(suffix='.db')
    os.close(fd)
    
    try:
        # Crear conexión
        conn = sqlite3.connect(path)
        conn.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE
            )
        ''')
        conn.commit()
        
        print(f"Base de datos temporal creada: {path}")
        yield conn
        
    finally:
        # Limpiar recursos
        if 'conn' in locals():
            conn.close()
        if os.path.exists(path):
            os.unlink(path)
        print("Base de datos temporal eliminada")

@contextmanager
def suppress_output():
    """Context manager para suprimir salida estándar"""
    import sys
    from io import StringIO
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        yield
    finally:
        sys.stdout = old_stdout

@contextmanager
def changed_directory(path):
    """Context manager para cambiar directorio temporalmente"""
    old_cwd = os.getcwd()
    try:
        os.chdir(path)
        yield os.getcwd()
    finally:
        os.chdir(old_cwd)

# Ejemplos de uso
if __name__ == "__main__":
    print("=== Context Managers Personalizados ===\n")
    
    # 1. Timer
    with timer("Cálculo pesado"):
        time.sleep(1)
        result = sum(range(1000000))
    
    print()
    
    # 2. Base de datos temporal
    with temporary_database() as db:
        db.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                  ("Alice", "alice@example.com"))
        db.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                  ("Bob", "bob@example.com"))
        db.commit()
        
        cursor = db.execute("SELECT name, email FROM users")
        users = cursor.fetchall()
        print("Usuarios en DB temporal:")
        for name, email in users:
            print(f"  - {name}: {email}")
    
    print()
    
    # 3. Suprimir salida
    print("Esta línea se ve")
    with suppress_output():
        print("Esta línea NO se ve")
        print("Esta tampoco")
    print("Esta línea se ve de nuevo")
    
    print()
    
    # 4. Cambiar directorio
    print(f"Directorio actual: {os.getcwd()}")
    with changed_directory("/tmp"):
        print(f"Directorio temporal: {os.getcwd()}")
    print(f"Directorio restaurado: {os.getcwd()}")