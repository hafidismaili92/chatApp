from django.db import models
from django.conf import settings

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Server(models.Model):
    """Server is a kind of group with same topic (for example : school topics), each server can have muliple channels (a chat room) that discuss a topic in the server (channel with math topic for example)"""

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="server_owner"
    )

    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL, related_name="server_category"
    )

    description = models.CharField(max_length=250, blank=True, null=True)

    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self) -> str:
        return self.name


class Channel(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="channel_owner"
    )
    topic = models.CharField(max_length=100)
    server = models.ForeignKey(
        Server, on_delete=models.CASCADE, related_name="channel_server"
    )

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Channel, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
