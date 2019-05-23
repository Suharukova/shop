from django.contrib import admin

# Register your models here.
from cart import models
from cart.models import Cart


class CartItemInline(admin.TabularInline):
    model = models.CartItem
    extra = 0
    list_display = ['item', 'amount']


@admin.register(Cart)#==damin.site.register(Cart) вместо пустого класса
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_filter = ['user__username']
    inlines = [CartItemInline]
    actions = ['remove_all']

    def username(self, cart):
        return cart.user.username if cart.user is not None else '- Unknown -'

    def remove_all(self, request, queryset):
        for cart in queryset:
            item = cart.items.all().delete()
    #remove_all.short_description = 'Remove AlL'

