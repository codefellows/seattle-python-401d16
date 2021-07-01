from django.contrib.auth import get_user_model
from django.db import models


class Sweet(models.Model):
    name = models.CharField(max_length=256)
    purchaser = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    amount = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return self.name
