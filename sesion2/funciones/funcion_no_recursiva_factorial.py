#Escribir una función que reciba un número entero positivo 
#y devuelva su factorial.

def factorial(n):
    """Función que calcula el factorial de un número entero positivo.
    Parámetros
    n: Es un entero positivo.
    Devuelve el factorial de n.
    """
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp

print(factorial(4))
print(factorial(10))
