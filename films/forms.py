from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['titre', 'annee', 'genre', 'image', 'commentaire', 'note']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du film'}),
            'annee': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '2024', 'min': 1888}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre du film'}),
            'commentaire': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Commentaire sur le film', 'rows': 3}),
            'note': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Note sur 5 (ex : 2,5)', 'min': 1, 'max': 5}),
        }
