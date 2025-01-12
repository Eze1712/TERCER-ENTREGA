from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Post, Comentario, Categoria
from .forms import PostForm, ComentarioForm

def post_list(request):
    query = request.GET.get('q', '')  
    if query:
        post_list = Post.objects.filter(
            Q(titulo__icontains=query) | 
            Q(contenido__icontains=query) | 
            Q(autor__username__icontains=query)
        )
    else:
        post_list = Post.objects.all()

    return render(request, 'blog/post_list.html', {'posts': post_list})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.autor = request.user  
                post.save()
                return redirect("blog:post_list")
            else:
                form.add_error(None, "Debes estar logueado para crear una publicación")
    else:
        form = PostForm()

    return render(request, 'blog/post_create.html', {"form": form})

def comentario_create(request, post_id):
    post = Post.objects.get(id=post_id)  
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            if request.user.is_authenticated:
                comentario.usuario = request.user 
                comentario.post = post  
                comentario.save()
                return redirect('blog:post_list')  
            else:
                form.add_error(None, "Debes estar logueado para comentar")
    else:
        form = ComentarioForm()

    return render(request, 'blog/comentario_create.html', {"form": form, "post": post})
