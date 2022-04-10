from django.db import models

# AUTH_USER_MODEL = 'django_facebook.FacebookCustomUser'
# AUTH_PROFILE_MODULE = 'django_facebook.FacebookProfile'

# Create your models here.
class Event(models.Model):
    title = models.TextField(max_length=250)
    location = models.TextField(max_length=100)
    more_info = models.TextField(max_length=100)
    days = models.TextField(max_length=100)
    month = models.TextField(max_length=100)
    day_of_week = models.TextField(max_length=100)
    dates_duration = models.TextField(max_length=100)
    
    
class Sermon(models.Model):
    title = models.TextField(max_length=200)
    source = models.TextField(max_length=100, default="FaceBook")
    description = models.TextField(max_length=600)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "myapp_image"
    