from django.db import models
from django.contrib.auth.models import User
from model_utils import Choices


class UserInfo(models.Model):

    TRAVEL = 'TR'
    SEARCH = 'SH'
    RENT_HOUSE = 'HH'
    STATUS_TYPE = Choices(
        (TRAVEL, 'Travelling'),
        (SEARCH, 'Find house'),
        (RENT_HOUSE, 'Rent a house'),
    )

    user = models.OneToOneField(User,
                                unique=True,
                                on_delete='Cascade')
    gender = models.BooleanField(default=False)
    birthday = models.DateField(blank=True)
    status = models.CharField(max_length=2,
                              choices=STATUS_TYPE,
                              blank=True,
                              default=TRAVEL)

    phone_num = models.CharField(max_length=12,
                                 blank=True)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30,
                            blank=True)
    info = models.TextField(max_length=256,
                            blank=True)

    registration = models.DateField(auto_now_add=True)
    last_visit = models.DateTimeField(auto_now=True)
    big_photo = models.ImageField(upload_to='user_photo/',
                                  blank=True,
                                  default='def_user_photo.png')

class Note(models.Model):
    user = models.ForeignKey(User, on_delete='Cascade')
    text = models.TextField(max_length=1000, blank=True)
    date_public = models.DateTimeField(auto_now_add=True)


def get_upload_file_way(type):
    return 'user_files/%s/' % type

class Attachment(models.Model):
    FILE_TYPE = (
        ('IM', 'фото'),
        ('VD', 'видео'),
        ('AU', 'аудио'),
        ('FL', 'файл'),
    )

    note = models.ForeignKey(Note, on_delete='Cascade')
    type = models.CharField(max_length=2,
                            choices=FILE_TYPE)
    file = models.FileField(upload_to='user_files/%s/' % 'img')
