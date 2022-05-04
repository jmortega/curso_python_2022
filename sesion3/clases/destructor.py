class Empleado: 
    def __init__(self,nombre):
        self.nombre = nombre
        print('Empleado creado.')
    
    def getNombre(self):
        return self.nombre
  
    # Deleting (Calling destructor) 
    def __del__(self):
        print('Destructor llamado, Empleado eliminado.') 
  
obj = Empleado("empleado") 
del obj

print(obj.getNombre())


