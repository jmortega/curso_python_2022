lista1 = [0,0,0,1,0,0,0,0]
print(any(lista1))
#True

lista2 = [0,0,0,0.0,0,0,0.0,0]
print(any(lista2))
#False

lista3 = [True, False, False]
print(any(lista3))
#True

lista4 = ["","","not empty"]

print(any(lista4))
#True

lista5 = ["","",""]
print(any(lista5))
#False




