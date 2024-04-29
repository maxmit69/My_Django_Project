from django import forms

from catalog.models import Product, Category, Blog, Version

forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
            if isinstance(self.fields[field], forms.BooleanField):
                self.fields[field].widget.attrs = {'class': 'form-check-input'}


class ProductForm(StyleFormMixin, forms.ModelForm):
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


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('heading', 'content', 'image',)


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('version_name', 'version_number', 'product', 'indicates_current_version',)
