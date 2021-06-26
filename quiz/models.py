from django.db import models

# Create your models here.
class Quiz(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    answer=models.IntegerField()

class Player_info(models.Model):
    number = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    age=models.IntegerField()
    nation=models.CharField(max_length=50)
    team=models.CharField(max_length=50)
    value=models.CharField(max_length=50)
    photo=models.URLField(null=True, blank=True)

class Player_name(models.Model):
    name=models.CharField(max_length=50)