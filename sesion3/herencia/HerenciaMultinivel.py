#clase base
class Padre(object):
	def __init__(self, nombre):
		self.nombre = nombre
	def getNombre(self):
		return self.nombre 

#Hijo hereda de padre
class Hijo(Padre):
	def __init__(self, nombre, edad):
		Padre.__init__(self, nombre)
		self.edad = edad
	def getEdad(self):
		return self.edad
		
#Nieto hereda de Hijo
class Nieto(Hijo):
	def __init__(self, nombre, edad, direccion):
		Hijo.__init__(self, nombre, edad)
		self.direccion = direccion
	def getDireccion(self):
		return self.direccion
	def getEdad(self):
		return "Mi edad es "+str(self.edad)	

padre = Padre("Padre")
hijo = Hijo("Hijo",30)
nieto = Nieto("Nombre", 30, "Spain") 
print(padre.getNombre(),hijo.getNombre(),hijo.getEdad(),nieto.getNombre(), nieto.getEdad(), nieto.getDireccion())
