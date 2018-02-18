from django.contrib import admin
from .models import *


class StatusAdmin(admin.ModelAdmin):
    #list_display = ['name','email']
    list_display = [ field.name for field in Status._meta.fields]
    #inlines = [FieldMappingInline]
    #fields = []
    #exclude = []
    #list_filter = ['name']
    #search_fields = ['name', 'email']

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]


    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder


admin.site.register(ProductInOrder, ProductInOrderAdmin)


class _ProductInBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInBasket


admin.site.register(ProductInBasket, _ProductInBasketAdmin)