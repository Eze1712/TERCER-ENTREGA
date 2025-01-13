from django.contrib import admin
from .models import Post, Leyenda

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor", "estado", "fecha_publicacion"]
    list_filter = ["estado", "autor"]
    raw_id_fields = ["autor"]
    ordering = ["-fecha_publicacion"]

@admin.register(Leyenda)
class LeyendaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "genero", "fecha_nacimiento"]
    list_filter = ["genero"]
    search_fields = ["nombre", "genero"]
    ordering = ["nombre"]
