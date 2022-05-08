ºimport sqlite3


def crear_tablas(con):
    cur = con.cursor()

    try:
        cur.execute('DROP TABLE perfiles')
        cur.execute('DROP TABLE usuarios')
        cur.execute('DROP TABLE posts')
    except Exception:
        print('No data on the database')

    cur.execute('''CREATE TABLE perfiles (id INTEGER PRIMARY KEY, 
                                          nombre_perfil TEXT, 
                                          puede_editar TEXT)''')

    cur.execute('''CREATE TABLE usuarios (id INTEGER PRIMARY KEY, 
                                          nombre TEXT, 
                                          apellido TEXT, 
                                          f_nacimiento TEXT, 
                                          perfil_id INTEGER,
                                          FOREIGN KEY (perfil_id) REFERENCES perfiles(id)
                                          )''')

    cur.execute('''CREATE TABLE posts (id INTEGER PRIMARY KEY, 
                                       autor_id INTEGER,
                                       texto TEXT,
                                       fecha TEXT,
                                       likes INTEGER,
                                       FOREIGN KEY (autor_id) REFERENCES usuarios(id)
                                       )''')


def insertar_datos(con):
    cur = con.cursor()

    cur.executescript('''
        DELETE FROM usuarios;
        DELETE FROM perfiles;
        DELETE FROM posts;
''')
    cur.execute('''INSERT INTO perfiles (nombre_perfil, puede_editar) 
                    values ('Admin', 'Y'),
                           ('Visitante', 'N'),
                           ('Editor', 'Y')''')

    cur.executescript('''INSERT INTO usuarios (nombre, apellido, f_nacimiento, perfil_id) 
                          values ('Paco', 'Lopez', '1998-08-03', 3),
                                 ('Maria', 'Gomez', '2000-10-28', 1),
                                 ('Antonio', 'Lopez', '1990-02-21', 3);
                                 
                          INSERT INTO posts (autor_id,  texto, fecha, likes)
                          values (1, 'Mi primera entrada', '2022-01-28', 4),
                                 (1, 'Mi segunda entrada', '2022-02-09', 1),
                                 (2, '¿Como hacer ejercicio?', '2021-09-08', 40),
                                 (3, 'Dietas saludables', '2021-07-19', 15);
                               ''')
    con.commit()


if __name__ == '__main__':
    connection = sqlite3.connect('ejemplo_sqlite.db')

    crear_tablas(connection)
    insertar_datos(connection)

    connection.row_factory = sqlite3.Row
    cur = connection.cursor()
    cur.execute("SELECT * from usuarios")
    usuarios = cur.fetchall()
    info = '\n'.join(' - '.join(map(str, r)) for r in usuarios)
    print(f'{info}')
    
    cur = connection.cursor()
    cur.execute(
        "SELECT p.texto, p.likes, u.nombre, u.apellido from usuarios u, posts p WHERE p.autor_id = u.id and p.likes > 1 order by p.likes")
    rows = cur.fetchall()
    info = '\n'.join(' - '.join(map(str, r)) for r in rows)
    print(f'Post con autores:\n{info}')

    cur = connection.cursor()
    cur.execute("SELECT u.nombre, p.likes from usuarios u, posts p WHERE p.autor_id = u.id group by u.nombre")
    rows = cur.fetchall()
    info = '\n'.join(f'{r[0]}->{r[1]}' for r in rows)
    print(f"Autores y likes:\n{info}")

