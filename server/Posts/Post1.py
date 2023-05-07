from xml.etree.ElementTree import *
import re

class Peticion1:
    
    def __init__(self):
        self.NombresPerfiles = []
        self.Perfiles = []   # cada casilla tiene un arreglo con las palabras clave
        self.Descartadas = []
        self.rutaPerfiles = "server\DataBase\PerfilesDescartes.xml"
        self.PDescartadasN = 0
        self.PerfilesN = 0
        self.PefilesActE = 0

    def LecturaXML(self,DatosXML,veces):
        if veces:
         self.CargarBase()
        contador = 0

        raiz = fromstring(DatosXML) # fromstring convierte el string en la raíz del archivo
        for lista in raiz:
            if contador == 0:
                for perfil in lista:      
                    repetido,IndicePerfil =self.nombresRepetidos(perfil.find('nombre').text)
                    if repetido:
                     self.PerfilesN+=1
                     self.PefilesActE+=1

                     self.NombresPerfiles.append(perfil.find('nombre').text.strip())
                     palabraClave = perfil.find('palabrasClave')
                     PalabrasClave = []
                     for Palabra in palabraClave:
                       Palabra =re.findall('\w+',Palabra.text.strip())
                       for definitivo in Palabra:
                        PalabrasClave.append(definitivo)
                     self.Perfiles.append(PalabrasClave)   
                    else:
                       self.Alterno(perfil,IndicePerfil)    # perfiles ya creados

            elif contador ==1:
                for Descarte in lista:
                    repetido = self.PalabrasRepetidas(Descarte.text,0,False)
                    if repetido:
                     self.PDescartadasN +=1
                     self.Descartadas.append(Descarte.text.strip())
            contador+=1  
    
    def Escribir(self):   #Escribir en el texto
       
       Perfiles = open(self.rutaPerfiles,'w',encoding='utf-8')

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
 <perfilesNuevos>Se han creado {self.PerfilesN} perfiles nuevos</perfilesNuevos>
 
 <perfilesExistentes>Se han actualizado {self.PefilesActE} perfiles existentes</perfilesExistentes>

 <descartadas>Se han creado {self.PDescartadasN} nuevas palabras a descartar</descartadas>
 
 </respuesta>'''   

    def nombresRepetidos(self,perfil):
       for i in range(len(self.NombresPerfiles)): #verifica si se repite
          if self.NombresPerfiles[i] ==  perfil:
             return False,i
       return True,None    # no se repite

    def PalabrasRepetidas(self,palabra,IndicePerfil,modoPerfiles):
      if modoPerfiles: 
       for i in range(len(self.Perfiles[IndicePerfil])):
          if palabra == self.Perfiles[IndicePerfil][i]:
        
            return False
       return True       # no se repite 
      else:
         for i in self.Descartadas:
            if palabra == i:
               return False
         return True  

    def Alterno(self,perfil,IndicePerfil):
       
       palabraClave = perfil.find('palabrasClave')
       a = 0
       for palabra in palabraClave:
         repetido = self.PalabrasRepetidas(palabra.text,IndicePerfil,True)
         if repetido:
           if a ==0:
            self.PefilesActE +=1
           self.Perfiles[IndicePerfil].append(palabra.text.strip())  
         else:
            continue  
         a+=1   

    def Reinicio(self,listas,contadores):
         if listas:
          self.NombresPerfiles = []
          self.Perfiles = []
          self.Descartadas = []  
         if contadores:    
          self.PDescartadasN = 0
          self.PerfilesN = 0
          self.PefilesActE = 0

    def CargarBase(self):
         self.Reinicio(True,True)
         # ruta de la base de datos
         with open(self.rutaPerfiles, 'r',encoding='utf-8') as archivo:
          contenido = archivo.read()

         if contenido !='':
          self.LecturaXML(contenido,False) # cargamos los datos de la base de datos
          self.Reinicio(False,True)
          
             
          