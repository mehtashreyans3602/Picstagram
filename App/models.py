from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EditProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='profile_images/',default='profile_images/user-default.png')
    bio = models.TextField(null=True,blank=True)
    phoneNo = models.CharField(null=True,blank=True,max_length=10)
    gender = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=False,default=None)
    image = models.ImageField(upload_to='post/', null=True)
    caption = models.TextField(default='hello', null=True, blank=True)
    

    def __str__(self):
        return str(self.author)

class Followers(models.Model):
    follower = models.CharField(max_length=1000)
    user = models.CharField(max_length=1000)

    def __str__(self):
        return self.user