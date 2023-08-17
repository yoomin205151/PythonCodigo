
# Agrega un elemento al final de la lista
lista.append(elemento)

# Inserta un elemento en la posición especificada
lista.insert(indice, elemento)

# Extiende la lista agregando los elementos de otro iterable (lista, tupla, etc.)
lista.extend(iterable)

# Elimina el primer elemento con el valor especificado
lista.remove(valor)

# Elimina el elemento en la posición especificada
lista.pop(indice)

# Devuelve el índice de la primera aparición del valor especificado
indice = lista.index(valor)

# Cuenta cuántas veces aparece un valor en la lista
cantidad = lista.count(valor)

# Ordena la lista en su lugar (sin crear una nueva lista)
lista.sort()

# Ordena la lista en su lugar en orden descendente
lista.sort(reverse=True)

# Devuelve una copia ordenada de la lista original
lista_ordenada = sorted(lista)

# Invierte el orden de los elementos en la lista
lista.reverse()

# Copia la lista
copia_lista = lista.copy()

# Elimina todos los elementos de la lista
lista.clear()

# Devuelve el índice del primer elemento con el valor especificado en el rango dado
indice = lista.index(valor, inicio, fin)

# Devuelve la suma de todos los elementos en la lista
suma = sum(lista)

# Devuelve el valor máximo de la lista
maximo = max(lista)

# Devuelve el valor mínimo de la lista
minimo = min(lista)

# Devuelve la longitud (cantidad de elementos) de la lista
longitud = len(lista)

# Devuelve una lista que contiene elementos únicos en el mismo orden que aparecen en la lista original
lista_sin_duplicados = list(set(lista))

# Devuelve una cadena que representa la lista
cadena_lista = str(lista)
