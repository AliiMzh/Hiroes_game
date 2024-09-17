from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class warrior(models.Model):
    name = models.CharField(max_length=32)
    hp = models.IntegerField(default="100")
    ap = models.FloatField(default=10.0)
    dp = models.FloatField(default=0.1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} ({self.user})"
