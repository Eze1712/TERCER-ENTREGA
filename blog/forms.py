from django import forms
from .models import Post, Comentario, Categoria

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'estado', 'categoria']

    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label=None)


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'contenido']

class SearchForm(forms.Form):
    query = forms.CharField(label="Buscar", max_length=100)