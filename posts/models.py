from django.db import models

# Create your models here.
# Data Bases deal with classes
class post(models.Model):
    text = models.TextField(default='Input text here')

# post is the new database model
# text is the data base field and type to hold the textfield
    def __str__(self):
        return self.text[:50]
