from django.contrib import admin
from .models import *
# Register your models here.


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name','location']
    list_filter = ['location__state','location__city']
    search_fields = ['location__state','location__address','products__name','products__sku']

admin.site.register(Warehouse,WarehouseAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','sku','quantity']
    list_filter = ['quantity']
    search_fields = ['sku','name']

admin.site.register(Product,ProductAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ['address','city','state']
    list_filter = ['city','state']
    search_fields = ['city','state','address']

admin.site.register(Location,LocationAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display =  ['user','phone_number']

admin.site.register(Profile,ProfileAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'user', 'date_added']
    list_filter = ['date_added', 'tracking', 'payment_method']
    search_fields = ['items', 'user__email', 'invoice','location']


admin.site.register(Order,OrderAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ['product','quantity','total','pick_up_from']
    list_filter = ['date_added']
    search_fields = ['product']

admin.site.register(Item,ItemAdmin)

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['location','status']
    list_filter = ['location']

admin.site.register(Delivery,DeliveryAdmin)