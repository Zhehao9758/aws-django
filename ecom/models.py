from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField()
    image = models.FilePathField(path='/img')
    detail = models.TextField()


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
