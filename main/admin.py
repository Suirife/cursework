from django.contrib import admin
from .models import Users, Products, Orders, OrderItems
# Register your models here.

admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(OrderItems)
