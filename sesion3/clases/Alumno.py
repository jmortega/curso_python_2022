class Alumno: 
     
    def __init__(self):
        self.datos_alumno = { 
            "nombre":"", 
            "email":"" 
        } 
     
    def __str__(self): 
        return self.datos_alumno["nombre"] + " " + self.datos_alumno["email"]

alumno = Alumno() 
 
alumno.datos_alumno["nombre"] = "Nombre alumno" 
alumno.datos_alumno["email"] = "email"
print(alumno)
