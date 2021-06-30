from django.contrib.auth import get_user_model
from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=64)
    rater = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name
