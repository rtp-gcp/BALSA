from flask import Blueprint, render_template, request, redirect, url_for, session, current_app
from google.oauth2 import id_token
from google.auth.transport import requests

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template("auth.html", client_id=current_app.client_id, login_uri=current_app.login_uri)


@auth.route("/login/callback", methods=["GET","POST"])
def callback():
    #print("=== hit callback routine ===")
    # Extract the ID token sent by Google
    token = request.form.get("credential")
    try:
        # Verify the token
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), current_app.client_id)

        # Check if the user's email is in the allowed list
        #print("==== Attempting to read firestore. ====")
        email = idinfo["email"]
        #print("== email:", email)
        users_ref = current_app.firestore_client.collection("allowed_users")
        #print("== allowed users:", users_ref)
        user_doc = users_ref.document(email).get()
        #print("== user_doc:", user_doc)
        #print("==== Got collection from firestore. ====")

        #return "nope", 403

        if user_doc.exists:
            session["email"] = email
            #print("session: ", session)
            return redirect(url_for("balsa.balsa_index"))
        else:
            # User not allowed
            #print("No permission to read document?")
            return "Access Denied. Email davisjf@gmail.com for access.", 403

    except ValueError:
        # Invalid token
        return "Invalid token", 401


@auth.route("/logout")
def logout():
    session.pop("email", None)
    return redirect(url_for("auth.login"))
