from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    person_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.EmailField()
    contact = models.CharField(max_length=70)
    desc = models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.name





class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    tags = models.CharField(max_length=100)
    image = models.CharField(max_length=100000, default="")
    song = models.FileField(upload_to='images')
    movie = models.CharField(max_length=1000, default="")
    credit = models.CharField(max_length=100000, default="")

    def __str__(self):
        return self.name

class Watchlater(models.Model):
    watch_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=10000000, default="")

class History(models.Model):
    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_id = models.CharField(max_length=10000000, default="")

class Channel(models.Model):
    channel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    music = models.CharField(max_length=100000000)
# Create your models here.
