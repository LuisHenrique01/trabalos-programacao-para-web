from django.db import models


class PessoaAbstract(models.Model):
    """Model definition for Pessoa."""

    cpf = models.IntegerField("CPF", primary_key=True)
    nome = models.CharField('Nome', max_length=250)
    telefone = models.CharField('Telefone', max_length=250)
    email = models.EmailField('E-mail', max_length=254)
    cidade = models.CharField('Cidade', max_length=250)
    bairro = models.CharField('Bairro', max_length=250)
    rua = models.CharField('Rua', max_length=250)
    numero = models.CharField('Numero', max_length=20)
    complemento = models.CharField('Complemento', max_length=300, blank=True, null=True)

    class Meta:
        """Meta definition for Pessoa."""

        abstract =True

    def __str__(self):
        """Unicode representation of Pessoa."""
        return f'{self.nome}'



class Inquilino(PessoaAbstract):
    """Model definition for Inquilino."""


    class Meta(PessoaAbstract.Meta):
        """Meta definition for Inquilino."""

        verbose_name = 'Inquilino'
        verbose_name_plural = 'Inquilinos'


class Corretor(PessoaAbstract):
    """Model definition for Corretor."""

    salario = models.FloatField('Salario')

    class Meta(PessoaAbstract.Meta):
        """Meta definition for Corretor."""

        verbose_name = 'Corretor'
        verbose_name_plural = 'Corretores'


class Proprietario(PessoaAbstract):
    """Model definition for Proprietario  ."""

    class Meta(PessoaAbstract.Meta):
        """Meta definition for Proprietari."""

        verbose_name = 'Proprietario'
        verbose_name_plural = 'Proprietarios'


class Imovel(models.Model):
    """Model definition for Imovel."""
    
    ALUGADO = [(True, 'Sim'),
               (False, 'Não')]

    descricao = models.TextField('Descrição')
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE)
    valor_aluguel = models.FloatField('Valor do Aluguel')
    alugado = models.BooleanField('Alugado', choices=ALUGADO)

    class Meta:
        """Meta definition for Imovel."""

        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'

    def __str__(self):
        """Unicode representation of Imovel."""
        return f'{self.valor_aluguel:.2f} - {self.alugado}'
    
    
class Alugar(models.Model):
    """Model definition for Alugar."""

    inquilino = models.ForeignKey(Inquilino, on_delete=models.CASCADE)
    data_aluguel = models.DateField('Data do aluguel')
    data_vencimento = models.DateField('Data de Vencimento')
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    corretor = models.ForeignKey(Corretor, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Alugar."""

        verbose_name = 'Alugado'
        verbose_name_plural = 'Alugados'

    def __str__(self):
        """Unicode representation of Alugar."""
        return f'{self.inquilino.nome}'


class Atende(models.Model):
    """Model definition for Atende."""

    corretor = models.ManyToManyField(Corretor)
    inquilino = models.ManyToManyField(Inquilino)
    data = models.DateField('Data e hora de atendimento')

    class Meta:
        """Meta definition for Atende."""

        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'

    def __str__(self):
        """Unicode representation of Atende."""
        return f'{self.corretor.nome} - {self.inquilino.nome}'
    
    
class Contactar(models.Model):
    """Model definition for Contatar."""

    corretor = models.ManyToManyField(Corretor)
    proprietario = models.ManyToManyField(Proprietario)
    data = models.DateField('Data e hora de atendimento')

    class Meta:
        """Meta definition for Contatar."""

        verbose_name = 'Contatar'
        verbose_name_plural = 'Contatars'

    def __str__(self):
        """Unicode representation of Contatar."""
        return f'{self.corretor.nome} - {self.proprietario.nome}'
