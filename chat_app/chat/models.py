from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(User,related_name='chatromms')

class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom,on_delete=models.CASCADE)
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

