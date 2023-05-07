import re

class Probabilidad:

    def __init__(self,ListaMensajes,Perfiles,Descartadas,Usuarios,NombresPerfiles,usuarioE,Fecha):
        self.Probabilidades = [] #Tendrá el mismo tamaño  de la lista de mensajes, y cada casilla tendra
        # una lista con el mismo tamaño de perfiles
        self.FechasPorMensaje = [] # tendrá el mismo tamaño que las probabilidades
        self.ListaMensajes = ListaMensajes
        self.Perfiles = Perfiles 
        self.Descartadas = Descartadas  # palabras descartadas
        self.Usuarios = Usuarios  #todos los usuarios por mensaje
        self.NombresPerfiles = NombresPerfiles
        self.usuarioE =usuarioE
        self.Fecha = Fecha
        self.coincidencia = 0
        self.TablaHTML = ''
        self.bordes = 'style="border: 1px solid black;"'

    def AnalizarMensaje(self,visualizar):
        AllWordsMensajes = []
        patron = r"\d{2}/\d{2}/\d{4}"    
        for i in range(len(self.ListaMensajes)): #primer paso encontrar todas las palabras excepto las descartadas
            AllWords = []
            palabras = re.findall('\w+',self.ListaMensajes[i].Mensaje)
            self.BuscarFechas(patron,i)
            for palabra in palabras: #recorre solo palabras
                guardar = True
                for descarte in self.Descartadas:
                    if palabra.lower() != descarte.lower(): # método lower para evitar que se comparen mayúsculas o minúsculas
                        if palabra.isdigit():
                            guardar = False
                            break
                        continue
                    else:
                        guardar = False
                        #print(palabra)
                        break
                if guardar:
                 AllWords.append(palabra)
                 #print('---->'+palabra+'<---')
            AllWordsMensajes.append(AllWords)    
        '''
        for i in range(len(AllWordsMensajes)):
            print('Mensaje',str(i+1))
            for j in range(len(AllWordsMensajes[i])):
                print('---->'+AllWordsMensajes[i][j]+'<----')''' 

        ''' 
        for i in range(len(AllWordsMensajes)):
            print('tamaño para el mensaje',str(i+1))
            print(len(AllWordsMensajes[i]))'''
        
        #paso 2: palabras que coinciden con los perfiles
        for i in range(len(AllWordsMensajes)):
            probable = []
            for k in range(len(self.Perfiles)):   
                self.coincidencia = 0 
                self.RecorrerMensaje(AllWordsMensajes,i,k,probable)
            self.Probabilidades.append(probable)     
        
        
        #Filtros
        
        if visualizar: 
         '''
         Filtro = input('Que filtro necesita por fecha o por usuario, esciba T para todos:')
        
         if Filtro == 'usuario':
         
          usuario = input("Escriba el usuario:") 
          Cada = 1
         elif Filtro ==  'fecha':  

          fecha = input('Escriba la fecha dd/mm/yyyy:') 
          Cada = 2
         elif Filtro == 'T': 
         
            Cada = 3'''
         if self.usuarioE == '':
          Cada = True
          Cada1 = True
         elif self.usuarioE:
            Cada = False
            Cada1 = True
            True
         if self.Fecha:
            Cada = True
            Cada1 = False   
        
         self.TablaHTML = ''
         self.TablaHTML = '<h2>Probabilidad del mensaje por perfil<h2>'
         for usuario in self.Usuarios:
          if self.usuarioE == usuario or Cada:
            self.TablaHTML += f'<h3>Usuario: {usuario}<h3>'
            self.TablaHTML +=f'<table {self.bordes}><tr><th {self.bordes}>Mensaje</th>'
            it = 0
            for i in range(len(self.Probabilidades)):  #recorrer mensajes  
             if self.ListaMensajes[i].Usuario == usuario:
              self.recorrerPerfiles(i,it,Cada1)  
              it +=1
            self.TablaHTML +='</tr><tr></table>\n' 
        #self.PesosUsuarioPerfil()     
               
    def recorrerPerfiles(self,i,it,cada1):
            
            print('-----------mensaje',str(i+1)+'------------')
            if it ==0:
             for j in range(len(self.Probabilidades[i])): #recorre perfiles
                
                self.TablaHTML += f'<th {self.bordes}>{self.NombresPerfiles[j]}</th>'
                if j == (len(self.Probabilidades[i])-1):
                   self.TablaHTML +='</tr><tr>' 
            
            if cada1 or self.FechasPorMensaje[i] == self.Fecha: 
             fecha = self.ListaMensajes[i].LugarFecha.split(',')[1].strip()
             self.TablaHTML+=f'<tr><td {self.bordes}>{fecha}</td>'

             for j in range(len(self.Probabilidades[i])): #recorre perfiles 
                print('--perfil',str(j+1)+'--')   
                self.TablaHTML += f'<td {self.bordes}>{self.Probabilidades[i][j]}</td>'
                print(self.Probabilidades[i][j])  

    def respuesta(self):
       return self.TablaHTML

    def RecorrerMensaje(self,AllWordsMensajes,i,k,probable):
        for j in range(len(AllWordsMensajes[i])):
            for l in range(len(self.Perfiles[k])):
                if AllWordsMensajes[i][j].lower() == self.Perfiles[k][l].lower():
                    #print('mensaje',str(i+1),'en perfil',str(k+1),':'+AllWordsMensajes[i][j])
                    self.coincidencia+=1
        probable.append("{:.2f}".format((self.coincidencia/len(AllWordsMensajes[i]))*100)) 

    def BuscarFechas(self,patron,i):
        match = re.search(patron,self.ListaMensajes[i].LugarFecha)
        if match:
            self.FechasPorMensaje.append(str(match.group()))    # con group jalamos la fecha    
    
    def PesosUsuarioPerfil(self):
        sumas = []
        numeroMensajes=[]
        PesosPorUsuario = [] # tendrá el tamaño de numero de usuarios
        for i in range(len(self.Perfiles)):  # llenamos de ceros el arreglo suma  
             sumas.append(0)  
             numeroMensajes.append(0)                  # para que tenga el tamaño de los perfiles        
        
        
        for usuario in range(len(self.Usuarios)): #recorremos usuario
            
            sumas = [0] * len(self.Perfiles) # vaciamos el arreglo
            numeroMensajes = [0]*len(self.Perfiles)

            for j in range(len(self.Probabilidades)):  #recorremos mensajes
               if self.Usuarios[usuario] == self.ListaMensajes[j].Usuario:
                for k in range(len(self.Probabilidades[j])):  # recorremos probabilidad por perfil 
                    if float(self.Probabilidades[j][k]) !=0: # sumamos si es diferente de 0
                      numeroMensajes[k] +=1                
                    sumas[k] += float(self.Probabilidades[j][k])
                    #print(sumas[k])     
            #print(sumas)         
            PesosPorUsuario.append(sumas)  
            for j in range(len(PesosPorUsuario[usuario])):
                PesosPorUsuario[usuario][j] = float("{:.2f}".format(PesosPorUsuario[usuario][j]/numeroMensajes[j]))        

        

        '''
        Filtro = input('Que filtro necesita todos o por usuario:')

        if Filtro == 'todos':
           cad = 1
        elif Filtro== 'usuario':
           us = input('Escriba el usuario:')
           cad = 2  '''
           
        self.TablaHTML = f'<h2>Probabilidad del mensaje por perfil<h2><table {self.bordes}>'
        self.TablaHTML += f'<tr><th {self.bordes}>Usuario</th>'
        for j in range(len(self.NombresPerfiles)):
           
           self.TablaHTML +=f'<th {self.bordes}>{self.NombresPerfiles[j]}</th>'
           
        if self.usuarioE == '':
           cad = True
        else:
           cad = False   
        for i in range(len(PesosPorUsuario)):
            #print('----Usuario '+str(i+1)+'----')
           if self.Usuarios[i] == self.usuarioE or cad:
            self.TablaHTML +=f'<tr><td {self.bordes}>{self.Usuarios[i]}</td>'
            print('-------'+self.Usuarios[i]+'-------')
            for j in range(len(PesosPorUsuario[i])):
              print('Perfil '+str(j+1))
              self.TablaHTML += f'<td {self.bordes}>{PesosPorUsuario[i][j]}</td>'
              if j == len(PesosPorUsuario[i])-1:
                 self.TablaHTML += '</tr>'
              print(PesosPorUsuario[i][j])   
        self.TablaHTML +='</table>'                      
                                  