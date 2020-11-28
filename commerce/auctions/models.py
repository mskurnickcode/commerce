from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    pass


class Post(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    post_name = models.CharField(max_length=64)
    post_image = models.URLField(max_length=128)
    post_text = models.CharField(max_length=250)
    post_start_bid = models.PositiveIntegerField()
    post_date = models.DateTimeField()
    post_end_date = models.DateField()
    post_category = models.CharField(max_length=25)
    def __str__(self): 
        return self.post_name 

class bids(models.Model):
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    bid = models.PositiveIntegerField()
    bid_time = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self): 
        return self.bid_time 

class Watchlist(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
    watch_current = models.BooleanField()
    def __str__(self): 
        return self.post_id

