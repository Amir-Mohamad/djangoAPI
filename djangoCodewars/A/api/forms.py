from django import forms
from .models import GithubModel


class GithubForm(forms.ModelForm):
    class Meta:
        model = GithubModel
        fields = ('username',)
