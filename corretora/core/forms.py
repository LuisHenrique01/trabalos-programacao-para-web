from django import forms
from core.models import Inquilino, Corretor, Proprietario, Imovel, Alugar, Atende, Contactar

class InquilinoForm(forms.ModelForm):
    """Form definition for Inquilino."""

    class Meta:
        """Meta definition for Inquilinoform."""

        model = Inquilino
        exclude = ['id']
        
        
class ProprietarioForm(forms.ModelForm):
    """Form definition for Proprietario."""

    class Meta:
        """Meta definition for Proprietarioform."""

        model = Proprietario
        exclude = ['id']
        
        
class CorretorForm(forms.ModelForm):
    """Form definition for Corretor."""

    class Meta:
        """Meta definition for Corretorform."""

        model = Corretor
        exclude = ['id']


class ImovelForm(forms.ModelForm):
    """Form definition for Imovel."""

    class Meta:
        """Meta definition for Imovelform."""

        model = Imovel
        exclude = ['id']
        
        
class AlugarForm(forms.ModelForm):
    """Form definition for Alugar."""

    class Meta:
        """Meta definition for Alugarform."""

        model = Alugar
        exclude = ['id']


class AtendeForm(forms.ModelForm):
    """Form definition for Atende."""

    class Meta:
        """Meta definition for Atendeform."""

        model = Atende
        exclude = ['id']
        
        
class ContactarForm(forms.ModelForm):
    """Form definition for Contactar."""

    class Meta:
        """Meta definition for Contactarform."""

        model = Contactar
        exclude = ['id']