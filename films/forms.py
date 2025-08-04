from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['titre', 'annee', 'genre', 'image']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du film'}),
            'annee': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '2024', 'min': 1888}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre du film'}),
            # 'image' : forms.ImageField(attrs={'class': 'form-control', 'placeholder': 'Covers du film'}),
        }
