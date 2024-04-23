from django import forms

from catalog.models import Product

forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name_prod(self):
        cleaned_data = self.cleaned_data.get('name_prod').split()
        for data in cleaned_data:
            if data in forbidden_words:
                raise forms.ValidationError('Ошибка! В тексте недопустимые слова')

        cleaned_data = " ".join(cleaned_data)
        return cleaned_data

    def clean_description_prod(self):
        cleaned_data = self.cleaned_data.get('description_prod').split()
        for data in cleaned_data:
            if data in forbidden_words:
                raise forms.ValidationError('Ошибка! В тексте недопустимые слова')

        cleaned_data = " ".join(cleaned_data)
        return cleaned_data
