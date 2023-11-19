from flask import Blueprint, render_template,  request, session
from app.auth import login_required
from google.cloud import firestore
import openai
from dotenv import load_dotenv
import os

main = Blueprint('main', __name__)
db = firestore.Client()

# # Get the current working directory
# cwd = os.getcwd()
# # Construct the .env file path
# env_path = os.path.join(cwd, '.env')

# # Load the .env file
# load_dotenv(dotenv_path=env_path)
# # Set openai.api_key to the OPENAI environment variable
# OPENAI_APIKEY = os.environ["OPENAI"]
# openai.api_key=OPENAI_APIKEY

default_model="gpt-3.5-turbo-0613"
tuned_model="ft:gpt-3.5-turbo-0613:personal::8HzSS7eU"


## Uncomment and use this function if integrating with OpenAI
# def send_openai_request(prompt, our_mode):
#     """Send a request to OpenAI API."""
#     system_msg = 'You are a helpful assistant who understands IBM HLASM'  # Default system message
#     our_model = tuned_model if our_mode == "tuned" else default_model
#     response = openai.ChatCompletion.create(
#         model=our_model,
#         messages=[{"role": "system", "content": system_msg}, {"role": "user", "content": prompt}]
#     )
#     return response.choices[0].message['content']


@main.route('/handle_train_data', methods=['POST'])
@login_required
def handle_train_data():
    """Handle submissions for training data."""
    prompt = request.form['prompt']
    response = request.form['response']

    # Use 'prompt' as the document ID to overwrite the response
    doc_ref = db.collection('train_data').document(prompt)
    doc_ref.set({
        'prompt': prompt,
        'response': response
    })
    return render_template('index.html')

@main.route('/handle_prompt', methods=['POST'])
@login_required
def handle_prompt():
    """Handle form submissions from the index page."""
    action = request.form.get('action')
    our_mode = request.form.get('our_mode')
    prompt = request.form.get('prompt')
    response = request.form.get('response')

    if action == 'submit':
        # Prepare and send the request to OpenAI
        # response = send_openai_request(prompt, our_mode)
        # Mock response for demonstration purposes
        response = "def hello_world():\n    print('Hello, world!')\n\nhello_world()"
        return render_template('index.html', prompt=prompt, response=response, email=session["email"])
    elif action == 'good':
        # Serve a blank index.html template if 'Good'
        return render_template('index.html')
    elif action == 'bad':
        # Serve the train.html template for further editing if 'Bad'
        return render_template('train.html', prompt=prompt, response=response)
    

@main.route('/', methods=['GET'])
@login_required
def index():
    """Route for the home page."""
    return render_template('index.html', email=session["email"])
