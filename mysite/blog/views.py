from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def administrador(request):
    return render(request, 'blog/administrador.html', {})


def login(request):

    return render(request, 'blog/registration/login.html')

def logout(request):
    return redirect('/blog')

def nuevatienda(request):
    return render(request, 'blog/nuevatienda.html')

def nuevoproducto(request):
    return render(request, 'blog/nuevo_producto.html')

def registroventa(request):
    return render(request, 'blog/registro_venta.html')

def vendedor(request):
    return render(request, 'blog/vendedor.html')

@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})
