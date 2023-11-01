from django.db import models
from django.utils import timezone

class Film (models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    release_date = models.DateField()
    photo = models.ImageField(blank=True, null = True,)
    storyline = models.TextField()
    viewing_date = models.DateTimeField(default=timezone.now)
    rating = models.DecimalField(decimal_places=10, max_digits=1)

    def release(self):
        self.release_date = timezone.now()

    def __str__(self):
        return self.title
    
