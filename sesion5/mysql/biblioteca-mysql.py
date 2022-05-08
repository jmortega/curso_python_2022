#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
import sys
import pymysql

try:
    conector = pymysql.connect(host='remotemysql.com',
    port=3306,
    user='nrwvZekj7X',
    db='nrwvZekj7X',
    password='ZNhRlLhOl4',
    charset='utf8'
    )
    
    def listar(conector):
    	print("Listar libros:\n")
    	sql = "select * from biblioteca"
    	cur = conector.cursor()
    	cur.execute(sql)
    	filas = cur.fetchall()
    	for rows in filas:
    		print(rows)
    	menu()
    
    def agregar(conector):
        print("Insertar un nuevo libro:\n")
        isbn = input("Introduzca ISBN: ")
        titulo = input("Introduzca Título: ")
        anyo = int(input("Introduzca Año: "))
        autor = input("Introduzca Autor: ")   
              
        cur = conector.cursor()
        sql_insert = "insert into biblioteca (isbn,titulo,anyo,autor) values (%s,%s,%s,%s)"
        cur.execute(sql_insert,(isbn,titulo,int(anyo),autor))
        conector.commit()
        menu()
        
    def editar(conector):
        cur = conector.cursor()
        print("Editar un libro:\n")
        id = input("Introduzca el ID del libro: ")
        isbn = input("Introduzca ISBN: ")
        titulo = input("Introduzca Título: ")
        anyo = input("Introduzca Año: ")
        autor = input("Introduzca Autor: ")        
        
        #Reviso si existe o no el id a editar
        coincidencia = "select id from biblioteca where id = %s"
        existe = cur.execute(coincidencia,(id))
        if not existe:
            print("No existe ID para editar. Intente nuevamente")
        else:
            sql = "update biblioteca set isbn=%s,titulo=%s,anyo=%s,autor=%s where id = %s"
            cur.execute(sql,(isbn,titulo,int(anyo),autor,id))
            conector.commit()
            menu()
            
    def buscar(conector):
        print("Buscar un libro:\n")
        isbn = input("Introduzca ISBN a buscar: ")
        sql = "select * from biblioteca where isbn = %s"
        cur = conector.cursor()
        cur.execute(sql,(isbn))
        filas = cur.fetchall()
        for rows in filas:
            print(rows)
        menu()
        
    def borrar(conector):
        cur = conector.cursor()
        print("Borrar un libro:\n")
        #id = raw_input("Ingrese el ID del libro: ")
        id = input("Introduzca el ID del libro: ")
        coincidencia = "select id from biblioteca where id = %s"
        existe = cur.execute(coincidencia,(id))
        if not existe:
            print("No existe ID, no se puede eliminar")
        else:
            sql = "delete from biblioteca where id = %s"
            cur.execute(sql,(id))
            conector.commit()
        menu()
        
    def menu():
        print("""
        Bienvenido a la Biblioteca del Curso\t
        Escoja las opciones:\t
        """)
        #opciones = raw_input("""
        opciones = input("""
        (1) Listar libros\t
        (2) Añadir nuevo libro\t
        (3) Editar libro por ID\t
        (4) Borrar libro por ID\t
        (5) Buscar libro por ISBN\t
        (6) Salir del programa
        """)
        opciones = int(opciones)
        if opciones == 1:
            listar(conector)
        if opciones == 2:
            agregar(conector)
        elif opciones == 3:
            editar(conector)
        elif opciones == 4:
            borrar(conector)
        elif opciones == 5:
            buscar(conector)
        elif opciones == 6:
        	conector.close()
        	os.system("clear")
        else:
            menu()
    menu()

except Exception as e:
    sys.exit(e)
