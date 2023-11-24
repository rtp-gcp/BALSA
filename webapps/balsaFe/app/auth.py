from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps
from google.oauth2 import id_token
from google.auth.transport import requests
from google.cloud import firestore
import os

auth = Blueprint("auth", __name__)
db = firestore.Client()
# bad gateway
#db = firestore.client()


@auth.route("/login")
def login():
    print("=== hit login routine ===")
    return render_template("login.html", client_id=os.environ.get('CLIENT_ID'), login_uri=os.environ.get('LOGIN_URI'))


@auth.route("/login/callback", methods=["GET","POST"])
def callback():
    print("=== hit callback routine ===")
    # Extract the ID token sent by Google
    token = request.form.get("credential")
    try:
        # Verify the token
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), os.environ.get('CLIENT_ID'))

        # Check if the user's email is in the allowed list
        print("==== Attempting to read firestore. ====")
        email = idinfo["email"]
        print("== email:", email)
        users_ref = db.collection("allowed_users")
        print("== allowed users:", users_ref)
        user_doc = users_ref.document(email).get()
        print("== user_doc:", user_doc)
        print("==== Got collection from firestore. ====")

        #return "nope", 403

        if user_doc.exists:
            session["email"] = email
            print("session: ", session)
            return redirect(url_for("main.index"))
        else:
            # User not allowed
            print("No permission to read document?")
            return "Access Denied", 403

    except ValueError:
        # Invalid token
        return "Invalid token", 401


@auth.route("/logout")
def logout():
    session.pop("email", None)
    return redirect(url_for("auth.login"))


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "email" not in session:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)

    return decorated_function
