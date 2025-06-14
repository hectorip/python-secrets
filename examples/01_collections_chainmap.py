"""
Ejemplo de collections.ChainMap
Combina múltiples diccionarios en una sola vista
"""

from collections import ChainMap

# Configuración por defecto
defaults = {
    'debug': False,
    'port': 8000,
    'host': 'localhost',
    'timeout': 30
}

# Configuración del usuario
user_config = {
    'debug': True,
    'port': 3000
}

# Configuración de línea de comandos
cli_config = {
    'port': 5000
}

# Combinar configuraciones (prioridad: CLI > User > Defaults)
config = ChainMap(cli_config, user_config, defaults)

print("Configuración final:")
for key, value in config.items():
    print(f"  {key}: {value}")

print(f"\nPuerto usado: {config['port']}")  # 5000 (de CLI)
print(f"Debug activado: {config['debug']}")  # True (de user)
print(f"Host: {config['host']}")  # localhost (de defaults)

# Modificar valores
config['new_setting'] = 'valor'
print(f"\nNueva configuración: {config['new_setting']}")

# Ver qué diccionario contiene cada valor
print(f"\nOrigen del puerto: {config.maps}")