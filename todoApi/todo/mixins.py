from django.db import models
from django.contrib.auth.models import AbstractUser


class TodoMixins(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AbstractUserMixin(AbstractUser):
    pass
