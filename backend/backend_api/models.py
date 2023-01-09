from django.db import models

class User(models.Model):
    ROLE = (
        ('admin', 'Admin'),
        ('user', 'User')
    )

    role = models.CharField(max_length=5, choices=ROLE, default=ROLE[1][0])
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_date = models.DateField()
    imdb = models.FloatField(default=0.0)

class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)