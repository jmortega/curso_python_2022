# Define decorador
def decorador(funcion):
    # Define función decorada
    def funciondecorada(*param1, **param2):
        print('Inicio', funcion.__name__)
        funcion(*param1, **param2)
        print('Fin', funcion.__name__)
    return funciondecorada
    
def suma(a, b):
    print(a + b)

@decorador
def producto(arg1, arg2):
    print(arg1 * arg2)
    
suma = decorador(suma)
suma(2,2)
producto(2,2)
