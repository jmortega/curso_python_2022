#######################################
#       Fichero: Insert.py            #
#   Inserta en base de datos los      #
#     registros de las tablas         #
#######################################

# Importa la librería para utilizar SQLite
import sqlite3

# Conecta a la base de datos
database = sqlite3.connect('coches.db')

# Crea los registros de fabricantes
register1 = ('Honda3', '911234567', 'Calle Japón 3','hello@honda.es')
register2 = ('Seat3', '919876543', 'Calle España 1','info@seat.es')

# Apertuda de un cursor e inserción de los fabricantes
cursor = database.cursor()
cursor.execute("INSERT INTO Fabricante('Nombre','Telefono','Direccion','Email') VALUES(?,?,?,?)", register1)
cursor.execute("INSERT INTO Fabricante ('Nombre','Telefono','Direccion','Email') VALUES(?,?,?,?)", register2)

# Commit de las operaciones
database.commit()

# Crea los registros de los coches
register1 = (9, 1, 'Civic', 1600,'Azul')
register2 = (10, 1, 'HR-V', 2400,'Negro')
register3 = (11, 2, 'Ibiza', 1200,'Rojo')
register4 = (12, 2, 'Ateca', 1800,'Blanco')

# Inserción de los modelos de coches
cursor.execute("INSERT INTO Coche VALUES(?,?,?,?,?)", register1)
cursor.execute("INSERT INTO Coche VALUES(?,?,?,?,?)", register2)
cursor.execute("INSERT INTO Coche VALUES(?,?,?,?,?)", register3)
cursor.execute("INSERT INTO Coche VALUES(?,?,?,?,?)", register4)

# Commit de las operaciones
database.commit()

# Cierra la conexión a la base de datos    
database.close()
