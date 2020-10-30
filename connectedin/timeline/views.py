from django.shortcuts import render, redirect
from core.models import Perfil, Postagem
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    perfil = request.user.perfil
    context = {'perfil': perfil}
    context['posts'] = perfil.get_timeline()
    return render(request, 'index.html', context)


@login_required
def postar(request):
    perfil = request.user.perfil
    texto = request.GET['texto']
    Postagem.objects.create(perfil=perfil, texto=texto)
    return redirect('index')