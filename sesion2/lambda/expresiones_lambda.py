def f_principal(n):
    return lambda x: x * n


multi_5 = f_principal(5)
print(f'Funcion parcial multi_5(10): {multi_5(10)}')

#Función Lambda
suma = lambda x, y : x + y 
print(suma(2, 3)) # Salida: 5


