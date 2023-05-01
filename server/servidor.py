#iniciamos el proyecto
from  Posts.peticiones import *

from flask import Flask,request, jsonify
from flask_cors import CORS

Solicitudes = Peticiones()

app = Flask(__name__)
CORS(app) #restringimos y aseguramos solicitudes http externas

@app.route('/')


def home():
    return 'Hello, world!'

@app.route('/CrearPerfiles', methods=['POST'])
def Mensaje ():
    # Obtener los datos enviados en la solicitud en un string
    DatosXML = request.data
    #print(DatosXML)
    Solicitudes.LecturaXML(DatosXML,True)
    respuesta = Solicitudes.RespuestaS1()
    return respuesta

if __name__ == '__main__':
    app.run(debug=True)
