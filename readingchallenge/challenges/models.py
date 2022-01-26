from django.db import models
from django import forms
from django.contrib.auth import get_user_model

from readingchallenge import challenges

# Create your models here.

class Challenge(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey (
        get_user_model(),
    )
    pitch = models.CharField(max_length=200)
    description = models.TextField(default="")
    website = models.URLField()
    image_url = models.ImageField()
    date_created = models.DateTimeField()
    deadline = models.DateTimeField()

    class Meta:
        ordering = ["date_created"]

#  create a Challenge Form model to store its structure 
class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = (
            'title', 'author', 'pitch', 'description', 'website', 'image_url', 'deadline'
        )
    
#  how do we store the tasks from the front end?