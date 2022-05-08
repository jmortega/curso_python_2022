tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
lista = [5,2,6,7,8,10,77,55,2,1,30,4,2,3]

def numero_par(elemento):
    return elemento % 2 == 0

resultado = tuple(filter( numero_par, lista))
print(resultado)

resultado = list(filter( lambda elemento: elemento % 2==0, tupla))
print(resultado)
