#iniciamos el proyecto

from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app) #restringimos y aseguramos solicitudes http externas

@app.route('/')


def home():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=True)
