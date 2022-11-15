from django.contrib import admin

from .models import Customer,Issue
# Register your models here.

admin.site.register(Customer)
admin.site.register(Issue)
