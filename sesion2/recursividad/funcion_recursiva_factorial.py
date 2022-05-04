#Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(numero):
	if numero == 0 or numero == 1:
		return 1
	else:
		return numero * factorial(numero-1)

print(factorial(4))
print(factorial(10))
