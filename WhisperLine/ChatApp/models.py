from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class GroupChat(models.Model):
    group_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(User,related_name="group_chats")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_name

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name="messages")
    group = models.ForeignKey(GroupChat, on_delete=models.CASCADE,related_name="messages", blank=True,null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,related_name="private_message",blank=True,null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message From {self.sender}"
