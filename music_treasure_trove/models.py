from django.db import models

# Create your models here.

class Musician(models.Model):
    name = models.CharField(max_length=100)
    debut_year = models.DateField()
    num_stars = models.IntegerField()
# max_length required for CharField


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE) 
    title = models.CharField(max_length=100) 
    songs = models.CharField(max_length=500)
    year = models.DateField()
    filetype = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    collection = models.CharField(max_length=50)
    num_stars = models.IntegerField()
    # coverart = 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
