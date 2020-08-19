from django.shortcuts import render

# Create your views here.
def bemvindo(request):
    return render(request, 'bemvindo.html')