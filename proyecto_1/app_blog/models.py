from django.db import models
import datetime
from datetime import datetime
#from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Comentario(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField()
    due_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Ranking(models.Model):
    name_course = models.CharField(max_length=30)
    opinion = models.TextField()
    score = models.IntegerField()
    

    def __str__(self):
        return self.name_course