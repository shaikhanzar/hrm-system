from django.db import models
from accounts.models import User

class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    status = models.CharField(
        max_length=20,
        default="Pending"
    )