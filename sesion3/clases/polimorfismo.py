class python():
	
	variable_clase ="python"
	
	def __init__(self,variable):
		self.variable = variable
		print("init",self.variable)
		
	def welcome(self):
		print("Python")
	
	@staticmethod
	def metodo_estatico(variable):
		return "metodo estatico",variable
	
	@classmethod
	def metodo_clase(clase):
		return "metodo de clase",clase
	
class java():
	def welcome(self):
		print("Java")	

def lenguajeFavorito(lenguaje):
	lenguaje.welcome()	

if __name__ == '__main__':
	p = python("python")
	print(p.variable_clase)
	print(p.metodo_estatico("variable"))
	print(p.metodo_clase())
	j = java()
	lenguajeFavorito(p)
	lenguajeFavorito(j)
