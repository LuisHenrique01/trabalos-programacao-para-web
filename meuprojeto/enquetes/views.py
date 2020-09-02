from django.shortcuts import render, get_object_or_404
from .models import Enquete
# Create your views here.
def bemvindo(request):
    return render(request, 'bemvindo.html')


def enquete(request, enquete_id):
    #context = {'enquete': Enquete.objects.get(id=enquete_id)}
    context = {'enquete': get_object_or_404(Enquete, id=enquete_id)}
    return render(request, 'enquete.html', context)