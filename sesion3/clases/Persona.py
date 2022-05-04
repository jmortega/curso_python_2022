class Persona:
    def __init__ (self, nombre, apellidos, edad):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Edad = edad
        
    def MostrarPersona(self):
        print("Nombre: " + self.Nombre)
        print("Apellidos: " + self.Apellidos)
        print("Edad: " + str(self.Edad))
        
    def __str__(self):
        return self.Nombre + " "+ self.Apellidos

print("OBJETOS ORIGINALES")
p1 = Persona("Antonio","Perez", 20)
p1.MostrarPersona()
p2 = Persona("Valeria","Moreno", 30)
p2.MostrarPersona()

#modificar objetos p1 y p2
p1.Edad = 36
p2.Apellidos = "Moreno Martinez"

print("OBJETOS MODIFICADOS")
p1.MostrarPersona()
p2.MostrarPersona()

#asignar p2 a p1,ahora son la misma persona	
#p1=p2
print("OBJETOS TRAS ASIGNACIÓN")
p1.MostrarPersona()
p2.MostrarPersona()

print("probar metodo str")
print(p1)
print(p2)

