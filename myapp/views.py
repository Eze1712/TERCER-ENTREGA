from django.shortcuts import render
from .models import Usuario

# Create your views here.
def index(request):
    context = {"mensaje": "Bienvenidos a mi aplicación hecha en Django"}
    return render(request, "myapp/index.html", context)
