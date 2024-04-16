from django.shortcuts import render, redirect
from .models import Curso
# Create your views here.

def home(request):
    cursos = Curso.objects.all()
    
    return render(request, 'gestioncursos.html', {"curso":cursos})

def registrarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    
    curso = Curso.objects.create(codigo=codigo, nombre = nombre, creditos = creditos)
    
    return redirect('/')

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    
    return redirect('/')
