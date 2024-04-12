from django.shortcuts import render
from .models import Curso
# Create your views here.

def home(request):
    cursos = Curso.objects.all()
    
    return render(request, 'gestioncursos.html', {"curso":cursos})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numcreditos']
    
    
    
    return render(request,)
