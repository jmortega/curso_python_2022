def tablas(funcion):
    def envoltura(tabla=1):
        print('Tabla del %i:' %tabla)
        print('-' * 15)
        for numero in range(0, 11):            
            funcion(numero, tabla)
        print('-' * 15)
    return envoltura


@tablas
def multiplicar(numero, tabla=1):
    print('%2i X %2i = %3i' %(tabla, numero, tabla*numero))

# Muestra la tabla de multiplicar del 1
multiplicar()

# Muestra la tabla de multiplicar del 10
multiplicar(10) 
