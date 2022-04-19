from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticleFrom(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Naming'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article text'
            })
        }
