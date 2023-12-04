from flask import Blueprint, render_template,  request, session, redirect, url_for, current_app

main = Blueprint('main', __name__)



@main.route('/', methods=['GET'])
def index():
    print("== hit main index route === ")


    return render_template('index.html')

