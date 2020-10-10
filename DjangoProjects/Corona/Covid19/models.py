from django.db import models

# Create your models here.

class Patients(models.Model):
    P_name = models.CharField(max_length=50)
    P_age = models.IntegerField(null = False)
    P_email = models.EmailField()

    def __str__(self):
        return self.P_name