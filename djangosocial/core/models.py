from django.db import models
from datetime import date
# Create your models here.
class Usuario(models.Model):
    email = models.EmailField('E-mail', max_length=254)
    senha = models.CharField('Senha', max_length=100)
    data_nascimento = models.DateField('Data nascimento', auto_now=False, auto_now_add=False)
    
    class Meta:
        """Meta definition for Usuario."""

        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return '%s'%self.email
    
    
class Perfil(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=200)
    contatos = models.ManyToManyField('self', related_name='contatos', blank=True)
    
    def get_timeline(self):
        return Postagem.objects.filter(perfil=self)
    
    class Meta:
        """Meta definition for Perfil."""

        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
    
    def __str__(self):
        return '%s'%self.nome
    
    
class Postagem(models.Model):
    texto = models.TextField('Texto')
    data = models.DateField('Data criação', auto_now_add=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    
    def get_count_reacoes(self):
        return Reacao.objects.annotate(
            count_reacao=(models.Count('tipo') * models.F('peso'))
        ).filter(postagem=self)
    
    class Meta:
        """Meta definition for Postagem."""
        ordering = ['data']
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
    
    def __str__(self):
        if len(self.texto) > 15:
            return self.texto[:15:]  
        return self.texto
    
    
class Comentario(models.Model):
    """Model definition for Comentario."""

    texto = models.TextField('Texto')
    data = models.DateField('Data criação', auto_now_add=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Comentario."""
        ordering = ['data']
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        """Unicode representation of Comentario."""
        if len(self.texto) > 15:
            return self.texto[:15:]  
        return self.texto
    
    
class Reacao(models.Model):
    """Model definition for Reacao."""
    class Tipos(models.TextChoices):
        CURTIR = 'Curtir'
        AMAR = 'Amar'
        RIR = 'Rir' 
        IMPRECIONANTE = 'Imprecionante'
        TRISTE = 'Triste'
        IRRITANTE = 'Irritante'
        
    tipo = models.CharField('Tipo', max_length=13, choices=Tipos.choices)
    data = models.DateField('Data criação', auto_now_add=True)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    peso = models.IntegerField('Peso')
    
    class Meta:
        """Meta definition for Reacao."""

        verbose_name = 'Reaçao'
        verbose_name_plural = 'Reacões'

#    def save(self, *args, **kwargs):
#        """Gerenciando para que o mesmo usuario use duas ou mais reações no mesmo post"""
#        reacao = Reacao.objects.filter(postagem=self.postagem, perfil=self.perfil)
#        self.data = date.today()
#        if len(reacao) > 0:
#            self.id = reacao[0].id
#            super(Reacao, self).save(*args, **kwargs)
#        super(Reacao, self).save(*args, **kwargs)

    def __str__(self):
        """Unicode representation of Reacao."""
        return f'{self.tipo}'
