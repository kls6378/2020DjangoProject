from django.db import models

# Create your models here.

class Card(models.Model):
    contents = models.CharField(max_length=300)
    templates = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contents +' | '+ self.templates

class TEST(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title