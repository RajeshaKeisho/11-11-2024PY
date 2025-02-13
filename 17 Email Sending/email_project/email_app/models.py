from django.db import models

class FormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    attachment = models.FileField(upload_to='attachments/')

