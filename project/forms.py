from django import forms

from project.models import Product, Version

WORDS_BLACKLIST = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно',
                   'обман', 'полиция', 'радар')

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'actual_version_indicator':
                field.widget.attrs['class'] = 'form-control'
            elif not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
            else:
                field.widget.attrs['class'] = 'form-check-input'


class ProductAddForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('updated_by', 'owner', 'published')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        if cleaned_data in WORDS_BLACKLIST:
            raise forms.ValidationError('У-пс, название товара в списке запрещённых товаров')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        if cleaned_data in WORDS_BLACKLIST:
            raise forms.ValidationError('У-пс, описание товара содержит запрещённые слова')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'version_number', 'name_of_version', 'actual_version_indicator')


class ProductManagerForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'published')