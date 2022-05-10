from flask import Flask,jsonify,request
  
app =   Flask(__name__)
  
@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "name" : "Curso python",
            "year" : 2022,
        }
  
        return jsonify(data)
  
if __name__=='__main__':
    app.run(debug=True)
