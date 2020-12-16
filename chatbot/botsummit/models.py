from django.db import models

# Create your models here.
class Messages(models.Model):
    user_input = models.TextField()
    reply = models.TextField()

    def __str__(self):
        return self.user_input