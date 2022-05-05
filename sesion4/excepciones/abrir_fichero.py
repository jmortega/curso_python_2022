# -*- coding: utf-8 -*-

import sys

def abrirFichero(fichero = "fichero.txt"):
	try:
		fd = open(fichero)
		line = fd.readline()
		parsedInt = int(line.strip())
	except IOError as e:
		print("I/O error({0}): {1}".format(e.errno, e.strerror))
		raise
	except:
		print("Error inesperado, lanzando excepción:", sys.exc_info()[0])
		raise
	finally:
		print("Finally ejecutado")

try:
	abrirFichero("fichero.txt")
except Exception as exception: 
	print(exception)        
