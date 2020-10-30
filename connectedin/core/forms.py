from django import forms

class PerfilForm(forms.Form):
    """PerfilForm definition."""

    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    senha = forms.CharField(required=True)
    nome = forms.CharField(required=True)
    data_nascimento = forms.DateField(required=True)