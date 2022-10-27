from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from storage import ImageStorage
# Create your models here.


cover = models.ImageField(verbose_name='上传图片', upload_to='article/%Y/%m/%d', storage=ImageStorage())
class Img(models.Model):
    img_url = models.ImageField(verbose_name="现场照片",upload_to='image_upload_to')
    project_id = models.ForeignKey(verbose_name="项目名称",to='Order',default=1,on_delete=models.CASCADE)


class Wallpaper(models.Model):
    imagNAME = models.CharField(max_length=200)
    imagSRC = models.CharField(max_length=200)
    imagTAGS = models.CharField(max_length=200)
    
    def __str__(self):
        return self.imagNAME

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username

class Rating(models.Model):
    username = models.CharField(max_length=100)
    imagNAME =models.CharField(max_length=200)
    rating = models.IntegerField()

    def __str__(self):
        return self.username

