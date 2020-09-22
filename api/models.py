from django.db import models
from django.conf import settings

# Create your models here.
class Burger(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='burgers')

    def __str__(self):
        return self.title
    