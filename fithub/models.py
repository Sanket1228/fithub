from django.db import models

class Registration(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    DOB = models.DateField()
    gender = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=10)
    fitness_level = models.CharField(max_length=10)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    bmi = models.CharField(max_length=10)
    fat_per = models.CharField(max_length=10)

    def __str__(self):
        return self.product_name