from django import forms
from django.utils.translation import ugettext_lazy

from .models import Product


class ProductAddForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = [""]
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
