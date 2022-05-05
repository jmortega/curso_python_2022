#con caracteres especiales(\n\t)
cadena1 = input("Introduzca la primera cadena:")
cadena2 = input('Introduzca la segunda cadena:')
cadena3 = input('Introduzca la tercera cadena:')
cadenaconsaltos = "\n\t" + cadena1 + "\n\t" + cadena2 + '\n\t' + cadena3
print("Cadena con saltos:",cadenaconsaltos)

#formateo de cadenas en el print
multiplicando = int(input("Multiplicando:"))
multiplicador = int(input("Multiplicador:"))
print("El resultado de multiplicar %d por %d es %d"  % (multiplicando, multiplicador, multiplicando*multiplicador))

multiplicando = int(input("Multiplicando:"))
multiplicador = int(input("Multiplicador:"))
print("El resultado de multiplicar {0} por {1} es {2}".format(multiplicando, multiplicador, multiplicando*multiplicador))

