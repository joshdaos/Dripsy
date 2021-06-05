from django.db import models

from django.db.models import Model, CharField, TextField
from django.db.models.fields.related import ForeignKey

# import user model from built in auth
from django.contrib.auth.models import User

# Create your models here.

class SellerProfile(Model):

    name = CharField(max_length=100)
    bio = TextField(max_length=500)
    image = CharField(max_length=500)
    user = ForeignKey(User, on_delete=models.CASCADE, related_name="seller")

    def __str__(self):
        return self.name


class SellersFollowed(Model):

    user = ForeignKey(User, on_delete=models.CASCADE, related_name="follows")
    seller = ForeignKey(SellerProfile, on_delete=models.CASCADE, related_name="followers")


class Product(Model):

    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    CLOTHING = 'Merch'

    name = CharField(max_length=200, default=CLOTHING)
    sku = CharField(max_length=6)
    description = TextField(max_length=350)
    size_choices = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]
    size = CharField(
        max_length=200,
        choices=size_choices,
        default=SMALL,
    )
    image = CharField(max_length=500)
    seller = ForeignKey(SellerProfile, on_delete=models.CASCADE, related_name="products")

    

