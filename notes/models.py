from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title