from django import forms

from UserProfile.models import *


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['user', 'date_public']

        widgets = {
            'text': forms.Textarea,
        }


class AttachmentForm(forms.Form):
    files = forms.ImageField(
        widget=forms.FileInput(attrs={'name': 'photo',
                                      'multiple': True,
                                      'accept': 'image/*'})
    )
