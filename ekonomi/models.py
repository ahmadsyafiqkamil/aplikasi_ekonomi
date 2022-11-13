from django.db import models


# Create your models here.

class Berita(models.Model):
    data = models.JSONField()
    kata_kunci = models.CharField(max_length=50, null=True, blank=True)
