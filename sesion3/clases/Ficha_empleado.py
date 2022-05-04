class Ficha_empleado:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.antigüedad = None
        self.cualificación = None
    def Sueldo(self):
        return(1000 + self.antigüedad * 25 + self.cualificación * 100)

def main():
    a = Ficha_empleado()
    a.nombre = "Javier"
    a.edad = 21
    a.antigüedad = 2
    a.cualificación = 1

    b = Ficha_empleado()
    b.nombre = "Fernando"
    b.edad = 32
    b.antigüedad = 9
    b.cualificación = 4

    print("El sueldo de ", a.nombre, ",con ", a.antigüedad, \
    " años en la empresa y con cualificación de grado ", a.cualificación, \
    " es de ", a.Sueldo()," euros", sep='')

    print("El sueldo de ", b.nombre, ",con ", b.antigüedad, \
    " años en la empresa y con cualificación de grado ", b.cualificación, \
    " es de ", b.Sueldo()," euros", sep='')

main()
