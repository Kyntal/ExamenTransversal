from django.shortcuts import render

# Create your views here.
def administrador(request):
    return render(request, 'blog/administrador.html', {})

