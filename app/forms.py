from .models import *
from django import forms

class EditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_pic']

class AssetForm(forms.ModelForm):
    class Meta:
        model = Assets
        fields = ('name','assetfile',)