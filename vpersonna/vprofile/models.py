from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Client(models.Model):
    id = models.IntegerField('Client ID', blank=False, primary_key=True)
    name = models.CharField('Client Name', max_length=200)
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
    def __str__(self):
        return self.name + "(" + self.email + ")" 

class ServiceType(models.Model):
    #service_id = models.IntegerField('Service id', blank=False, primary_key=True)
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField('Service name', blank=False, max_length=25)
    def __str__(self):
        return self.service_name

class Rule(models.Model):
    #rule_id = models.IntegerField('Rule id', blank=False, primary_key=True)
    rule_id = models.AutoField(primary_key=True)
    type_of_service = models.ForeignKey(ServiceType) 
    client = models.ForeignKey(Client)
    #client = models.IntegerField(blank=False)
    bandwidth_percent = models.PositiveIntegerField('Bandwidth Percent', blank=False)
    destination_address = models.CharField('Destination URL', blank=True, max_length='200')

class Offer(models.Model):
    offer_id = models.AutoField(primary_key=True)
    offer_name = models.CharField('Offer Name', blank=False, max_length=25)
    offer_description = models.CharField('Offer description', blank=True, max_length=25)
    offer_short_description = models.CharField('Offer short description', blank=True, max_length=200)
    cost_per_min = models.PositiveIntegerField('Cost per minute', blank=False)
    def __str__(self):
        return self.offer_name

#New tables:
class SiteAccess(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField('Site URL', blank=True, max_length=25)
    ip_regex = RegexValidator(regex='^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', message='IP format A.B.C.D')
    ip_addr = models.CharField('IP address ', validators=[ip_regex], blank=False, max_length=20)
    num_accesses = models.PositiveIntegerField('Number of accesses', blank=False)

class ServiceUtilizationStatistics(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client)
    service = models.ForeignKey(ServiceType)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    num_accesses = models.PositiveIntegerField('Number of accesses', blank=False)

class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client)
    description = models.CharField('Action Description', blank=False, max_length=100)
