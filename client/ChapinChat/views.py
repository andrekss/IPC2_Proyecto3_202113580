from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,"home.html")

def SServicio(request):
    return render(request,"Solicitar servicio.html")

def Peticiones(request):
    return render(request,"Peti.html")

def MensajesUsuarios(request):
    return render(request,"Msj.html")
