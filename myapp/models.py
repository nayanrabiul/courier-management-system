from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import uuid
from datetime import date, datetime
Locaton_choices = (
    ('dhaka', 'dhaka'),
    ('gazipur', 'gazipur'),
    ('mymensingh', 'mymensingh'),
    ('shariatpur', 'shariatpur'),
    ('faridpur', 'faridpur'),
    ('tangail', 'tangail'),
    ('jessore', 'jessore'),
    ('jhenaidaha', 'jhenaidaha'),
    ('magura', 'magura'),
    ('bagerhat', 'bagerhat'),
    ('khulna', 'khulna'),
    ('nowapara', 'nowapara'),
    ('shatkhira', 'shatkhira'),
    ('kushtia', 'kushtia'),
    ('kumarkhali', 'kumarkhali'),
    ('dinajpur', 'dinajpur'),
    ('pabna', 'pabna'),
    ('natore', 'natore'),
    ('rajshahi', 'rajshahi'),
    ('rangpur', 'rangpur'),
    ('sirajgang', 'sirajgang'),
    ('comilla', 'comilla'),)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_officer = models.BooleanField(default=False)
    is_disp = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(
        max_length=20, choices=Locaton_choices, default='khulna')


class Admin(models.Model):
    User = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)


class Officer(models.Model):
    User = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)


class Disp(models.Model):
    User = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)


def create_new_ref_number():
    return str(random.randint(1000000000, 9999999999))


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)

    sender_name = models.CharField(max_length=30)
    sender_email = models.EmailField()
    sender_location = models.CharField(
        max_length=20, choices=Locaton_choices, default='khulna')
    sender_phone_number = models.CharField(max_length=20)

    reciver_name = models.CharField(max_length=30)
    reciver_email = models.EmailField()
    reciver_location = models.CharField(
        max_length=20, choices=Locaton_choices, default='khulna')
    reciver_phone_number = models.CharField(max_length=20)

    product_weight_in_gram = models.FloatField()
    product_type = models.CharField(max_length=60)
    product_is_paid = models.BooleanField(default=False)
    product_is_arrived = models.BooleanField(default=False)
    product_officer = models.CharField(max_length=60)
    delivery_price = models.FloatField(default=0)
    product_date = models.DateField()
    is_retuned = models.BooleanField(default=False)
    retuned = models.BooleanField(default=False)
