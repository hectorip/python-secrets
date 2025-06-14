# Ejemplos de Código - Secretos de Python

Este directorio contiene ejemplos prácticos de las características poco conocidas de Python presentadas en la charla.

## Estructura de Archivos

### 📚 Biblioteca Estándar
- **`01_collections_chainmap.py`** - Demostración de `collections.ChainMap` para combinar diccionarios
- **`02_singledispatch.py`** - Sobrecarga de funciones con `functools.singledispatch`
- **`03_contextmanager.py`** - Context managers personalizados con `contextlib.contextmanager`
- **`04_pathlib_modern.py`** - Manejo moderno de rutas con `pathlib`

### ⚙️ Intérpretes
- **`05_interpreter_secrets.py`** - Secretos del intérprete: MRO, string interning, caching, etc.

### 🛠️ Tooling
- **`06_python_m_tooling.py`** - Demostración de módulos ejecutables con `python -m`
- **`07_advanced_fstrings.py`** - f-strings avanzados con formateo complejo

### 🔗 Interoperabilidad
- **`08_interoperability.py`** - ctypes, subprocess, multiprocessing e integración con C

### 🌟 Comunidad
- **`09_community_innovations.py`** - Simulaciones de bibliotecas innovadoras (FastAPI, Rich, Typer, etc.)

### ✨ Características Únicas
- **`10_unique_features.py`** - Lo que hace único a Python: objetos, comprehensions, generators, etc.

## Cómo Ejecutar los Ejemplos

Cada archivo se puede ejecutar independientemente:

```bash
# Ejecutar un ejemplo específico
python examples/01_collections_chainmap.py

# Ejecutar todos los ejemplos
for file in examples/*.py; do
    echo "=== Ejecutando $file ==="
    python "$file"
    echo
done
```

## Requisitos

Los ejemplos están diseñados para funcionar con Python 3.8+ y solo usan la biblioteca estándar, excepto por algunas simulaciones que muestran cómo funcionarían bibliotecas externas.

## Notas Especiales

### Ejemplos Asíncronos
- `09_community_innovations.py` incluye ejemplos de asyncio que requieren ejecutarse con `asyncio.run()`

### Ejemplos de Sistema
- `08_interoperability.py` incluye ejemplos específicos del sistema operativo
- Algunos ejemplos pueden funcionar diferente en Windows vs Unix/Linux/macOS

### Ejemplos con Archivos Temporales
Varios ejemplos crean archivos temporales para demostración y los limpian automáticamente.

## Estructura de Cada Ejemplo

Cada archivo sigue esta estructura:
1. **Docstring** explicando el propósito
2. **Funciones de demostración** organizadas por tema
3. **Función main** que ejecuta todas las demostraciones
4. **Comentarios explicativos** en el código

## Conceptos Cubiertos

### Nivel Básico
- Uso básico de características poco conocidas
- Comparaciones con enfoques tradicionales
- Casos de uso comunes

### Nivel Intermedio
- Patrones avanzados
- Optimizaciones
- Integración con otras herramientas

### Nivel Avanzado
- Metaclasses
- Descriptors
- Introspección profunda
- Interoperabilidad con C

## Tips para Aprender

1. **Ejecuta los ejemplos** - No solo leas el código
2. **Modifica los parámetros** - Experimenta con diferentes valores
3. **Combina conceptos** - Usa múltiples características juntas
4. **Lee los errores** - Los ejemplos incluyen manejo de errores educativo
5. **Consulta la documentación** - Cada ejemplo incluye referencias

## Recursos Adicionales

- [Documentación oficial de Python](https://docs.python.org/3/)
- [PEP Index](https://www.python.org/dev/peps/) - Propuestas de mejora de Python
- [Python Enhancement Proposals](https://peps.python.org/)
- [Real Python](https://realpython.com/) - Tutoriales avanzados

## Contribuciones

Si encuentras errores o tienes ideas para mejoras:
1. Los ejemplos están diseñados para ser educativos, no necesariamente para producción
2. Prioriza la claridad sobre la eficiencia
3. Incluye comentarios explicativos
4. Mantén compatibilidad con Python 3.8+

¡Disfruta explorando los secretos de Python! 🐍✨