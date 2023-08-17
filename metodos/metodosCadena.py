# Convierte la cadena a mayúsculas
# Ejemplo: "Hola Mundo" -> "HOLA MUNDO"
str.upper()

# Convierte la cadena a minúsculas
# Ejemplo: "Hola Mundo" -> "hola mundo"
str.lower()

# Convierte el primer carácter de la cadena a mayúscula y el resto a minúsculas
# Ejemplo: "hOLA MUNDO" -> "Hola mundo"
str.capitalize()

# Convierte cada palabra en la cadena a mayúscula
# Ejemplo: "hola mundo" -> "Hola Mundo"
str.title()

# Elimina los espacios en blanco al principio y al final de la cadena
str.strip()

# Elimina los espacios en blanco al principio de la cadena
str.lstrip()

# Elimina los espacios en blanco al final de la cadena
str.rstrip()

# Reemplaza todas las ocurrencias de "old" con "new" en la cadena
# Ejemplo: "Hello, world!" -> "Hi, world!"
str.replace(old, new)

# Verifica si la cadena comienza con el prefijo especificado
# Ejemplo: "Hello, world!" -> True
str.startswith(prefix)

# Verifica si la cadena termina con el sufijo especificado
# Ejemplo: "Hello, world!" -> False
str.endswith(suffix)

# Divide la cadena en una lista de subcadenas utilizando el separador especificado
# Ejemplo: "apple,banana,orange" -> ['apple', 'banana', 'orange']
str.split(separator)

# Une una lista de cadenas en una cadena usando la cadena actual como separador
# Ejemplo: ['apple', 'banana', 'orange'] -> "apple,banana,orange"
str.join(iterable)

# Devuelve el índice de la primera ocurrencia de la subcadena o -1 si no se encuentra
# Ejemplo: "apple" -> 0
str.find(substring)

# Cuenta cuántas veces aparece la subcadena en la cadena
# Ejemplo: "apple apple" -> 2
str.count(substring)

# Verifica si la cadena contiene solo letras
str.isalpha()

# Verifica si la cadena contiene solo dígitos numéricos
str.isdigit()

# Verifica si la cadena contiene solo letras y números
str.isalnum()

# Verifica si todos los caracteres de la cadena están en minúsculas
str.islower()

# Verifica si todos los caracteres de la cadena están en mayúsculas
str.isupper()
