from django import forms
from django.forms import ModelForm
from .models import Artist, Song
from crispy_forms.helper import FormHelper

class ArtistForm(forms.ModelForm):
    class Meta:
        Model = Artist
        fields = "__all__"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = "__all__"
        
        def __init__(self, *args, **kwargs):
            self.helper = FormHelper()
            self.helper.form_method = 'POST'

        