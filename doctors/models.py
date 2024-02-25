from django.db import models


# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField("accounts.CustomUser", on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=255)
