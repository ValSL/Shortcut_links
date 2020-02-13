from django import forms
from .models import CuttedUrl
from django.core.exceptions import ValidationError


class URLForm(forms.Form):
    url = forms.URLField(label='url')
    code = forms.CharField(max_length=5, label='code', help_text='By default, the code is auto-generated.',
                           required=False)

    def clean_code(self):
        urls = CuttedUrl.objects.all()
        codes = []
        for obj in urls:
            codes.append(obj.code)
        if self.cleaned_data['code'] in codes:
            raise ValidationError('Такой код уже существует!')
