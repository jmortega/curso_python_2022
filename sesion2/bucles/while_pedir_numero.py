pedirnumero = True
while pedirnumero:
    valor = int(input("Introduce un entero inferior a 10: "))
    if valor<10:
        pedirnumero = False
print("FIN: ¡Ha introducido un valor inferior a 10!")
