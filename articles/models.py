from django.db import models

class Article(models.Model):
    headline = models.CharField(max_length=300)
    image = models.URLField()
    author = models.CharField(max_length=100)
    copy = models.TextField()

    def __str__(self):
        return self.headline