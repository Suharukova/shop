from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class ItemAmount(models.Model):
    class Meta:
        abstract = True

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='+')
    amount = models.PositiveIntegerField()

    @property
    def total_price(self):
        return self.amount * self.item.price