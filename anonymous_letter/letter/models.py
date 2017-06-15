from django.db import models


class Letter(models.Model):
    message = models.TextField()
    response = models.TextField()
