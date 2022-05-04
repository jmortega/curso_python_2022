import math
class Punto():
	""" Representación de un punto en el plano, los atributos son x e y
	que representan los valores de las coordenadas cartesianas."""

	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	
	
	def distancia(self, punto):
		""" Devuelve la distancia entre ambos puntos. """
		dx = self.x - punto.x
		dy = self.y - punto.y
		return math.sqrt((dx*dx + dy*dy))
	
	@staticmethod
	def mostrar_punto(punto):
		return punto.x,punto.y
		
	@classmethod
	def metodo_clase(cls,punto):
		return punto.x,punto.y

if __name__ == '__main__':
	
	punto1=Punto()
	punto2=Punto(4,5)
	print(punto1.distancia(punto2))
	print(Punto().mostrar_punto(punto2))
	print(Punto().metodo_clase(punto2))
	print(punto1.__dict__)
	print(punto2.__dict__)
