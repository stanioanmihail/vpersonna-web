from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Client(models.Model):
    client_id = models.IntegerField('Client ID', blank=False)
    client_name = models.CharField('Client Name', max_length=200)
    phone_regex = RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField('Phone Number', validators=[phone_regex], blank=True, max_length=20)
    email = models.EmailField('Email', max_length=100)
    card_id_regex = RegexValidator(regex='^\\d{13}$', message='Card ID (CNP) is 13 digits left.')
    card_id = models.CharField('Card ID', validators=[card_id_regex], blank=True, max_length=20)
    address = models.CharField('Address', max_length=300)
    contract_id = models.CharField('Contract', max_length=100)
    contract_type = models.CharField('Contract Type', max_length=100)
    uname_regex = RegexValidator(regex='^[a-z0-9_]{3,16}$', message="Username contains just digits, letters and _")
    username = models.CharField('Username ', validators=[uname_regex], blank=True, max_length=20)
    password = models.CharField('Password ', blank=True, max_length=20)

