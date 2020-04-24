from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class YeetBot(Resource):
    def get(self):
        return {'yeet': 'yeet'}

api.add_resource(YeetBot, '/')

if __name__ == "__main__":
    app.run(debug=True)