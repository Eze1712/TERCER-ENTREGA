from django import forms
from .models import Post, Comentario, Categoria  


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'estado', 'categoria']  


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'contenido']
