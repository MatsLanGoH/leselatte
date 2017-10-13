from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    page_count = models.IntegerField()
    authors = ArrayField(models.CharField(max_length=50))

