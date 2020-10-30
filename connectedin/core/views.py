from django.shortcuts import render, redirect
from core.models import Perfil, Convite
from django.views.generic import View
from core.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def perfil(request, pk):
    context = {}
    perfis = Perfil.objects.all()
    perfil = Perfil.objects.filter(id=pk) #O filter é usado para que o retorno seja do tipo QuerySet
    amigos = perfil[0].contatos.all()
    convites_feitos = perfil[0].remetente.all()
    convites_recebidos = perfil[0].destinatario.all()
    perfis_convites_feitos = Perfil.objects.filter(id__in=[c.destinatario.id for c in convites_feitos])
    perfis_convites_recebidos = Perfil.objects.filter(id__in=[c.remetente.id for c in convites_recebidos])
    posiveis_amigos = perfis.difference(amigos, perfil, perfis_convites_feitos, perfis_convites_recebidos)
    context['perfil'] = perfil[0]
    context['amigos'] = amigos
    context['posiveis_amigos'] = posiveis_amigos
    context['convites_recebidos'] = convites_recebidos
    return render(request, 'perfil.html', context)

@login_required
def enviar_convite(request, id_reme, id_dest):
    remetente = Perfil.objects.get(id=id_reme)
    destinatario = Perfil.objects.get(id=id_dest)
    convite = Convite(remetente=remetente, destinatario=destinatario)
    convite.save()
    return redirect('perfil', pk=id_reme)

@login_required
def aceitar_convite(request, id_conv):
    convite = Convite.objects.get(id=id_conv)
    destinatario = convite.destinatario
    remetente = convite.remetente
    destinatario.contatos.add(remetente)
    convite.delete()
    return redirect('perfil', pk=destinatario.id)

@login_required
def recusar_convite(request, id_conv):
    convite = Convite.objects.get(id=id_conv)
    destinatario = convite.destinatario
    convite.delete()
    return redirect('perfil', pk=destinata)

@login_required
def desfazer_amizade(request, id_pessoa, id_amigo):
    user = Perfil.objects.get(id=id_pessoa)
    amigo = Perfil.objects.get(id=id_amigo)
    user.contatos.remove(amigo)
    return redirect('perfil', pk=id_pessoa)
    
    
class CriarPerfil(View):
    
    def post(self, request, *args, **kwargs):
        form = PerfilForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            user = User.objects.create_user(username=dados['username'], email=dados['email'], password=dados['senha'])
            Perfil.objects.create(usuario=user, nome=dados['nome'], data_nascimento=dados['data_nascimento'])
            return redirect('index')
        return redirect(index)
            
    def get(self, request, *args, **kwargs):
        form = PerfilForm(request.POST)
        return render(request, 'criar_usuario.html', {'form': form})