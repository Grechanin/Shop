from  django.contrib.auth.models import User
from django.db import models
from products.models import Product
from django.db.models.signals import post_save


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статуси замовлення'


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#total price for all products in order
    email = models.EmailField()
    phone = models.CharField(max_length=64, blank=True, null=True, default=None)
    address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return "User_%s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_pre_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "User %s" % self.product.name

    class Meta:
        verbose_name = 'Товар в замовленні'
        verbose_name_plural = 'Товари в замовлення'

    def save(self, *args, **kwargs):
        price_pre_item = self.product.price
        self.price_pre_item = price_pre_item
        self.total_price = int(self.nmb) * price_pre_item
        super(ProductInOrder, self).save(*args, **kwargs)


def post_save_product_in_order(sender, instance, created, *args, **kwargs):
    all_products_in_order = ProductInOrder.objects.filter(order=instance.order, is_active=True)
    order_total_price = 0
    for product in all_products_in_order:
        order_total_price += product.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(post_save_product_in_order, sender=ProductInOrder)


class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_pre_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Товар в корзині'
        verbose_name_plural = 'Товари в корзині'

    def save(self, *args, **kwargs):
        price_pre_item = self.product.price
        self.price_pre_item = price_pre_item
        self.total_price = int(self.nmb) * price_pre_item
        super(ProductInBasket, self).save(*args, **kwargs)