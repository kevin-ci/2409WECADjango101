from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=150)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lists"
    )

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    parent_list = models.ForeignKey(
        List, on_delete=models.CASCADE, related_name="items"
    )
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name