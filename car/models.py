from django.db import models


# Create your models here.
class Car(models.Model):
    code = models.CharField(max_length=16)
    name = models.CharField(max_length=32)
    sale_date = models.DateField('date of sale')
    # owner = models.ForeignKey(Person, on_delete=models.PROTECT)


class Person(models.Model):
    id = models.IntegerField
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE)

    def print_car(self):
        print('my car is (code=' + self.car.code + ', name=' + self.car.name + ')')
