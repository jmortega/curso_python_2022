def mi_decorador(funcion):
    def nueva(*args):
        print("Llamada a la funcion", funcion.__name__)
        retorno = funcion(*args)
        return retorno
    return nueva

@mi_decorador
def imprimir(cadena):
    print(cadena)

#De esta forma cada vez que se llame a imprimir se estará 
#llamando realmente a la versión decorada.
imprimir("hola")
