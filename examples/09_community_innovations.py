"""
Innovaciones de la Comunidad Python
Ejemplos de bibliotecas que revolucionaron Python
"""

import asyncio
import time
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
import json

# Simulamos algunas bibliotecas populares con ejemplos simplificados

def demonstrate_fastapi_style():
    """Simular el estilo de FastAPI"""
    print("=== FastAPI Style - APIs Modernas ===")
    
    # Simulamos decoradores y modelos tipo FastAPI
    class APIRouter:
        def __init__(self):
            self.routes = []
        
        def get(self, path: str):
            def decorator(func):
                self.routes.append(('GET', path, func))
                return func
            return decorator
        
        def post(self, path: str):
            def decorator(func):
                self.routes.append(('POST', path, func))
                return func
            return decorator
    
    @dataclass
    class User:
        name: str
        age: int
        email: Optional[str] = None
    
    @dataclass
    class UserResponse:
        id: int
        user: User
        created_at: str
    
    # Simular una aplicación FastAPI
    app = APIRouter()
    
    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    
    @app.get("/users/{user_id}")
    async def get_user(user_id: int):
        return UserResponse(
            id=user_id,
            user=User(name="Alice", age=30, email="alice@example.com"),
            created_at="2024-01-01T00:00:00"
        )
    
    @app.post("/users/")
    async def create_user(user: User):
        return UserResponse(
            id=123,
            user=user,
            created_at="2024-01-01T00:00:00"
        )
    
    print("Rutas definidas:")
    for method, path, func in app.routes:
        print(f"  {method:4} {path:15} -> {func.__name__}")
    
    print("\nCaracterísticas de FastAPI:")
    print("✅ Type hints automáticos")
    print("✅ Validación de datos con Pydantic")
    print("✅ Documentación automática (OpenAPI/Swagger)")
    print("✅ Async/await nativo")
    print("✅ Inyección de dependencias")
    print()

def demonstrate_pydantic_style():
    """Simular el estilo de Pydantic"""
    print("=== Pydantic Style - Validación de Datos ===")
    
    # Simulamos validación estilo Pydantic
    class ValidationError(Exception):
        pass
    
    class BaseModel:
        def __init__(self, **kwargs):
            self._data = {}
            for field_name, field_type in self.__annotations__.items():
                value = kwargs.get(field_name)
                if value is None and hasattr(self, field_name):
                    value = getattr(self, field_name)
                
                # Validación básica de tipos
                if value is not None:
                    if field_type == int and not isinstance(value, int):
                        try:
                            value = int(value)
                        except ValueError:
                            raise ValidationError(f"{field_name} debe ser int")
                    elif field_type == str and not isinstance(value, str):
                        value = str(value)
                
                self._data[field_name] = value
                setattr(self, field_name, value)
        
        def dict(self):
            return self._data.copy()
        
        def json(self):
            return json.dumps(self._data, default=str)
    
    # Modelos de ejemplo
    class Address(BaseModel):
        street: str
        city: str
        country: str = "España"
    
    class Person(BaseModel):
        name: str
        age: int
        email: Optional[str] = None
        addresses: List[Address] = None
    
    # Uso de los modelos
    print("Creando persona con validación:")
    try:
        person = Person(
            name="Juan",
            age="30",  # String que se convierte a int
            email="juan@example.com"
        )
        print(f"✅ Persona creada: {person.name}, {person.age} años")
        print(f"   JSON: {person.json()}")
    except ValidationError as e:
        print(f"❌ Error de validación: {e}")
    
    print("\nCaracterísticas de Pydantic:")
    print("✅ Validación automática de tipos")
    print("✅ Serialización/deserialización JSON")
    print("✅ Validadores personalizados")
    print("✅ Integración con FastAPI")
    print("✅ Parsing de datos complejos")
    print()

def demonstrate_rich_style():
    """Simular el estilo de Rich"""
    print("=== Rich Style - Terminal con Estilo ===")
    
    # Simulamos funcionalidades de Rich
    class Console:
        def print(self, *args, style=None, **kwargs):
            text = " ".join(str(arg) for arg in args)
            if style:
                if "bold" in style:
                    text = f"**{text}**"
                if "red" in style:
                    text = f"🔴 {text}"
                elif "green" in style:
                    text = f"🟢 {text}"
                elif "blue" in style:
                    text = f"🔵 {text}"
            print(text)
        
        def rule(self, title=""):
            print(f"\n{'='*50}")
            if title:
                print(f"  {title}")
            print(f"{'='*50}")
    
    class Table:
        def __init__(self, title=None):
            self.title = title
            self.columns = []
            self.rows = []
        
        def add_column(self, header, style=None):
            self.columns.append((header, style))
        
        def add_row(self, *cells):
            self.rows.append(cells)
        
        def show(self):
            if self.title:
                print(f"\n📊 {self.title}")
            
            # Headers
            headers = [col[0] for col in self.columns]
            print(f"│ {' │ '.join(f'{h:^15}' for h in headers)} │")
            print(f"├{'─' * (17 * len(headers) - 1)}┤")
            
            # Rows
            for row in self.rows:
                formatted_row = []
                for i, cell in enumerate(row):
                    if i < len(self.columns) and self.columns[i][1]:
                        style = self.columns[i][1]
                        if "cyan" in style:
                            cell = f"🔷 {cell}"
                        elif "magenta" in style:
                            cell = f"🔻 {cell}"
                    formatted_row.append(f'{str(cell):^15}')
                print(f"│ {' │ '.join(formatted_row)} │")
    
    class Progress:
        def track(self, iterable, description="Processing"):
            total = len(iterable) if hasattr(iterable, '__len__') else 100
            for i, item in enumerate(iterable):
                progress = (i + 1) / total * 100
                bar_length = 30
                filled_length = int(bar_length * progress // 100)
                bar = '█' * filled_length + '▒' * (bar_length - filled_length)
                print(f"\r{description}: [{bar}] {progress:.1f}%", end='', flush=True)
                yield item
            print()  # Nueva línea al final
    
    # Demostración
    console = Console()
    progress = Progress()
    
    console.rule("Demostración de Rich")
    
    console.print("Texto normal")
    console.print("Texto en rojo", style="red")
    console.print("Texto en verde y bold", style="green bold")
    
    # Tabla
    table = Table(title="Resultados de Rendimiento")
    table.add_column("Algoritmo", style="cyan")
    table.add_column("Tiempo (ms)", style="magenta")
    table.add_column("Memoria (MB)", style="green")
    
    table.add_row("Quicksort", "1.2", "0.5")
    table.add_row("Mergesort", "1.8", "1.2")
    table.add_row("Heapsort", "2.1", "0.3")
    
    table.show()
    
    # Barra de progreso
    print("\nBarra de progreso:")
    data = range(20)
    for item in progress.track(data, "Procesando datos"):
        time.sleep(0.05)  # Simular trabajo
    
    print("\nCaracterísticas de Rich:")
    print("✅ Texto con colores y estilos")
    print("✅ Tablas formateadas")  
    print("✅ Barras de progreso")
    print("✅ Syntax highlighting")
    print("✅ Paneles y layouts")
    print()

def demonstrate_typer_style():
    """Simular el estilo de Typer"""
    print("=== Typer Style - CLIs con Type Hints ===")
    
    # Simulamos Typer
    class Typer:
        def __init__(self):
            self.commands = {}
        
        def command(self, name=None):
            def decorator(func):
                cmd_name = name or func.__name__
                self.commands[cmd_name] = func
                return func
            return decorator
        
        def run(self, func):
            # Simular ejecución de comando
            import inspect
            sig = inspect.signature(func)
            
            print(f"Comando: {func.__name__}")
            print(f"Parámetros:")
            for param_name, param in sig.parameters.items():
                param_type = param.annotation if param.annotation != param.empty else "any"
                default = param.default if param.default != param.empty else "required"
                print(f"  --{param_name}: {param_type} (default: {default})")
            
            # Simular ejecución con valores por defecto
            kwargs = {}
            for param_name, param in sig.parameters.items():
                if param.default != param.empty:
                    kwargs[param_name] = param.default
                else:
                    # Valores de ejemplo
                    if param.annotation == str:
                        kwargs[param_name] = "ejemplo"
                    elif param.annotation == int:
                        kwargs[param_name] = 42
                    elif param.annotation == bool:
                        kwargs[param_name] = False
            
            print(f"\nEjecutando con: {kwargs}")
            return func(**kwargs)
    
    # Aplicación CLI de ejemplo
    app = Typer()
    
    @app.command()
    def hello(name: str, age: int = 25, formal: bool = False):
        """Saludar a alguien de manera personalizada."""
        greeting = "Buenos días" if formal else "Hola"
        print(f"{greeting} {name}, tienes {age} años")
        return f"Comando ejecutado: hello {name}"
    
    @app.command("process-data")
    def process_data(input_file: str, output_file: str = "output.txt", verbose: bool = False):
        """Procesar archivo de datos."""
        if verbose:
            print(f"Procesando {input_file} -> {output_file}")
        return f"Archivo procesado: {input_file} -> {output_file}"
    
    # Demostración
    print("Comandos disponibles:")
    for cmd_name, func in app.commands.items():
        print(f"  {cmd_name}: {func.__doc__}")
    
    print("\nEjecutando comandos:")
    app.run(hello)
    print()
    app.run(process_data)
    
    print("\nCaracterísticas de Typer:")
    print("✅ Type hints automáticos para CLI")
    print("✅ Validación de argumentos")
    print("✅ Ayuda automática")
    print("✅ Subcomandos")
    print("✅ Autocompletado")
    print()

async def demonstrate_asyncio_patterns():
    """Demostrar patrones async/await modernos"""
    print("=== AsyncIO - Programación Asíncrona ===")
    
    # Simular operaciones asíncronas
    async def fetch_data(url: str, delay: float = 1.0):
        """Simular fetch de datos asíncrono"""
        print(f"  Iniciando fetch: {url}")
        await asyncio.sleep(delay)
        return f"Datos de {url}"
    
    async def process_data(data: str):
        """Simular procesamiento asíncrono"""
        await asyncio.sleep(0.5)
        return f"Procesado: {data}"
    
    # Patrón 1: Ejecutar múltiples tareas concurrentemente
    print("1. Concurrencia con gather:")
    start_time = time.time()
    
    urls = [
        "https://api1.example.com",
        "https://api2.example.com", 
        "https://api3.example.com"
    ]
    
    # Ejecutar en paralelo
    results = await asyncio.gather(*[fetch_data(url, 0.5) for url in urls])
    
    elapsed = time.time() - start_time
    print(f"  Resultados: {len(results)} en {elapsed:.2f}s")
    for result in results:
        print(f"    - {result}")
    
    # Patrón 2: Pipeline asíncrono
    print("\n2. Pipeline asíncrono:")
    
    async def async_pipeline(items):
        """Pipeline de procesamiento asíncrono"""
        tasks = []
        for item in items:
            # Fetch -> Process pipeline
            data = await fetch_data(f"source-{item}", 0.3)
            processed = await process_data(data)
            tasks.append(processed)
        return tasks
    
    pipeline_results = await async_pipeline([1, 2, 3])
    for result in pipeline_results:
        print(f"    - {result}")
    
    # Patrón 3: Context manager asíncrono
    print("\n3. Context manager asíncrono:")
    
    class AsyncDatabase:
        async def __aenter__(self):
            print("    Conectando a la base de datos...")
            await asyncio.sleep(0.1)
            return self
        
        async def __aexit__(self, exc_type, exc_val, exc_tb):
            print("    Cerrando conexión a la base de datos...")
            await asyncio.sleep(0.1)
        
        async def query(self, sql):
            await asyncio.sleep(0.2)
            return f"Resultado de: {sql}"
    
    async with AsyncDatabase() as db:
        result = await db.query("SELECT * FROM users")
        print(f"    Query result: {result}")
    
    print("\nCaracterísticas de AsyncIO:")
    print("✅ Concurrencia sin threading")
    print("✅ Mejor para I/O-bound tasks")
    print("✅ Context managers asíncronos")
    print("✅ Iteradores asíncronos")
    print("✅ Ecosistema de bibliotecas async")
    print()

def demonstrate_dataclasses_evolution():
    """Demostrar la evolución de dataclasses"""
    print("=== Dataclasses - Evolución de Clases de Datos ===")
    
    # Antes de dataclasses
    class PersonOldStyle:
        def __init__(self, name, age, email=None):
            self.name = name
            self.age = age
            self.email = email
        
        def __repr__(self):
            return f"Person(name='{self.name}', age={self.age}, email='{self.email}')"
        
        def __eq__(self, other):
            if not isinstance(other, PersonOldStyle):
                return False
            return (self.name, self.age, self.email) == (other.name, other.age, other.email)
    
    # Con dataclasses
    @dataclass
    class PersonModern:
        name: str
        age: int
        email: Optional[str] = None
        
        def __post_init__(self):
            if self.age < 0:
                raise ValueError("Age cannot be negative")
    
    # Comparación
    print("Comparación de estilos:")
    
    old_person = PersonOldStyle("Alice", 30, "alice@example.com")
    modern_person = PersonModern("Alice", 30, "alice@example.com")
    
    print(f"Estilo antiguo: {old_person}")
    print(f"Estilo moderno: {modern_person}")
    
    print(f"Igualdad automática: {PersonModern('Bob', 25) == PersonModern('Bob', 25)}")
    
    # Características avanzadas
    @dataclass(frozen=True)  # Inmutable
    class Point:
        x: float
        y: float
        
        def distance_to_origin(self) -> float:
            return (self.x ** 2 + self.y ** 2) ** 0.5
    
    point = Point(3.0, 4.0)
    print(f"Punto inmutable: {point}")
    print(f"Distancia al origen: {point.distance_to_origin():.2f}")
    
    # Con field() para configuraciones avanzadas
    from dataclasses import field
    
    @dataclass
    class ShoppingCart:
        items: List[str] = field(default_factory=list)
        metadata: Dict[str, Any] = field(default_factory=dict)
        total: float = field(init=False, default=0.0)
        
        def add_item(self, item: str, price: float):
            self.items.append(item)
            self.total += price
    
    cart = ShoppingCart()
    cart.add_item("Libro", 25.99)
    cart.add_item("Café", 4.50)
    print(f"Carrito: {len(cart.items)} items, total: ${cart.total:.2f}")
    
    print("\nCaracterísticas de Dataclasses:")
    print("✅ Menos código boilerplate")
    print("✅ Type hints integrados")
    print("✅ __repr__, __eq__ automáticos")
    print("✅ Inmutabilidad opcional")
    print("✅ Configuración flexible con field()")
    print()

async def main():
    """Función principal asíncrona"""
    print("=== Innovaciones de la Comunidad Python ===")
    print("Bibliotecas que revolucionaron el ecosistema Python\n")
    
    demonstrate_fastapi_style()
    demonstrate_pydantic_style()
    demonstrate_rich_style()
    demonstrate_typer_style()
    
    # Ejecutar ejemplos asíncronos
    await demonstrate_asyncio_patterns()
    
    demonstrate_dataclasses_evolution()
    
    print("=== Otras Innovaciones Importantes ===")
    innovations = [
        ("Jupyter Notebooks", "Computación interactiva y reproducible"),
        ("NumPy/Pandas", "Revolución en data science"),
        ("Django/Flask", "Frameworks web que definieron estándares"),
        ("Requests", "HTTP for Humans - API simple y elegante"),
        ("SQLAlchemy", "ORM potente y flexible"),
        ("Celery", "Procesamiento asíncrono de tareas"),
        ("Poetry", "Gestión moderna de dependencias"),
        ("Black", "Formateo automático de código"),
        ("Pytest", "Testing moderno y fixtures"),
        ("Streamlit", "Web apps para data science sin HTML/CSS"),
    ]
    
    for name, description in innovations:
        print(f"🚀 {name:20} - {description}")
    
    print("\n=== Impacto en la Industria ===")
    impacts = [
        "Democratización de la ciencia de datos",
        "APIs modernas con documentación automática",
        "Desarrollo web rápido y escalable",
        "CLIs intuitivas con type hints",
        "Testing más fácil y mantenible",
        "Formateo consistente de código",
        "Gestión de dependencias moderna",
    ]
    
    for impact in impacts:
        print(f"✅ {impact}")

if __name__ == "__main__":
    asyncio.run(main())