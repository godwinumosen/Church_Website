from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class ChurchActivity (models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    img = models.ImageField(upload_to='images/')
    publish_date = models.DateTimeField(auto_now_add=True)
    slugs = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        ordering =['-publish_date']
    
    def __str__(self):
        return self.title
    
class Pastors (models.Model):
    pastor_name = models.CharField(max_length=250)
    pastor_img = models.ImageField(upload_to='image/')
    pastor_content = models.TextField()
    
    def __str__(self) :
        return self.pastor_name
    
class Ministries (models.Model):
    Minister_name_or_title = models.CharField(max_length=250)
    Minister_content =  models.TextField()
    Minister_img = models.ImageField(upload_to='imag/')
    Minister_publish_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-Minister_publish_date']
    def __str__(self):
        return self.Minister_name_or_title
    
class UpcomingEvent (models.Model):
    event_title = models.CharField(max_length=250)
    event_content = models.TextField()
    event_img = models.ImageField(upload_to='event_img/')
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    