
print("Sumaremos los intervalos de \
enteros indicados (ambos incluidos) \
hasta que se introduzcan dos ceros")

suma_total = 0
principio = eval(input("Inicio: "))
fin = eval(input("Fin: "))

while principio !=0 and fin != 0:
    suma_parcial = 0
    for i in range(principio, fin + 1):
        suma_parcial = suma_parcial + i
    suma_total = suma_total + suma_parcial
    principio = eval(input("Inicio: "))
    fin = eval(input("Fin: "))

print("La suma total es: ", suma_total)
