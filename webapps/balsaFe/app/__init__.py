from flask import Flask
from google.cloud import firestore
from openai import OpenAI
import os
from dotenv import load_dotenv

# Get the current working directory and load .env
cwd = os.getcwd()
env_path = os.path.join(cwd, '.env')
load_dotenv(dotenv_path=env_path)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY',"SECRET_KEY")
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_COOKIE_SECURE'] = True  
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

    app.admin = os.environ.get("ADMIN")
    app.client_id = os.environ.get('CLIENT_ID')
    app.login_uri = os.environ.get('LOGIN_URI')

    # Init firestore client
    db = firestore.Client()

    # Crete firestore collection and a user as document ID
    doc_ref = db.collection("allowed_users").document(app.admin)
    doc_ref.set({})
    if not doc_ref.get().exists:
        print(f"allowed_users collection is no created in firestore")
    
    # attach firesotre to the app
    app.firestore_client = db

    # OpenAI init
    # attach openai api to the app
    app.openai_client = OpenAI()
    app.openai_default_model = os.environ.get('GPT_DEFAULT_MODEL')
    app.openai_tuned_model = os.environ.get('GPT_TUNED_MODEL')

    # register blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .service import service as service_blueprint
    app.register_blueprint(service_blueprint)

    return app