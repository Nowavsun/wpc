from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class wallpaper(models.Model):
    imagNAME = models.CharField(max_length=200)
    imagSRC = models.CharField(max_length=200)
    imagTAGS = models.CharField(max_length=200)
    
    def __str__(self):
        return self.imagNAME

