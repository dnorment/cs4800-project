# Installation
Create a virtual environment: 
`python -m venv env` OR `python3 -m venv env`
Activate the virtual environment: 
Windows: `env/Scripts/activate.bat`
Linux: `source env/bin/activate`
Install requirements: `pip install -r requirements.txt`

# Execution
Run `flask run` in the root directory
Flask will run the server on port 5000, which needs to be exposed to use DialogFlow callbacks
Run `ngrok http 5000` in the root directory
Edit DialogFlow fulfillment webhook to be the ngrok address from last step