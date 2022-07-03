from django.db import models

# Create your models here.


class Part(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    weight_ounces = models.IntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "part"
