from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title