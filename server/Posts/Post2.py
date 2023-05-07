from xml.etree.ElementTree import *
from Posts.DatosMensaje import *
from Probabilidades import *

class Peticion2:

    def __init__(self):
       self.ListaMensajes = []
       self.Usuarios = []
       self.RutaMensajes =  'server\DataBase\Mensajes.xml'
       self.NMensajes = 0

    def LeerXML(self,DatosXML,veces,fuera):

        if veces:
         self.CargarBase(False)

        raiz = fromstring(DatosXML)
        for Mensajes in raiz:
          self.NMensajes +=1
          self.ListaMensajes.append(Mensajes.text.strip())

        if veces == False and fuera:
           self.SepararInformación()  

    def RespuestaS2(self):
        self.Escribir()
        self.SepararInformación()
        return f'''<?xml version="1.0"?>
<respuesta>
 <usuarios>Se procesaron mensajes para {len(self.Usuarios)} usuarios distintos</usuarios>
 <mensajes>Se procesaron {self.NMensajes} mensajes en total</mensajes>
</respuesta>'''  # si hay tiempo arreglar el numero de usuarios


    def Escribir(self):
        Mensajes = open(self.RutaMensajes,'w', encoding='utf-8')

        Mensajes.write('''<?xml version="1.0"?>
<listaMensajes>''')
        for i in range(len(self.ListaMensajes)):
         Mensajes.write(f'''
 <mensaje>
  {self.ListaMensajes[i]}
 </mensaje>''')
        Mensajes.write('''
</listaMensajes>''')
        Mensajes.close()
    
    def SepararInformación(self):
      for i in range(len(self.ListaMensajes)): 
        Lista = self.ListaMensajes[i].split('\n')

        lugarFecha = Lista[0].replace('Lugar y Fecha:','').strip()
        Usuario = Lista[1].replace('Usuario:','').strip()
        Comentario = ''
        it = 3
        while True:
         try:
          Comentario += Lista[it].strip()+'\n'
         except:
           break 
         it +=1
        info = InfoMensaje(lugarFecha,Usuario,Comentario) 
        self.ListaMensajes[i] = info
      usua = []
      for i in range(len(self.ListaMensajes)):
        usua.append(self.ListaMensajes[i].Usuario)
        
        '''
        print('Lugar y Fecha:',self.ListaMensajes[i].LugarFecha) 
        print('Usuario:',self.ListaMensajes[i].Usuario)
        print(self.ListaMensajes[i].Mensaje) '''
      
      self.Usuarios = list(set(usua))


    def CargarBase(self,fuera):
      self.ListaMensajes=[]
      self.Usuarios = []
      with open(self.RutaMensajes, 'r',encoding='utf-8') as archivo:
           contenido = archivo.read() 
      try: 
          self.LeerXML(contenido,False,fuera) #cargamos el contenido de la base de datos  
          self.NMensajes =0      
      except:
            self.NMensajes = 0
            pass     
       
    def RespuestaP (self):


      '''<?xml version="1.0"?>
<respuesta>
 <fechaHora> 01/04/2023 15:21 </fechaHora> 
 <usuario> map0002@usac.edu </usuario>
 <perfiles>
 '''

      '''
</respuesta>
'''