from django.contrib import admin
from .models import Users, Products, Orders, OrderItems, OrderReport
from django.urls import path
from django.shortcuts import render


# Register your models here.

class OrderReportAdmin(admin.ModelAdmin):
    list_display = ('data', 'total_orders', 'total_cost')
    readonly_fields = ('data', 'total_orders', 'total_cost')
    search_fields = ('date',)
    date_hierarchy = 'data'


admin.site.register(OrderReport, OrderReportAdmin)
admin.site.register(Users)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(OrderItems)
