from django import forms
from django.utils.translation import ugettext_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Product


class ProductAddForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']
        help_texts = {
            'name': None,
            'description': None,
            'price': None,
            'category': None,
        }
        labels = {
            'name': ugettext_lazy('Укажите название товара'),
            'description': ugettext_lazy('Укажите описание товара'),
            'price': ugettext_lazy('Укажите цену товара'),
            'category': ugettext_lazy('Выберите категорию для товара'),
        }


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_texts = {
            'username': None,
        }
        labels = {
            'username': ugettext_lazy('Имя пользователя'),
            'email': ugettext_lazy('e-mail'),
            'password1': ugettext_lazy('Введите пароль'),
            'password2': ugettext_lazy('Повторите пароль'),
        }
