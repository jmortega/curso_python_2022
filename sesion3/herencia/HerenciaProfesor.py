class Persona:
    def __init__ (self):
        self.__Nombre = "" 
        self.__Apellidos = ""
        self.__Edad = 0
    def GetNombre(self):
        return self.__Nombre
    def SetNombre(self,nombre):
        self.__Nombre = nombre
    def GetApellidos(self):
        return self.__Apellidos
    def SetApellidos(self,apellidos):
        self.__Apellidos = apellidos       
    def GetEdad(self):
        return self.__Edad
    def SetEdad(self,edad):
        self.__Edad = edad

class Profesor(Persona):
    def __init__ (self):
        self.__Antigüedad = ""
        self.__Tutorias = ""
        self.__Telefono = ""
    def GetAntiguedad(self):
        return self.__Antigüedad
    def SetAntiguedad(self,antigüedad):
        self.__Antigüedad = antigüedad
    def GetTutorias(self):
        return self.__Tutorias
    def SetTutorias(self,tutorias):
        self.__Tutorias = tutorias
    def GetTelefono(self):
        return self.__Telefono
    def SetTelefono(self,telefono):
        self.__Telefono = telefono

class Investigador(Persona):
    def __init__ (self):
        self.__Especialidad = "" 
        self.__Años = ""
    def GetEspecialidad(self):
        return self.__Especialidad
    def SetEspecialidad(self,especialidad):
        self.__Especialidad = especialidad       
    def GetAños(self):
        return self.__Años
    def SetAños(self,años):
        self.__Años = años

class ProfesorUniversitario(Profesor,Investigador):
    def __init__ (self):
        self.__Universidad = ""
        self.__Departamento = ""
    def GetUniversidad(self):
        return self.__Universidad
    def SetUniversidad(self,universidad):
        self.__Universidad = universidad       
    def GetDepartamento(self):
        return self.__Departamento
    def SetDepartamento(self,departamento):
        self.__Departamento = departamento
    def MostrarProfesorUniversitario(self):
        print("Profesor Universitario:")
        print("\tNombre:",self.GetNombre())
        print("\tApellidos:",self.GetApellidos())
        print("\tEdad:",self.GetEdad())
        print("\tAntigüedad:",self.GetAntiguedad())
        print("\tTutorias:",self.GetTutorias())
        print("\tTelefono:",self.GetTelefono())
        print("\tEspecialidad:",self.GetEspecialidad())
        print("\tAños::",self.GetAños())
        print("\tUniversidad:",self.GetUniversidad())
        print("\tDepartamento:",self.GetDepartamento())

profesor = ProfesorUniversitario()
profesor.SetNombre("Alfredo")
profesor.SetApellidos("Moreno Muñoz")
profesor.SetEdad(35)
profesor.SetAntiguedad(15)
profesor.SetTutorias([["Lunes","16-18"],["Jueves","12-14"],["Viernes","11-13"]])
profesor.SetTelefono("654321098")
profesor.SetEspecialidad("Desarrollo de Software")
profesor.SetAños(15)
profesor.SetUniversidad("Universidad de Extremadura")
profesor.SetDepartamento("Lenguajes y Sistemas informáticos")
profesor.MostrarProfesorUniversitario()
