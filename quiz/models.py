from django.db import models

# Create your models here.
class Quiz(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    answer=models.IntegerField()

class Player_info(models.Model):
    number = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    age=models.IntegerField()
    nation=models.CharField(max_length=20)
    team=models.CharField(max_length=30)
    value=models.CharField(max_length=30)

class Player_name(models.Model):
    name=models.CharField(max_length=20)