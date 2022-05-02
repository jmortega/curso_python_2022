tupla = ('Java',2019,'Python',2020,'Python')
print("Elementos de la tupla: ",tupla)
print("Elemento de la posición 0: ",tupla[0])
print("Elemento de la posición 1: ",tupla[1])
print("Elemento de la posición 2: ",tupla[2])
print("Elemento de la posición 3: ",tupla[3])
print(tupla[1:3]) # Imprime los elementos en los índices 2 y 3
print(tupla[2:]) # Imprime la tupla a partir del 3er elemento
print("Número de elementos Python: ",tupla.count('Python'))
print("Posición que ocupa el elemento Python: ",tupla.index("Python"))

tupla2 = (1,2,3, "Videojuegos")
print("Tupla2: ", tupla2)
print("Número elementos de tupla2: ",len(tupla2))
tuplaconcatenada = tupla + tupla2
print("Número elementos de tuplaconcatenada: ",len(tuplaconcatenada))
print("tuplaconcatenada: ", tuplaconcatenada)
