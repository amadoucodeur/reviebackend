from django.db import models
from django.contrib.auth import get_user_model

class Chat(models.Model):
    participants = models.ManyToManyField(get_user_model())

class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')

class Media(models.Model):
    image = models.ImageField(upload_to='chat_medias/')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='medias', null=True, blank=True)
