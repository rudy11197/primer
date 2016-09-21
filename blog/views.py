from django.shortcuts import render

def articulo_lista(request):
    return render(request, 'blog/articulo_lista.html', {})
