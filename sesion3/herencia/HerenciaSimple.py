class Persona(object):
	# Constructor
	def __init__(self, nombre):
		self.nombre = nombre
	def getNombre(self):
		return self.nombre
	def isEmpleado(self):
		return False

class Empleado(Persona):
	def isEmpleado(self):
		return True

persona = Persona("Mr.Jeff")  # Objeto persona
print(persona.getNombre(), persona.isEmpleado()) 
empleado = Empleado("Alan") # Objeto empleado
print(empleado.getNombre(), empleado.isEmpleado()) 
