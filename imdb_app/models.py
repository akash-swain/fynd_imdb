from django.db import models

# Create your models here.
class Genre(models.Model):
    """
    Model to store Genre
    """
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name



class Movie(models.Model):
    """
    Model to store movies
    """
    name = models.CharField(max_length=200, unique=True)
    director = models.CharField(max_length=100, default="<...To be set later...>")
    imdb_score = models.FloatField(default=0)
    popularity = models.FloatField(default=0)
    genre = models.ManyToManyField(Genre, default="<...To be set later...>")

    def __str__(self):
        return self.name
