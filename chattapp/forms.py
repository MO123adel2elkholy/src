from django import forms
from .models import ChattMessage


class ChattMessageForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
                           'class': 'form-control bg-dark', 'rows': 3, "placeholder": "type your Messeges"}))

    class Meta:
        model = ChattMessage
        fields = ['body']
