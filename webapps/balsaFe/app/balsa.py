from flask import Blueprint, render_template,  request, session, redirect, url_for, current_app

balsa = Blueprint('balsa', __name__)

## openai api request
def send_openai_request(prompt, our_mode):
    """Send a request to OpenAI API."""
    system_msg = """
    When writing code, obey these rules:

    * NAME corresponds to a LABEL and is always in column 1.
        - The NAME is at most 8 characters long.
        - The NAME begins with characters A-Z, a-z, $, # or @. 
    * OPERATION corresponds to an instruction (mnemonic) and starts in column 10.
    * OPERANDS corresponds to instruction argumennts or parameters and starts in column 15.
        - Multiple operands are separated by a comma `,`.
        - Space ` ` characters are not permitted between OPERANDS.
    * COMMENT corresponds to non functional text and has two possible starting locations.  
        - If the entire line is a comment, then the comment marker `*` starts in column 1.
        - If the comment is used at the end of a line of code, it starts at column 32.
    * Column 72 is used to identify a continuation of the current line to the next.
        - Only use a continuation character when an instruction line spans more than 65 columns.
        - In this case, use a `x` in column 72 on the first line.
        - On the second continued line, code starts at column 16.

    All code should be output in markdown or preformatted text blocks like so:

    ```
    code here
    ```

    Unless explictly told to do so, do not include any commentary.

    When specifiying registers be explicit.  For example when referring to register one, use R1 rather than 1.
    """

    our_model = current_app.openai_tuned_model if our_mode == "tuned" else current_app.openai_default_model
    print("======== our_mode: ", our_mode)
    response = current_app.openai_client.chat.completions.create(
        model=our_model,
        messages=[{"role": "system", "content": system_msg}, {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

@balsa.before_request
def require_login():
    if "user" not in session:
            return redirect(url_for("auth.login"))

@balsa.route('/balsa/train-data', methods=['POST'])
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

    return render_template('balsa.html', email=session["user"]["email"], default_model_mode=session['user']['our_mode'])


@balsa.route('/balsa/prompt', methods=['POST'])
def handle_prompt():
    """Handle form submissions from the index page."""
    action = request.form.get('action')
    prompt = request.form.get('prompt')
    response = request.form.get('response')
    session['user']['our_mode'] = request.form.get('our_mode')

    if action == 'submit':
        # Prepare and send the request to OpenAI
        response = send_openai_request(prompt, session['user']['our_mode'])

        return render_template('balsa.html', prompt=prompt, response=response, email=session["user"]["email"], default_model_mode=session["user"]['our_mode'], show_buttons=True)

    elif action == 'good':
        # Serve a blank index.html template if 'Good'
        return render_template('balsa.html', email=session["user"]["email"], default_model_mode=session["user"]['our_mode'])
    elif action == 'bad':
        # Serve the train.html template for further editing if 'Bad'
        return render_template('train.html', prompt=prompt, response=response)
    

@balsa.route('/balsa', methods=['GET'])
def balsa_index():
    """Route for the service page."""
    print("== hit balsa route === ")
    return render_template('balsa.html', email=session["user"]["email"], default_model_mode=session['user']['our_mode'])




