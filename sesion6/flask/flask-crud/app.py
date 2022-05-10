from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'secret_key'

app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'nrwvZekj7X'
app.config['MYSQL_PASSWORD'] = 'ZNhRlLhOl4'
app.config['MYSQL_DB'] = 'nrwvZekj7X'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM estudiantes")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', students=data )

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Registro insertado correctamente")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO estudiantes (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('index'))

@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Registro eliminado correctamente")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM estudiantes WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))

@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE estudiantes
               SET name=%s, email=%s, phone=%s
               WHERE id=%s
            """, (name, email, phone, id_data))
        flash("Registro actualizado correctamente")
        mysql.connection.commit()
        return redirect(url_for('index'))
if __name__ == "__main__":
    app.run(debug=True)
