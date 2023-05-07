#iniciamos el proyecto
from  Posts.Post1 import *
from Posts.Post2 import *
from flask import Flask,request
from flask_cors import CORS
from Probabilidades import *


app = Flask(__name__)
CORS(app) #restringimos y aseguramos solicitudes http externas

@app.route('/')

def home():
    return 'Hello, world!'

@app.route('/Configuracion', methods=['POST'])
def ProfileDesc():
    # Obtener los datos enviados en la solicitud en un string
    DatosXML = request.data
    #print(DatosXML)
    Solicitud1 = Peticion1()

    Solicitud1.LecturaXML(DatosXML,True)
    respuesta = Solicitud1.RespuestaS1()
    return respuesta

@app.route('/Mensajes', methods=['POST'])
def Mensajes():
    Solicitud2 = Peticion2()

    DatosXML = request.data  # rconoce las tildes
    Solicitud2.LeerXML(DatosXML,True,False)
    respuesta = Solicitud2.RespuestaS2()
    return respuesta



@app.route('/MensajesUsuarios', methods=['GET'])
def Tablas():
    Solicitud2 = Peticion2()
    Solicitud1 = Peticion1()

    Solicitud1.CargarBase()
    Solicitud2.CargarBase(True)
    pro = Probabilidad(Solicitud2.ListaMensajes,Solicitud1.Perfiles,Solicitud1.Descartadas,Solicitud2.Usuarios,Solicitud1.NombresPerfiles,'','')
    pro.AnalizarMensaje(True)

    respuesta = pro.respuesta()

    return respuesta

@app.route('/FiltroUsuarios', methods=['POST'])
def FiltroUsuarios():
    Solicitud2 = Peticion2()
    Solicitud1 = Peticion1()
    usuario = str(request.data)
    usuario = usuario.replace("b", "").replace("'", "")

    print('--->'+usuario+'<----')
    Solicitud1.CargarBase()
    Solicitud2.CargarBase(True)
    pro = Probabilidad(Solicitud2.ListaMensajes,Solicitud1.Perfiles,Solicitud1.Descartadas,Solicitud2.Usuarios,Solicitud1.NombresPerfiles,usuario,'')
    pro.AnalizarMensaje(True)

    respuesta = pro.respuesta()

    return respuesta

@app.route('/FiltroFechas', methods=['POST'])
def FiltroFechas():
    Solicitud2 = Peticion2()
    Solicitud1 = Peticion1()
    fecha = str(request.data)
    fecha = fecha.replace("b", "").replace("'", "")

    print('--->'+fecha+'<----')
    Solicitud1.CargarBase()
    Solicitud2.CargarBase(True)
    pro = Probabilidad(Solicitud2.ListaMensajes,Solicitud1.Perfiles,Solicitud1.Descartadas,Solicitud2.Usuarios,Solicitud1.NombresPerfiles,'',fecha)
    pro.AnalizarMensaje(True)

    respuesta = pro.respuesta()

    return respuesta



@app.route('/GetPesos', methods=['GET'])
def Pesos():
    Solicitud2 = Peticion2()
    Solicitud1 = Peticion1()

    Solicitud1.CargarBase()
    Solicitud2.CargarBase(True)
    pro = Probabilidad(Solicitud2.ListaMensajes,Solicitud1.Perfiles,Solicitud1.Descartadas,Solicitud2.Usuarios,Solicitud1.NombresPerfiles,'','')
    pro.AnalizarMensaje(False) 
    pro.PesosUsuarioPerfil() 
    respuesta = pro.respuesta()  

    return respuesta

@app.route('/PesosUsuarios', methods=['POST'])
def PesosU():
    Solicitud2 = Peticion2()
    Solicitud1 = Peticion1()
    
    usuario = str(request.data)
    print(usuario)
    usuario = usuario.replace("b", "").replace("'", "")

    Solicitud1.CargarBase()
    Solicitud2.CargarBase(True)
    pro = Probabilidad(Solicitud2.ListaMensajes,Solicitud1.Perfiles,Solicitud1.Descartadas,Solicitud2.Usuarios,Solicitud1.NombresPerfiles,usuario,'')
    pro.AnalizarMensaje(False) 
    pro.PesosUsuarioPerfil() 
    respuesta = pro.respuesta()  

    return respuesta


@app.route('/MensajesP', methods=['POST'])
def MensajesP():

    Solicitud2 = Peticion2()

    DatosXML = request.data  # rconoce las tildes
    Solicitud2.LeerXML(DatosXML,True,False)
    respuesta = Solicitud2.RespuestaP()
    return respuesta

@app.route('/BorrarBase', methods=['GET'])
def Borrar():
  
  with open("server\DataBase\Mensajes.xml", "w") as f:
            f.write("")

  with open("server\DataBase\PerfilesDescartes.xml", "w") as f:
            f.write("")
            
  
  return "El contenido del archivo ha sido borrado exitosamente."

if __name__ == '__main__':
    app.run(debug=True)
