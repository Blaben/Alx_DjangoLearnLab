from django.db import models
from accounts.models import CustomUser
from posts.models import Post

# Create your models here.

class Notification(models.Model):
    recipient = models.ForeignKey(Post, on_delete=models.CASCADE)
    actor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    verb = models.TextField()
    target = models.ForeignKey('self')
    timestamp = models.DateTimeField(auto_now_add=True)
