# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class PhotoMetaData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to=str(user), null=True)
    placeLat = models.FloatField(null=True, help_text='Latitude of place')
    placeLong = models.FloatField(null=True, help_text='Longitude of place')
    placeName = models.TextField(null=True, max_length=512, help_text='Address of place')
    camera = models.TextField(null=True, max_length=255, help_text='Camera model')
    shootDate = models.DateTimeField(null=True, help_text='Date when photo was taken')

    class Meta:
        ordering = ['shootDate']


class Tags(models.Model):
    photo = models.ForeignKey('PhotoMetaData', on_delete=models.CASCADE)
    name = models.TextField(null=False, max_length=20)

    def __str__(self):
        return self.name
