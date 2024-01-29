# messaging_app/forms.py
from django import forms
from .models import Message, Comment

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
