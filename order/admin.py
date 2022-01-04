from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','order_payment_id','isPaid']

class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order','product','count','size']


admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemsAdmin)
