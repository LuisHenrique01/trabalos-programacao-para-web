from django.shortcuts import render, get_object_or_404
from .models import Enquete
from django.views import View, generic
# Create your views here.

"""
class bemvindo(generic.TemplateView):
    template_name = 'bemvindo.html'
    

class bemvindo(View):
    def get(self, request):
        return render(request, 'bemvindo.html')
"""
def bemvindo(request):
    return render(request, 'bemvindo.html')

def enquete(request, enquete_id):
    #context = {'enquete': Enquete.objects.get(id=enquete_id)}
    context = {'enquete': get_object_or_404(Enquete, id=enquete_id)}
    return render(request, 'enquete.html', context)

"""
class enquete(generic.DetailView):
    model = Enquete
    template_name = 'enquete.html'
    pk_url_kwarg = 'enquete_id'


class enquete(View):
    def get(self, request, enquete_id):
        context = {'enquete': get_object_or_404(Enquete, id=enquete_id)}
        return render(request, 'enquete.html', context)
"""