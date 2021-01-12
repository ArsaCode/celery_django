from django import forms
from django.utils.safestring import mark_safe
from todolist.models import Todo

class AddForm(forms.ModelForm):
    content = forms.CharField(
        label=mark_safe("<strong>Content</strong>"),
        min_length=5,
        max_length=255,
        widget=forms.TextInput
        (attrs={'class':'form-control',
            'placeholder':'Create an awesome thing'
        }))

    class Meta:
        model = Todo
        fields = ["content"]