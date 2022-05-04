class Base1(object):
	def __init__(self):
		self.str1 = "Python"
		print("Base1")
		
	def prueba2(self):
		print("prueba")

class Base2(object):
	def __init__(self):
		self.str2 = "Java"
		print("Base2")
		
	def prueba2(self):
		print("prueba2")

class Derived(Base1, Base2):
	def __init__(self):
		# Llamar a constructores de clases Base1 y Base2
		Base1.__init__(self)
		Base2.__init__(self)
		print("Derived")
		
	def printStrs(self):
		print(self.str1, self.str2) 


ob = Derived() 
ob.printStrs()
ob.prueba2()
