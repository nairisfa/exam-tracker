from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    grade = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    description = models.TextField()

