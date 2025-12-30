from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# username, password, f_name, l_name, age
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True) # optional
