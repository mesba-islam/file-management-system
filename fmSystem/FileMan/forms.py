from django.forms import ModelForm
from .models import UploadFile


class FileForm(ModelForm):
    class Meta:
        model= UploadFile
        fields = ['title', 'file','description', 'important']