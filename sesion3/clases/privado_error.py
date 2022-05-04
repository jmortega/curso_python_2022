class Ejemplo: 
    def publico(self): 
        print("Publico")
 
    def __privado(self): 
        print("Privado")

ej = Ejemplo()
ej.publico()
ej.__privado() #error

