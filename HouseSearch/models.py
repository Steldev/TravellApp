from django.db import models
from django.contrib.auth.models import User
from model_utils import Choices


class House(models.Model):
    PRIVATE_HOUSE = 'PH'
    APARTMENT = 'AP'
    HOUSE_TYPE = Choices(
        (PRIVATE_HOUSE, 'Private house'),
        (APARTMENT, 'Apartment'),
    )

    user = models.ForeignKey(User, on_delete='Cascade')
    country = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    type = models.CharField(max_length=2, choices=HOUSE_TYPE, default=PRIVATE_HOUSE)
    rooms = models.SmallIntegerField(default=1)
    sleeper = models.SmallIntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=10)


class HousePhoto(models.Model):
    house = models.ForeignKey(House, on_delete='Cascade')
    photo = models.ImageField(upload_to='house_data/photo/')
