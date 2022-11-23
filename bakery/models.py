from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    point_five = models.DecimalField(max_digits=10, decimal_places=2)
    one = models.DecimalField(max_digits=10, decimal_places=2)
    one_point_five = models.DecimalField(max_digits=10, decimal_places=2)
    two = models.DecimalField(max_digits=10, decimal_places=2)
    twe_point_five = models.DecimalField(max_digits=10, decimal_places=2)
    three = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) :
        return self.name

class Flavour(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name