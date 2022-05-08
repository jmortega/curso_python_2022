from math import pow

numeros = [2, 3, 4, 1]
potencias = [3, 2, 4,1]

resultados = list(map(pow, numeros, potencias))
print(resultados)
