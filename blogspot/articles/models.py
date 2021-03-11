from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
    thumb = models.ImageField(default= 'default.png', blank= True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

# Everytime we make changes in the models, 
# we have to run the following commands to reflect the changes in the database
# 1. python manage.py makemigrations
# 2. python manage.py migrate

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100] + "..."
