from django.db import models

# Create your models here.

class Film(models.Model):
    titre = models.CharField(max_length=100)
    annee = models.IntegerField()
    genre = models.CharField(max_length=50)
    image = models.ImageField(upload_to='covers/', null=True, blank=True)
    note = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    commentaire = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.titre} ({self.annee})"
