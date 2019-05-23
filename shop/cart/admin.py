from django.contrib import admin

# Register your models here.
from django.contrib.admin import TabularInline

from cart.models import Cart


@admin.register(Cart)#==damin.site.register(Cart) вместо пустого класса
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']

    def username(self, cart):
        return cart.user.username if cart.user is not None else '- Unknown -'