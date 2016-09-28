from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# Create your views here.

def articulo_lista(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/articulo_lista.html', {'posts': posts})

def articulo_detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/articulo_detalle.html', {'post': post})
