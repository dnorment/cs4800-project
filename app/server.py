from flask import Flask, request, jsonify
import dialogflow
import os

app = Flask(__name__)

@app.route('/')
def home():
    return ''

@app.route('/webhook', methods=['POST'])
def webhook():
    reply = {
        "fulfillmentText": request.get_json(silent=True)['queryResult']['queryText'],
    }
    return jsonify(reply)

@app.route('/send_message', methods=['POST'])
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