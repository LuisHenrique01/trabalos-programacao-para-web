from django.urls import path
from timeline import views as v


urlpatterns = [
    path('', v.index, name='index'),
    path('postar/', v.postar, name='postar')
]