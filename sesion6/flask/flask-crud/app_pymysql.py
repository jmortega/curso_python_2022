from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)
app.secret_key = 'secret_key'

app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'nrwvZekj7X'
app.config['MYSQL_PASSWORD'] = 'ZNhRlLhOl4'
app.config['MYSQL_DB'] = 'nrwvZekj7X'

def obtener_conexion():
	return pymysql.connect(host=app.config['MYSQL_HOST'],
	user=app.config['MYSQL_USER'],
	password=app.config['MYSQL_PASSWORD'],
	db=app.config['MYSQL_DB'])
                                
@app.route('/')
def index():
	conexion = obtener_conexion()
	with conexion.cursor() as cursor:
		cursor.execute("SELECT  * FROM estudiantes")
		data = cursor.fetchall()
	conexion.close()
	return render_template('index.html', students=data )

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST": 
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
        	cursor.execute("INSERT INTO estudiantes (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        conexion.commit()
        conexion.close()
        flash("Registro insertado correctamente")
        return redirect(url_for('index'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
    	cursor.execute("DELETE FROM estudiantes WHERE id=%s", (id_data,))
    conexion.commit()
    conexion.close()
    flash("Registro eliminado correctamente")
    return redirect(url_for('index'))

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
        	cursor.execute("""UPDATE estudiantes SET name=%s, email=%s, phone=%s WHERE id=%s""", (name, email, phone, id_data))
        flash("Registro actualizado correctamente")
        conexion.commit()
        conexion.close()
        return redirect(url_for('index'))
        
        
if __name__ == "__main__":
    app.run(debug=True)
