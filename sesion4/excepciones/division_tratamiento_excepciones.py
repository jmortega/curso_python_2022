'''El manejo de errores en Python se puede hacer usando el bloque try / except. 
añadir una instrucción else a este bloque puede ser útil. Se ejecuta cuando no se produce ninguna excepción en el bloque try. 
Si necesita ejecutar algo independientemente de la excepción, utilizar el bloque finally.'''

a, b = 1,0

try:
    print(a/b)
    # exception raised when b is 0
except ZeroDivisionError:
    print("division by zero")
else:
    print("no exceptions raised")
finally:
    print("Run this always")
