from django.shortcuts import render, redirect
from core.models import Perfil, Convite
# Create your views here.


def index(request):
    perfis = {}
    perfis['perfis'] = Perfil.objects.all()
    return render(request, 'index.html', perfis)


def perfil(request, pk):
    context = {}
    perfis = Perfil.objects.all()
    perfil = Perfil.objects.filter(id=pk) #O filter é usado para que o retorno seja do tipo QuerySet
    amigos = perfil[0].contatos.all()
    convites_ja_feitos =  Perfil.objects.filter(id__in=[c.destinatario.id for c in perfil[0].remetente.all()])
    posiveis_amigos = perfis.difference(amigos, perfil, convites_ja_feitos)
    context['perfil'] = perfil[0]
    context['amigos'] = amigos
    context['posiveis_amigos'] = posiveis_amigos
    return render(request, 'perfil.html', context)


def enviar_convite(request, id_reme, id_dest):
    remetente = Perfil.objects.get(id=id_reme)
    destinatario = Perfil.objects.get(id=id_dest)
    convite = Convite(remetente=remetente, destinatario=destinatario)
    convite.save()
    return redirect('perfil', pk=id_reme)