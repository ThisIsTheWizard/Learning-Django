from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="profile")
    mobile = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return f"{self.user}"
