from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

current_user = get_user_model()


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, related_name='creator', on_delete=models.CASCADE, default=current_user)
    members = models.ManyToManyField(User, related_name='group_member')

    def __str__(self):
        return self.name
