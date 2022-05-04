def Potencia(base,exponente):
    if exponente <= 0:
        return 1
    else:
        return base * Potencia(base,exponente-1)

base = int(input("Introduzca la base de la potencia: "))
exponente = int(input("Introduzca el exponente de la potencia: "))
print("El valor de " + str(base) + " elevado a " + str(exponente) + " es: " + str(Potencia(base,exponente)))
