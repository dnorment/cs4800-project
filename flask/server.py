from flask import Flask, request
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

class YeetBot(Resource):
    def get(self):
        return {'yeet': 'yeet'}
    
    def post(self):
        json = request.get_json()
        #TODO validate json
        message = json['inputText']
        clientid = json['clientId']
        r = requests.post('https://runtime.lex.us-west-2.amazonaws.com/bot/PsychBot/alias/PsychBot/user/'+clientid+'/text', data=message)
        return {'you get': r.text}, 200


api.add_resource(YeetBot, '/')

if __name__ == "__main__":
    app.run(debug=True)