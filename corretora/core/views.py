from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from core.models import Inquilino, Corretor, Proprietario, Imovel, Alugar, Contactar
from core.forms import *

# Create your views here.



class HomeView(TemplateView):
    template_name = "home.html"



class InquilinoCreateView(CreateView):
    model = Inquilino
    template_name = "inquilinoCreate.html"
    form_class = InquilinoForm
    success_url = 'home'


class ProprietarioCreateView(CreateView):
    model = Proprietario
    template_name = "proprietarioCreate.html"
    form_class = ProprietarioForm
    success_url = 'home'


class CorretorCreateView(CreateView):
    model = Corretor
    template_name = "corretorCreate.html"
    form_class = CorretorForm
    success_url = 'home'


class ImovelCreateView(CreateView):
    model = Imovel
    template_name = "imovelCreate.html"
    form_class = ImovelForm
    success_url = 'home'
    
    
class AlugarCreateView(CreateView):
    model = Alugar
    template_name = "alugarCreate.html"
    form_class = AlugarForm
    success_url = 'home'
    
    
class AtendeCreateView(CreateView):
    model = Atende
    template_name = "atendeCreate.html"
    form_class = AtendeForm
    success_url = 'home'
    
    
class ContactarCreateView(CreateView):
    model = Contactar
    template_name = "contactarCreate.html"
    form_class = ContactarForm
    success_url = 'home'