from django.conf import settings
from django.db import models

# Create your models here.
from catalog.models import ItemAmount


class OrderItem(ItemAmount):
    order = models.ForeignKey('order', on_delete=models.CASCADE, related_name='order_items')


class Order(models.Model):
    #payment = models.CharField(max_length=50)
    #delivery_date = models.DateField()
    #email = models.EmailField()
    #tel = models.SlugField()

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items)