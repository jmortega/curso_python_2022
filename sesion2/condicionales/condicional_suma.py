sumando1 = int(input("Escriba el primer sumando: "))
sumando2 = int(input("Escriba el segundo sumando: "))
resultado = sumando1 + sumando2
print("El resultado de la suma es: " + str(resultado))
if resultado%2==0:
    if resultado>=1000:
        print("¡El resultado de la suma es par y mayor o igual que 1000!")
    else:
        print("¡El resultado de la suma es par y menor que 1000!")
else:
    if resultado>=1000:
        print("¡El resultado de la suma es impar y mayor o igual que 1000!")
    else:
        print("¡El resultado de la suma es impar y menor que 1000!")
