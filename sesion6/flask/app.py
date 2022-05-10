import time
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
        
@app.route('/dinamico')
@app.route('/dinamico/<parametro>')
def dinamico(parametro=None):
    fecha = time.strftime("%d/%m/%y")
    return render_template('dinamico.html',parametro=parametro,fecha=fecha)
    
    
if __name__ == '__main__':
	app.run('0.0.0.0',5000, debug=True)
