#Obtener el cuadrado de todos los elementos en la lista.

def cuadrado(elemento=0):
    return elemento * elemento

lista = [1,2,3,4,5,6,7,8,9,10]
resultado = list(map(cuadrado,lista))
print(resultado)
resultado = list(map(lambda elemento:elemento*elemento,lista))
print(resultado)

