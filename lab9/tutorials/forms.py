from django import forms
from .models import Tutorial

class UploadFileForm(forms.ModelForm):
     class Meta:
            fields = (
                  'title',
                  'description',
                  'upload',
                )