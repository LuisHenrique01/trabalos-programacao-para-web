from django.urls import path, include
from core.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create-inquilino/', InquilinoCreateView.as_view(), name='InquilinoCreate'),
    path('create-proprietario/', ProprietarioCreateView.as_view(), name='ProprietarioCreate'),
    path('create-corretor/', CorretorCreateView.as_view(), name='CorretorCreate'),
    path('create-imovel/', ImovelCreateView.as_view(), name='ImovelCreate'),
    path('alugar/', AlugarCreateView.as_view(), name='AlugarCreate'),
    path('atendimento/', AtendeCreateView.as_view(), name='AtendeCreate'),
    path('contactar/', ContactarCreateView.as_view(), name='ContactarCreate'),
]