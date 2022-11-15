from django.db import models
from django.db.models.fields import DateTimeField

import datetime
Now=datetime.datetime.now()
week=datetime.timedelta(days=7)
# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    email_address = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=10)
    home_address = models.CharField(max_length=100, blank=True, null=True)
    currently_borrowed = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'

class Catalogue(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    book_isbn = models.CharField(max_length=13)
    author_name = models.CharField(max_length=60)
    day_of_addition = models.DateField()
    genre = models.CharField(max_length=40, blank=True, null=True)
    edition = models.IntegerField()
    times_borrowed = models.IntegerField(blank=True, null=True)
    min_age = models.IntegerField(blank=True, null=True)
    currently_borrowed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogue'


class Issue(models.Model):
    issue_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Catalogue, models.DO_NOTHING)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    staff = models.ForeignKey('Staff', models.DO_NOTHING)
    issue_date = models.DateTimeField(default=Now,blank=True, null=True)
    return_by = models.DateTimeField(default=Now+week,blank=True,null=True)
    current_status = models.IntegerField(default=0)
    fine = models.IntegerField(default=0,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issue'

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    prev_exp = models.IntegerField(blank=True, null=True)
    joining_date = models.DateField()
    phone_number = models.CharField(max_length=10)
    email_address = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'
