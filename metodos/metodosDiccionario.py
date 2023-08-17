# Ejemplo de diccionario
persona = {
    "nombre": "Juan",
    "edad": 30,
    "profesion": "ingeniero"
}

# Método keys(): Devuelve una vista de las claves en el diccionario
claves = persona.keys()
print("Claves:", claves)  # Salida: Claves: dict_keys(['nombre', 'edad', 'profesion'])

# Método get(): Devuelve un valor asociado a la clave dada o un valor predeterminado si la clave no existe
edad = persona.get("edad", 0)
altura = persona.get("altura", 0)
print("Edad:", edad)      # Salida: Edad: 30
print("Altura:", altura)  # Salida: Altura: 0

# Método clear(): Elimina todos los pares clave-valor en el diccionario
persona.clear()
print("Persona después de clear:", persona)  # Salida: Persona después de clear: {}

# Restaurar valores al diccionario
persona["nombre"] = "Juan"
persona["edad"] = 30
persona["profesion"] = "ingeniero"

# Método pop(): Elimina y devuelve el valor asociado a la clave especificada
edad = persona.pop("edad")
print("Edad eliminada:", edad)         # Salida: Edad eliminada: 30
print("Diccionario después de pop:", persona)  # Salida: Diccionario después de pop: {'nombre': 'Juan', 'profesion': 'ingeniero'}

# Método items(): Devuelve una vista de los pares clave-valor en el diccionario como tuplas
pares = persona.items()
print("Pares clave-valor:", pares)    # Salida: Pares clave-valor: dict_items([('nombre', 'Juan'), ('profesion', 'ingeniero')])
