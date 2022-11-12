from django.db import models


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    age = models.CharField(max_length=200, null=True)
    nationality = models.CharField(max_length=200)
    website = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    label = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200, null=True)


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=200)
    title = models.CharField(max_length=60)
    release_date = models.DateField(null=True,auto_now=False)
    album = models.CharField(max_length=80, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
