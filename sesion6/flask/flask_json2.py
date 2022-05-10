from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class returnjson(Resource):
	def get(self):
		data={
			"name" : "Curso python",
            "year" : 2022,
		}
		return data

api.add_resource(returnjson,'/returnjson')


if __name__=='__main__':
	app.run(debug=True)

