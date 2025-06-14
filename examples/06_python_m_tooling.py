"""
Demostración de python -m: El Swiss Army Knife de Python
Módulos útiles que se pueden ejecutar directamente
"""

import subprocess
import sys
import json
import tempfile
import os
from pathlib import Path

def run_command(cmd, description):
    """Ejecutar comando y mostrar resultado"""
    print(f"\n=== {description} ===")
    print(f"Comando: {cmd}")
    print("Salida:")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("Error:", result.stderr)
    except subprocess.TimeoutExpired:
        print("Comando timed out")
    except Exception as e:
        print(f"Error ejecutando comando: {e}")

def demonstrate_json_tool():
    """Demostrar python -m json.tool"""
    print("=== python -m json.tool ===")
    
    # Crear archivo JSON desordenado
    messy_json = '{"name":"Python","version":3.9,"features":["dynamic","interpreted","object-oriented"],"active":true}'
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        f.write(messy_json)
        temp_file = f.name
    
    print("JSON original (una línea):")
    print(messy_json)
    
    # Formatear JSON
    print(f"\nFormateado con python -m json.tool:")
    run_command(f'python -m json.tool {temp_file}', "Formatear JSON")
    
    # Limpiar
    os.unlink(temp_file)

def demonstrate_http_server():
    """Demostrar servidor HTTP simple"""
    print("\n=== python -m http.server ===")
    print("Comando: python -m http.server 8000")
    print("Descripción: Inicia un servidor HTTP simple en el puerto 8000")
    print("Útil para: Servir archivos estáticos, testing rápido")
    print("URL: http://localhost:8000")
    print("Nota: Ctrl+C para detener")
    
    # También mostrar variantes
    print("\nVariantes útiles:")
    print("python -m http.server 8080                    # Puerto específico")
    print("python -m http.server --bind 127.0.0.1        # Bind a IP específica")
    print("python -m http.server --directory /path/to/dir # Directorio específico")

def demonstrate_timeit():
    """Demostrar python -m timeit"""
    print("\n=== python -m timeit ===")
    
    examples = [
        ("Lista por comprensión", "[x**2 for x in range(100)]"),
        ("Map function", "list(map(lambda x: x**2, range(100)))"),
        ("Loop tradicional", "''.join([str(i) for i in range(100)])"),
        ("String formatting", "'{}'.format(42)"),
        ("f-string", "f'{42}'"),
    ]
    
    for description, code in examples:
        print(f"\n{description}:")
        print(f"Código: {code}")
        run_command(f'python -m timeit "{code}"', f"Timing - {description}")

def demonstrate_pdb():
    """Demostrar python -m pdb"""
    print("\n=== python -m pdb ===")
    
    # Crear script de ejemplo para debug
    debug_script = '''
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def main():
    numbers = [3, 5, 7]
    results = []
    for num in numbers:
        result = factorial(num)
        results.append(result)
    
    print("Factoriales calculados:")
    for i, result in enumerate(results):
        print(f"{numbers[i]}! = {result}")

if __name__ == "__main__":
    main()
'''
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(debug_script)
        script_file = f.name
    
    print("Script creado para debugging:")
    print(debug_script)
    
    print(f"\nPara debuggear, ejecuta:")
    print(f"python -m pdb {script_file}")
    print("\nComandos útiles del debugger:")
    print("  l        - Mostrar código actual")
    print("  n        - Siguiente línea")
    print("  s        - Step into function")
    print("  c        - Continue")
    print("  p <var>  - Print variable")
    print("  b <line> - Set breakpoint")
    print("  q        - Quit")
    
    # Limpiar
    os.unlink(script_file)

def demonstrate_calendar():
    """Demostrar python -m calendar"""
    print("\n=== python -m calendar ===")
    print("Comando: python -m calendar 2024")
    run_command("python -m calendar 2024", "Mostrar calendario del año")
    
    print("\nComando: python -m calendar 2024 12")
    run_command("python -m calendar 2024 12", "Mostrar mes específico")

def demonstrate_platform():
    """Demostrar python -m platform"""
    print("\n=== python -m platform ===")
    run_command("python -m platform", "Información de la plataforma")

def demonstrate_zipfile():
    """Demostrar python -m zipfile"""
    print("\n=== python -m zipfile ===")
    
    # Crear archivos de ejemplo
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Crear algunos archivos
        (temp_path / "file1.txt").write_text("Contenido del archivo 1")
        (temp_path / "file2.txt").write_text("Contenido del archivo 2")
        (temp_path / "subdir").mkdir()
        (temp_path / "subdir" / "file3.txt").write_text("Archivo en subdirectorio")
        
        # Crear ZIP
        zip_file = temp_path / "example.zip"
        
        print("Archivos creados:")
        for file in temp_path.rglob("*"):
            if file.is_file() and not file.name.endswith('.zip'):
                print(f"  - {file.relative_to(temp_path)}")
        
        # Crear archivo ZIP
        files_to_zip = " ".join([str(f.relative_to(temp_path)) for f in temp_path.rglob("*.txt")])
        create_cmd = f"cd {temp_path} && python -m zipfile -c example.zip {files_to_zip}"
        run_command(create_cmd, "Crear archivo ZIP")
        
        # Listar contenido del ZIP
        list_cmd = f"python -m zipfile -l {zip_file}"
        run_command(list_cmd, "Listar contenido del ZIP")
        
        # Extraer ZIP
        extract_dir = temp_path / "extracted"
        extract_dir.mkdir()
        extract_cmd = f"cd {extract_dir} && python -m zipfile -e {zip_file} ."
        run_command(extract_cmd, "Extraer archivo ZIP")

def demonstrate_other_modules():
    """Otros módulos útiles con -m"""
    print("\n=== Otros Módulos Útiles ===")
    
    modules = [
        ("ast", "python -m ast script.py", "Mostrar AST de un archivo Python"),
        ("base64", "echo 'hello' | python -m base64", "Codificar/decodificar base64"),
        ("gzip", "python -m gzip file.txt", "Comprimir archivos"),
        ("hashlib", "echo 'hello' | python -m hashlib sha256", "Calcular hashes"),
        ("uuid", "python -m uuid", "Generar UUIDs"),
        ("webbrowser", "python -m webbrowser http://python.org", "Abrir URL en navegador"),
        ("xmlrpc.server", "python -m xmlrpc.server", "Servidor XML-RPC simple"),
        ("antigravity", "python -m antigravity", "Easter egg de XKCD 🚀"),
    ]
    
    for module, command, description in modules:
        print(f"\n{module}:")
        print(f"  Comando: {command}")
        print(f"  Descripción: {description}")

def demonstrate_pip_module():
    """Demostrar python -m pip"""
    print("\n=== python -m pip ===")
    print("Usar python -m pip en lugar de pip directamente es mejor práctica")
    print("Garantiza que uses el pip del intérprete correcto")
    
    commands = [
        ("python -m pip list", "Listar paquetes instalados"),
        ("python -m pip show requests", "Información detallada de un paquete"),
        ("python -m pip freeze", "Lista para requirements.txt"),
        ("python -m pip install -e .", "Instalación en modo desarrollo"),
        ("python -m pip install --user package", "Instalación para usuario actual"),
        ("python -m pip check", "Verificar dependencias"),
    ]
    
    for command, description in commands:
        print(f"\n{command}")
        print(f"  -> {description}")

if __name__ == "__main__":
    print("=== Demostración de python -m ===")
    print("Python incluye muchos módulos útiles que se pueden ejecutar directamente")
    
    demonstrate_json_tool()
    demonstrate_http_server()
    demonstrate_timeit()
    demonstrate_pdb()
    demonstrate_calendar()
    demonstrate_platform()
    demonstrate_zipfile()
    demonstrate_other_modules()
    demonstrate_pip_module()
    
    print("\n=== Consejos ===")
    print("1. python -m módulo es más seguro que ejecutar scripts directamente")
    print("2. Garantiza usar el intérprete correcto en entornos virtuales")
    print("3. Muchos módulos estándar tienen funcionalidad CLI oculta")
    print("4. Usa python -h para ver opciones del intérprete")
    print("5. python -c 'código' para ejecutar código inline")