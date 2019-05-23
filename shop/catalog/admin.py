from django.contrib import admin

# Register your models here.
from catalog import models
from catalog.models import Item


class ItemPriceFilter(admin.SimpleListFilter):
    title = 'price'
    parameter_name = 'price'
    def lookups(self, request, model_admin):
        return [('0-10', '0 - 10'),
                ('10-50', '10 - 50'),
                ('50-', '50 - 100'),
                ]

    def queryset(self, request, queryset):
        price_range = self.value()
        price_ranges = {
            '0-10': {'price__lte': 10},
            '10-50': {'price__gt': 50, 'price__lte': 10},
            '50-': {'price__gt': 50}
        }
        return queryset.filter(**price_ranges.get(price_range, {}))

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count']
    list_filter = [ItemPriceFilter, 'count']
    #fields = ['name', 'price']
    #==exclude