from django.db import models

class Customer_info(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    key = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.full_name

