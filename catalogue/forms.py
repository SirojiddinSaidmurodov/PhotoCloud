from django.forms import forms

from catalogue.models import PhotoMetaData


class UploadForm(forms.Form):
    photo = forms.FileField(help_text='image')

    class Meta:
        model = PhotoMetaData
        fields = ('photo',)
