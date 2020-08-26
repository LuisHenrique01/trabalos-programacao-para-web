from django.db import models

# Create your models here.
class Enquete(object):
    
    def __init__(self, texto, data_publicacao):
        self.texto = texto
        self.data_publicacao = data_publicacao