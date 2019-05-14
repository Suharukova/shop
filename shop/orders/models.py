from django.conf import settings
from django.db import models

# Create your models here.
from catalog.models import ItemAmount


class OrderItem(ItemAmount):
    order = models.ForeignKey('order', on_delete=models.CASCADE, related_name='order_items')


class Order(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payment = models.CharField(max_length=50, null=True)
    delivery_date = models.DateField(null=True)
    email = models.EmailField(null=True)
    tel = models.CharField(max_length=20, null=True)

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items)