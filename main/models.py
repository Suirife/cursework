from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum
from django.utils import timezone


# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    type_t = (
        ('online', "online"),
        ('offline', "offline"),
    )
    type = models.CharField(max_length=255, choices=type_t, default="offline")
    status_t = (
        ('active', "active"),
        ('completed', "completed"),
        ('cancelled', "cancelled"),
    )
    status = models.CharField(max_length=255, choices=status_t, default="active")


class OrderReport(models.Model):
    data = models.DateTimeField(default=timezone.now)
    total_orders = models.IntegerField(default=0)
    total_cost = models.FloatField(default=0)

    def update(self):
        orders = Orders.objects.filter(completed_at__date=self.data.date(), status='completed')
        total_orders = orders.count()
        total_cost = orders.aggregate(total_cost=Sum('orderitems__cost'))['total_cost'] or 0

        self.total_orders = total_orders
        self.total_cost = total_cost
        self.save()


class OrderItems(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    count = models.IntegerField()
    discount = models.FloatField(default=0)
    cost = models.FloatField(default=0)

    def clean(self):
        if self.count > self.product_id.stock:
            raise ValidationError('Count must be less than stock')

    def save(self, *args, **kwargs):
        self.clean()
        self.cost = self.count * self.product_id.price * (1 - self.discount)
        super(OrderItems, self).save(*args, **kwargs)


# Регистрируем сигнал после определения класса OrderItems
@receiver(post_save, sender=OrderItems)
def update_product_stock(sender, instance, **kwargs):
    if instance.order_id.status != 'cancelled':
        product = instance.product_id
        product.stock -= instance.count
        product.save()


@receiver(post_save, sender=OrderItems)
def update_order_report(sender, instance, **kwargs):
    instance.order.report.update()


# Регистрируем сигнал после определения класса OrderItems
@receiver(pre_save, sender=Orders)
def revert_stock_on_cancel(sender, instance, **kwargs):
    if instance.pk:
        original_order = Orders.objects.get(pk=instance.pk)
        if original_order.status != 'cancelled' and instance.status == 'cancelled':
            order_items = OrderItems.objects.filter(order_id=instance)
            for order_item in order_items:
                product = order_item.product_id
                product.stock += order_item.count
                product.save()
