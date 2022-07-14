from xml.dom.minidom import AttributeList
from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ManyToManyField("Artist", related_name="albums", null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"