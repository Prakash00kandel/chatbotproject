from django.db import models

sub_choices = [
    ('BScCSIT', 'BScCSIT'),
    ('BIT', 'BIT')
]


# Create your models here.
class Messages(models.Model):
    user_input = models.TextField()
    reply = models.TextField()

    def __str__(self):
        return self.user_input


class UserInfo(models.Model):
    name = models.CharField(max_length=122)
    phone_number = models.PositiveIntegerField()
    desired_sub = models.CharField(max_length=25, choices=sub_choices)
    notes = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
