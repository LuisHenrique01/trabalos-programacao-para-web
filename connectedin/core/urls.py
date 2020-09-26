from django.urls import path
from core import views as v


urlpatterns = [
    path('', v.index, name='index'),
    path('perfil/<int:pk>/', v.perfil, name='perfil'),
    path('enviar-convite/<int:id_reme>/<int:id_dest>/', v.enviar_convite, name='enviar_convite')
]