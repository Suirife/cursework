from django.shortcuts import render
from django.views import generic
from .models import Products, Orders, OrderItems, Users


# Create your views here.


def index(request):
    products_count = Products.objects.all().count()
    orders_count = Orders.objects.all().count()
    order_items_count = OrderItems.objects.all().count()
    users_count = Users.objects.all().count()
    products_list = Products.objects.all()

    context = {
        'products_list': products_list,
        'products_count': products_count,
        'orders_count': orders_count,
        'order_items_count': order_items_count,
        'users_count': users_count
    }

    return render(request, 'index.html', context=context)

