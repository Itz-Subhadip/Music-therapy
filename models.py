from django.db import models

# Create your models here.

class Musician(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=150)
    tag = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    Artist = models.CharField(max_length=100)
    song = models.FileField(upload_to='song')
    
def __str__(self):
    return self.name
