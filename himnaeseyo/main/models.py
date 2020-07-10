from django.db import models

# Create your models here.

class Photo(models.Model):
    filename = models.CharField(max_length=100)
    path = models.CharField(max_length=100)

    def __str__(self):
        return self.filename
