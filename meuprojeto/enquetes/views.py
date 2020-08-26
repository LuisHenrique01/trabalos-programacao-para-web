from django.shortcuts import render
from .models import Enquete
# Create your views here.
def bemvindo(request):
    return render(request, 'bemvindo.html')


def enquete(request, enquete_id):
    context = {}
    if enquete_id == 1:
        context['enquete'] = Enquete("Como usar classes em Python?", '2020-08-26')
    elif enquete_id == 1:
        context['enquete'] = Enquete("O que é Django REST Framework", '2020-07-30') 
    elif enquete_id == 3:
        context['enquete'] = Enquete("O que é **kwargs?", '2020-08-16')
    return render(request, 'enquete.html', context)