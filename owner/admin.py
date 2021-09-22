from django.contrib import admin
from owner.models import Order,Book

# Register your models here.
admin.site.register(Book)
admin.site.register(Order)
