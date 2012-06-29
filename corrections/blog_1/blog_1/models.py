from django.db import models

class Post(models.Model):
    titre = models.CharField(max_length=255) # remarque: pas oublier que c'est la taille maximum d'un string si vous utilisez mysql (mais pas postgresql)
    content = models.TextField()
