from app import create_app
from dotenv import load_dotenv
import os

cwd = os.getcwd()
dotenv_path = os.path.join(cwd, '.env')
load_dotenv(dotenv_path=dotenv_path)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)