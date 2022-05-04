suma = lambda val1=0, val2=0: val1 + val2
resta = lambda val1=0, val2=0: val1 - val2
operacion = lambda operacion, val1=0, val2=0 : operacion(val1, val2)

resultado_suma = operacion(suma, 10, 20)
resultado_resta = operacion(resta, 20, 10)

print(resultado_suma)
print(resultado_resta)
