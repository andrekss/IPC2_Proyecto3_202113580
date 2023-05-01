from xml.etree.ElementTree import *

class Peticiones:
    def __init__(self):
        self.NombresPerfiles = []
        self.Perfiles = []
        self.Descartadas = []
        self.rutaPerfiles = "server\DataBase\Perfiles.xml"

    def LecturaXML(self,DatosXML,veces):
        if veces:
         self.NombresPerfiles = []
         self.Perfiles = []
         self.Descartadas = []

         ruta =  self.rutaPerfiles# ruta de la base de datos
         with open(ruta, 'r') as archivo:
          contenido = archivo.read()

         if contenido !='':
          self.LecturaXML(contenido,False) # cargamos los datos de la base de datos

        contador = 0
        raiz = fromstring(DatosXML) # fromstring convierte el string en la raíz del archivo
        for lista in raiz:
            if contador == 0:
                for perfil in lista:      
                    repetido,IndicePerfil =self.nombresRepetidos(perfil.find('nombre').text)
                    
                    if repetido:
                     self.NombresPerfiles.append(perfil.find('nombre').text)
                     palabraClave = perfil.find('palabrasClave')
                     PalabrasClave = []
                     for Palabra in palabraClave:
                       PalabrasClave.append(Palabra.text)
                     self.Perfiles.append(PalabrasClave)   
                    else:
                       palabraClave = perfil.find('palabrasClave')
                       for palabra in palabraClave:
                          self.Perfiles[IndicePerfil].append(palabra.text)
                       continue    

            elif contador ==1:
                for Descarte in lista:
                    self.Descartadas.append(Descarte.text)
            contador+=1  
    
    def Escribir(self):   #Escribir en el texto
       
       Perfiles = open(self.rutaPerfiles,'w')

       Perfiles.write('''<?xml version="1.0"?>
<configuracion>
 
 <perfiles>''')
       
       for i in range(len(self.NombresPerfiles)):
        Perfiles.write(f'''
  <perfil>
    <nombre>{self.NombresPerfiles[i]}</nombre>
    <palabrasClave>''')
        for j in range(len(self.Perfiles[i])):
          Perfiles.write(f'''
     <palabra>{self.Perfiles[i][j]}</palabra>''')
    
        Perfiles.write('''
        </palabrasClave>
  </perfil>''')
       
       Perfiles.write(
       '''
 </perfiles>''')
 
       Perfiles.write(
    '''
 <descartadas>''')
       for i in self.Descartadas:
        Perfiles.write(f'''
  <palabra>{i}</palabra>''')

       Perfiles.write('''
 </descartadas>
</configuracion>''')
       Perfiles.close()
   
   
    def RespuestaS1(self):
        self.Escribir()
        return f'''<?xml version="1.0"?>
<respuesta>
 <perfilesNuevos>Se han creado {str(len(self.Perfiles))} perfiles nuevos</perfilesNuevos>
 
 <perfilesExistentes>Se han actualizado 2 perfiles existentes</perfilesExistentes>

 <descartadas>Se han creado {str(len(self.Descartadas))} nuevas palabras a descartar</descartadas>
 
</respuesta>'''   

    def nombresRepetidos(self,perfil):
       for i in range(len(self.NombresPerfiles)): #verifica si se repite
          if self.NombresPerfiles[i] ==  perfil:
             return False,i
       return True,None    # no se repite
             

