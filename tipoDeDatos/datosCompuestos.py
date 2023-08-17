#Array
lista = ["Alejadnro", "ko" , True, 1.80]
lista[0] = "Francisco" # el array se puede modificar los datos
print(lista[0])

#Tuplas
tupla = ("Alejadnro", "ko" , True, 1.80)
tupla[0] # las tuplas no se pueden modificar

#Conjunto (set)
conjunto = {"Alejadnro", "ko" , True, 1.80} 
#print(conjunto[1])  no se puede mostrar por indice
                #, no se pueden moficar
                #, no puede haber datos repetidos
                # solo se puede recorrer los datos atra vez de un bucle

#Creacion de Diccionario
diccionario = {
    'nombre': "alejandro",
    'apellido': "ko"
}
print(diccionario['nombre']) #funciona como una lista pero se recorre por el nombre de la caracteristica