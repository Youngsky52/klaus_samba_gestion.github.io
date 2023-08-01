from django.db import models

# Create your models here.
class Etudiant(models.Model):

    nom = models.CharField(max_length=70)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(max_length=1, default='M')
    age = models.IntegerField(default='12')
    email = models.EmailField(default='@gmail.com')
    tel = models.CharField(max_length=22, default='+24206...')