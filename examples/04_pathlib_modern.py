"""
Ejemplo de pathlib - Manejo moderno de rutas
Comparación entre os.path y pathlib
"""

from pathlib import Path
import os
import tempfile
from datetime import datetime

def demo_pathlib_vs_os_path():
    """Comparar pathlib con os.path"""
    
    print("=== Comparación pathlib vs os.path ===\n")
    
    # Crear directorio temporal para ejemplos
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # 1. Construcción de rutas
        print("1. Construcción de rutas:")
        
        # Método tradicional
        old_way = os.path.join(temp_dir, "subdir", "file.txt")
        print(f"os.path: {old_way}")
        
        # Método moderno
        new_way = temp_path / "subdir" / "file.txt"
        print(f"pathlib: {new_way}")
        
        print()
        
        # 2. Crear estructura de directorios
        print("2. Creando estructura de directorios:")
        
        # Crear algunos archivos y directorios
        (temp_path / "docs").mkdir()
        (temp_path / "src").mkdir()
        (temp_path / "tests").mkdir()
        
        # Crear archivos
        (temp_path / "README.md").write_text("# Mi Proyecto\n\nDescripción del proyecto")
        (temp_path / "src" / "main.py").write_text("print('Hello World')")
        (temp_path / "src" / "utils.py").write_text("def helper(): pass")
        (temp_path / "tests" / "test_main.py").write_text("def test_hello(): assert True")
        (temp_path / "docs" / "manual.txt").write_text("Manual de usuario")
        
        print(f"Estructura creada en: {temp_path}")
        
        # 3. Navegación y consultas
        print("\n3. Información de archivos:")
        
        readme = temp_path / "README.md"
        print(f"Archivo: {readme.name}")
        print(f"Extensión: {readme.suffix}")
        print(f"Nombre sin extensión: {readme.stem}")
        print(f"Directorio padre: {readme.parent}")
        print(f"Existe: {readme.exists()}")
        print(f"Es archivo: {readme.is_file()}")
        print(f"Tamaño: {readme.stat().st_size} bytes")
        
        # 4. Buscar archivos
        print("\n4. Buscar archivos:")
        
        # Todos los archivos Python
        py_files = list(temp_path.rglob("*.py"))
        print(f"Archivos .py encontrados: {len(py_files)}")
        for py_file in py_files:
            print(f"  - {py_file.relative_to(temp_path)}")
        
        # Archivos en directorio específico
        src_files = list((temp_path / "src").iterdir())
        print(f"\nArchivos en src/: {len(src_files)}")
        for src_file in src_files:
            print(f"  - {src_file.name}")
        
        # 5. Operaciones con contenido
        print("\n5. Operaciones con contenido:")
        
        # Leer archivo
        content = readme.read_text()
        print(f"Contenido de README.md:")
        print(content)
        
        # Escribir a archivo
        config_file = temp_path / "config.json"
        config_content = '{\n  "debug": true,\n  "port": 8000\n}'
        config_file.write_text(config_content)
        print(f"\nArchivo config.json creado")
        
        # 6. Métodos útiles
        print("\n6. Métodos útiles de Path:")
        
        sample_path = Path("/home/user/documents/projects/my_app/src/main.py")
        print(f"Ruta de ejemplo: {sample_path}")
        print(f"  .name: {sample_path.name}")
        print(f"  .parent: {sample_path.parent}")
        print(f"  .parents[1]: {sample_path.parents[1]}")
        print(f"  .suffix: {sample_path.suffix}")
        print(f"  .suffixes: {sample_path.suffixes}")
        print(f"  .stem: {sample_path.stem}")
        print(f"  .anchor: {sample_path.anchor}")
        print(f"  .parts: {sample_path.parts}")
        
        # 7. Rutas especiales
        print("\n7. Rutas especiales:")
        print(f"Home: {Path.home()}")
        print(f"Directorio actual: {Path.cwd()}")
        
        # 8. Comparaciones y operaciones
        print("\n8. Operaciones avanzadas:")
        
        # Cambiar extensión
        python_file = Path("script.py")
        text_file = python_file.with_suffix(".txt")
        print(f"Cambiar extensión: {python_file} -> {text_file}")
        
        # Cambiar nombre
        new_name = python_file.with_name("new_script.py")
        print(f"Cambiar nombre: {python_file} -> {new_name}")
        
        # Resolver rutas relativas
        relative_path = Path("../docs/./manual.txt")
        try:
            resolved = relative_path.resolve()
            print(f"Resolver ruta: {relative_path} -> {resolved}")
        except:
            print(f"Resolver ruta: {relative_path} -> (no existe)")

def demonstrate_path_utilities():
    """Demostrar utilidades adicionales de pathlib"""
    print("\n\n=== Utilidades adicionales ===\n")
    
    # Trabajar con rutas URL-like
    base = Path("https://example.com/api/v1")
    endpoint = base / "users" / "123" / "profile"
    print(f"URL-like path: {endpoint}")
    
    # Trabajo con archivos temporales
    import tempfile
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_path = Path(f.name)
        f.write('{"temp": true}')
    
    print(f"Archivo temporal: {temp_path}")
    print(f"Contenido: {temp_path.read_text()}")
    
    # Limpiar
    temp_path.unlink()
    print("Archivo temporal eliminado")

if __name__ == "__main__":
    demo_pathlib_vs_os_path()
    demonstrate_path_utilities()