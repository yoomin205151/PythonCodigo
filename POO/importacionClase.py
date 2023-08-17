# Importar la clase Perro del archivo perro.py
from claseObjeto import Perro
# Crear objetos de la clase Perro
perro1 = Perro("Rex", 3)
perro2 = Perro("Luna", 2)

# Acceder a los métodos y atributos de los objetos
perro1.ladrar()
print(f"{perro2.nombre} tiene {perro2.edad} años")
