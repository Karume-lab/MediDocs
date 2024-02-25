from django.db import models
from utils.departments import get_departments


# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(
        "accounts.CustomUser", on_delete=models.CASCADE, primary_key=True
    )
    department = models.CharField(
        max_length=3,
        choices=get_departments(),
        default="UN",
        blank=True,
        null=True,
    )

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    def __str__(self):
        return "DR. {} {}".format(self.user.first_name, self.user.last_name)
