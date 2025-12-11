from django import forms
from .models import Imovel
from django.contrib.auth.forms import UserCreationForm
# Este formulário é pronto para criar um novo usuário com username e password



class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = ['titulo', 'descricao', 'preco', 'foto_principal', 'disponivel', 'corretor']
