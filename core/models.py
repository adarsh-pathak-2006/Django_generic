from django.db import models
from django.contrib.auth.models import User

class products(models.Model):
    name=models.CharField(max_length=70)
    description=models.TextField()
    price=models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
