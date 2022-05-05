#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Curso(object):

    def __init__(self,nombre):
    	self.nombre = nombre

    def __str__(self) -> str:
    	str_curso = "El curso {} se imparte en modalidad online".format(self.nombre)
    	return str_curso

    def __repr__(self) -> str:
    	representacion_interpretable = '{self.__class__.__name__}({self.nombre})'.format(self=self)
    	return representacion_interpretable


if __name__ == "__main__":
    curso = Curso("Python")
    representacion_str = str(curso)
    representacion_repr = repr(curso)
    print(representacion_str)
    print(representacion_repr)

