from django.urls import path
from core import views as v


urlpatterns = [
    path('<int:pk>/', v.perfil, name='perfil'),
    path('enviar-convite/<int:id_reme>/<int:id_dest>/', v.enviar_convite, name='enviar_convite'),
    path('aceitar-convite/<int:id_conv>/', v.aceitar_convite, name='aceitar_convite'),
    path('recusar-convite/<int:id_conv>/', v.recusar_convite, name='recusar_convite'),
    path('desfazer_amizade/<int:id_pessoa>/<int:id_amigo>/', v.desfazer_amizade, name='desfazer_amizade'),
    path('criar_usuario/', v.CriarPerfil.as_view(), name='criar_usuario')
]