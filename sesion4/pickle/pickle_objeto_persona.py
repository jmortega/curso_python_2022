import pickle

class Persona:
    def __init__(self):
        self.nombre = None
        self.edad = None

def main():
 
    a = Persona()
    a.nombre = "Javier"
    a.edad = 21

    b = Persona()
    b.nombre = "Fernando"
    b.edad = 32

    fichero = open(r"personas.dat", "wb")
    pickle.dump(a, fichero)
    pickle.dump(b, fichero)
    fichero.close()

    fichero= open(r"personas.dat", "rb")
    print("Contenido del fichero:")
    for i in range(2):
        objeto = pickle.load(fichero)
        print("\nFicha número", i + 1, ":")
        print("Nombre: ", objeto.nombre)
        print("Edad: ", objeto.edad)
    fichero.close()

main()
