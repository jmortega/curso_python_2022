class MiExcepcion(Exception):
	def __init__(self, valor):
		self.valor = valor
		
	def __str__(self):
		return "Error " + str(self.valor)

resultado =25
try:
	if resultado > 20:
		raise MiExcepcion(33)
except MiExcepcion as excepcion:
	print(excepcion)
