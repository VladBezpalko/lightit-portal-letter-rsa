from django.db import models


class Letter(models.Model):
    message = models.TextField()
    answer = models.TextField()
    codeword = models.SlugField(unique=True)
