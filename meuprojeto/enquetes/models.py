from django.db import models

# Create your models here.
class Enquete(models.Model):
    """Model definition for Enquete."""

    texto = models.CharField('Texto', max_length=250)  
    data_publicacao = models.DateField('Data da publicação')

    class Meta:
        """Meta definition for Enquete."""

        verbose_name = 'Enquete'
        verbose_name_plural = 'Enquetes'

    def __str__(self):
        """Unicode representation of Enquete."""
        inicio_de_texto = (len(self.texto) * 0.10 if len(self.texto) > 25 else len(self.texto)) - 1
        return self.texto[inicio_de_texto] + '... ' + self.data_publicacao.isoformat()
