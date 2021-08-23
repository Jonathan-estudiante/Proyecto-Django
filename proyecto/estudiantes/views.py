from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import*

# Create your views here.
def homepage(request):
    estudiantes = Estudiante.objects.all()
    contexto = {
        'estudiante':estudiantes
    }
    return render(request, "principal/inicio.html", contexto)

class CreateStudent(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'estudiantes/new-student.html'
    success_url = reverse_lazy('estudiantes:list-student')

def listStudent(request):
    estudiante = Estudiante.objects.all()
    contexto = {
        'estudiante': estudiante
    }
    return render(request, 'estudiantes/list-student.html', contexto)

class EditStudent(UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name  = 'estudiantes/edit-student.html'
    success_url = reverse_lazy('estudiantes:list-student')

def deleteStudent(request, id):
    estudiante = Estudiante.objects.get(id = id)
    estudiante.delete()
    return redirect('estudiantes:list-student')