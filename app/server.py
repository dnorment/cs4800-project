from flask import Flask
from flask_restplus import Api, Resource, fields
import dialogflow
import os

#Build Flask app
project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
app = Flask(__name__)

#Set API config
api = Api(
    app=app,
    doc='/api',
    version='1.0.0',
    title='YeetBot API',
    description='Better than a psychiatrist (not really)'
)

#Use /api/ namespace for requests
ns = api.namespace(name='api')

#Model for the format of requests and responses to the API
message_model = api.model('Message', {
    'message': fields.String(description='The message to send'),
    'session_id': fields.String(description='The ID of the session to reply to, each user should have a unique session ID for each new conversation')
})
reply_model = api.model('Reply', {
    'message': fields.String(description='The reply message from YeetBot')
})

#Add endpoint to API for sending a message
@ns.route("/send_message/")
class SendMessage(Resource):
    @ns.expect(message_model) #Expect requests adhere to the message model
    @ns.marshal_with(reply_model)
    def post(self):
        """
        Returns a chat response from YeetBot
        """
        
        #Extract data from payload
        message = api.payload['message']
        session_id = api.payload['session_id']

        #Get current Dialogflow session
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(project_id, session_id)

        #Send query to Dialogflow
        text_input = dialogflow.types.TextInput(text=message, language_code="en")
        query_input = dialogflow.types.QueryInput(text=text_input)

        #Get response from Dialogflow and parse into custom response JSON
        result = session_client.detect_intent(session=session, query_input=query_input)
        response = {
            "message":  result.query_result.fulfillment_text
        }

        #Return reponse on success
        return response, 200
