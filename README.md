# YeetBot

YeetBot is a psychiatry chatbot created using Google's Dialoglow. Our project creates a server with a RESTful API to serve any requests and responses to and from Dialogflow without all the necessary dependencies and authentications.

---
# Install

Create a virtual environment (optional, recommended): 

### Using venv & pip
Run `python -m venv env` or `python3 -m venv env` to create the virtual environment
Activate the virtual environment: 
Windows: Run `env/Scripts/activate.bat` on the command line
Install requirements: `pip install -r requirements.txt`

### Using pipenv
Run `pipenv shell` to setup virtual environment and load variables
Install requirements: `pip install -r requirements.txt`

---
# Execution

Run `flask run` in the root directory to run the server on localhost:5000

Deploying to Heroku will work using the Procfile & Pipfile.lock