numero = 1
numero2 = 2


if numero == 1:
    numero2 = 4
    # Código a ejecutar si la condición es verdadera


#----------------------------------------------------------------

if numero == 1:
    numero2 = 4
    # Código a ejecutar si la condición es verdadera
else:
    numero2 = 9
    # Código a ejecutar si la condición es falsa

#----------------------------------------------------------------
if numero == 1:
    numero2 = 4
    # Código a ejecutar si la condición1 es verdadera
elif numero == 12:
    numero2 = 9
    # Código a ejecutar si la condición2 es verdadera
else:
    numero2 = 10
    # Código a ejecutar si ninguna de las condiciones anteriores es verdadera

#----------------------------------------------------------------------

#resultado = valor_si_verdadero if condicion else valor_si_falso
edad = 18
puede_votar = True if edad >= 18 else False
