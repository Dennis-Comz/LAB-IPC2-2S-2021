from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def documentacion(request):
    return render(request, 'documentacion.html')

def datos(request):
    return render(request, 'datos.html')

def select_graficas(request):
    return render(request, 'select_grafica.html')