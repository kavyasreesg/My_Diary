from django.db import models


# Create your models here.

class ActivityData(models.Model):
    text_from_user = models.CharField(max_length=1000)
