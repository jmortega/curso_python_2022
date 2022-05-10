from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/suma')
def suma():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@app.route('/')
def index():
    return render_template('suma.html')

if __name__ == '__main__':
    app.run()
