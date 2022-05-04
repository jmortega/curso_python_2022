'''Escribir un programa que pida al usuario un número entero  n  y muestre por pantalla un triángulo el de más abajo.

    *
   ***
  *****
 *******
*********

donde  n  es el número de filas del triángulo.'''

#solution1

# Preguntamos el número de filas del triángulo y lo convertimos en un entero
n = int(input('Introduce el número de filas del triángulo: '))
# Recorremos con un bucle cada fila del triángulo
for i in range(n):
    # Añadimos con un bucle el número de espacios de cada línea para que los asteriscos aparezcan centrados
    for j in range(n-i-1):
        print(' ', end='')
    # Añadimos con otro bucle el número de asteriscos de cada línea
    for j in range(2*i+1):
        print('*', end='')
    print()
	
#solution2

# Preguntamos el número de filas del triángulo y lo convertimos en un entero
n = int(input('Introduce el número de filas del triángulo: '))
# Recorremos con un bucle cada fila del triángulo
for i in range(n):
    # Añadimos el número de espacios de cada línea para que los asteriscos aparezcan centrados
    print(' '*(n-i-1), end='')
    # Añadimos el número de asteriscos de cada línea.
    print('*'*(2*i+1))