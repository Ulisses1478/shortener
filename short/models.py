from django.db import models

class Shortener(models.Model):
    link = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
