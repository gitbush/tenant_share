from django import forms
from .models import ChatMessage

class MessageForm(forms.ModelForm):
    """
    Chat message form for new message
    """
    class Meta:
        model = ChatMessage
        fields = ['message']
        widgets = {
          'message': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }