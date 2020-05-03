from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import dialogflow
import os

#Build Flask app
app = Flask(__name__)

#Setup Swagger URI & config
swagger_url = '/api/docs'
api_url = '/static/swagger.json'
swagger_cfg = {
    "app_name": "YeetBot"
}
blueprint = get_swaggerui_blueprint(swagger_url, api_url, config=swagger_cfg)
app.register_blueprint(blueprint, url_prefix=swagger_url)

#Home page
@app.route('/')
def home():
    return ''

#Webhook endpoint for detecting response in certain intents
@app.route('/webhook', methods=['POST'])
def webhook():
    reply = {
        "fulfillmentText": request.get_json(silent=True)['queryResult']['queryText'],
    }
    return jsonify(reply)

#Endpoint for sending message to pass through Dialogflow, returns reply from bot
@app.route('/api/send_message', methods=['POST'])
def send_message():
    message = request.get_json(silent=True)['message']
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, "unique")

    if message:
        text_input = dialogflow.types.TextInput(text=message, language_code="en")
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)

    response_text = { "message":  response.query_result.fulfillment_text }
    return jsonify(response_text)

if __name__ == "__main__":
    app.run(debug=True)