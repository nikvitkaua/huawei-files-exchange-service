from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass


class File(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False, blank=False)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
