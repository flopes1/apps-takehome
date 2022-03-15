from django.db import models


class Widget(models.Model):
    name = models.CharField(max_length=128, blank=True, null=False)
    function = models.CharField(max_length=32, blank=True, null=True)