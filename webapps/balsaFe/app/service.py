from flask import Blueprint, render_template,  request, session, redirect, url_for, current_app

service = Blueprint('service', __name__)

## openai api request
def send_openai_request(prompt, our_mode):
    """Send a request to OpenAI API."""
    system_msg = 'You are a helpful assistant who understands IBM HLASM'  # Default system message
    our_model = current_app.openai_tuned_model if our_mode == "tuned" else current_app.openai_default_model
    response = current_app.openai_client.chat.completions.create(
        model=our_model,
        messages=[{"role": "system", "content": system_msg}, {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

@service.before_request
def require_login():
    if "email" not in session:
            return redirect(url_for("auth.login"))

@service.route('/train-data', methods=['POST'])
def handle_train_data():
    """Handle submissions for training data."""
    prompt = request.form['prompt']
    response = request.form['response']

    # Use 'prompt' as the document ID to overwrite the response
    doc_ref = current_app.firestore_client.collection('train_data').document(prompt)
    doc_ref.set({
        'prompt': prompt,
        'response': response
    })
    return render_template('index.html', email=session["email"], mode=session['our_mode'])

@service.route('/prompt', methods=['POST'])
def handle_prompt():
    """Handle form submissions from the index page."""
    action = request.form.get('action')
    prompt = request.form.get('prompt')
    response = request.form.get('response')
    session['our_mode'] = request.form.get('our_mode')

    if action == 'submit':
        # Prepare and send the request to OpenAI
        response = send_openai_request(prompt, session['our_mode'])
        return render_template('index.html', prompt=prompt, response=response, email=session["email"], show_buttons=True)
    elif action == 'good':
        # Serve a blank index.html template if 'Good'
        return render_template('index.html', email=session["email"])
    elif action == 'bad':
        # Serve the train.html template for further editing if 'Bad'
        return render_template('train.html', prompt=prompt, response=response)
    

@service.route('/', methods=['GET'])
def index():
    """Route for the service page."""
    print("== hit index route === ")
    return render_template('index.html', email=session["email"], mode=session['our_mode'])
