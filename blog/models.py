from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = 'B', 'Borrador'
        PUBLICADO = 'P', 'Publicado'
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.BORRADOR)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True, blank=True, related_name="posts")

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Establecer un valor por defecto para 'usuario'
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.post.titulo}"

class Categoria(models.Model):
    class TipoInstrumento(models.TextChoices):
        GUITARRA = 'G', 'Guitarra'
        BAJO = 'B', 'Bajo'
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    tipo_instrumento = models.CharField(max_length=1, choices=TipoInstrumento.choices, default=TipoInstrumento.GUITARRA)
    categoria_padre = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name="subcategorias"
    )

    def __str__(self):
        return self.nombre
