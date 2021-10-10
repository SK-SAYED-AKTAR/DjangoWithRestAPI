from django.db import models

# Create your models here.

class StudentClass(models.Model):
    name = models.CharField(max_length=10)
    roll = models.IntegerField()
    
    def __str__(self):
        return str(self.name)