from django import forms
from .models import NewsLetterSub


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetterSub
        fields = ['email', ]
