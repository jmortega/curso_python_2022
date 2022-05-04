# Escribe una función que convierta un número en binario
#  y otra que convierta un número binario en entero.

numero = 5
numero_binario = 0b101

def decimal_a_binario(decimal: float):
    return bin(decimal)
    
def binario_a_decimal(binario):
    return int(binario)

print(f'El número {numero} en binario sería: {decimal_a_binario(numero)}')

print(f'El número binario {str(numero_binario)} es el número: {binario_a_decimal(numero_binario)}')


