class Perro:
    def __init__(self, nombre, edad): # __init__ es un método especial (también conocido como "constructor") en Python que 
        self.nombre = nombre            # se llama automáticamente cuando se crea una instancia de una clase. Su función principal es inicializar los atributos del objeto.
        self.edad = edad

    def ladrar(self):
        print(f"{self.nombre} está ladrando")

#-----------------------------------------------
#setter y getter
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property               #metodo getter
    def nombre(self):  
        return self._nombre

    @nombre.setter     #metodo setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

# Crear un objeto de la clase Persona
persona = Persona("Juan")

# Acceder y modificar el atributo "nombre" a través de la propiedad
print(persona.nombre)  # Acceso
persona.nombre = "Pedro"  # Modificación


#---------------------------------------------
#ejemplo toString

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona: {self.nombre}, Edad: {self.edad}"

# Crear un objeto de la clase Persona
persona = Persona("Juan", 30)

# Imprimir el objeto o convertirlo a una cadena utilizando str()
print(persona)  # Salida: Persona: Juan, Edad: 30

