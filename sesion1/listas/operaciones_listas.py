list = [ 'python', 1 ,'java', 2 ]
tinylist = ['JavaScript', 3]
print(list) # Imprime una lista
print(list[0]) # Imprime el primer elemento de la lista
print(list[1:3]) # Imprime los elementos en los índices 2 y 3
print(list[2:]) # Imprime la lista a partir del 3er elemento
print(tinylist * 2) # Imprimie una lista 2 veces
print(list + tinylist) # Concatena 2 listas

objeto = "PHP"
list.append(objeto) # Añadir un objeto a una lista
print(list)
print(list.count(objeto)) # Devuelve el número de veces que se encuentra un objeto en la lista
list.remove(objeto) # Elimina un objeto de una lista
print(list)
