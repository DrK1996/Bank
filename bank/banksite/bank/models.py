
from django.db import models

class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=50)
    # slug = models.SlugField(unique=True,default="default-slug")
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
