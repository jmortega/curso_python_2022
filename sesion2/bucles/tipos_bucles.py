# Inicialización de Variables
lista = [1,2,3,4,5,6,7,8,9,10]
rango = range(1,10)

for numero in rango:
    print(numero)

for elemento in lista:
	print(elemento)

while (len(lista) > 3):
    lista.pop()
    print(lista)


#do-while
i = 1  
while True:  
    print(i)  
    i = i + 1  
    if(i > 5):  
        break  

# Bucle WHILE INFINITO
'''
while True:
    suma+=1
    print(suma)
'''

