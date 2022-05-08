from functools import reduce

def sumar(x, y):
    return x + y

lista = [1, 2, 3]
suma = reduce(sumar, lista)
print(suma)

