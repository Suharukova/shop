from django.contrib import admin, messages

# Register your models here.
from orders import models
from orders.models import InvalidOrderStateError


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    exclude = ['state']
    actions = ['review',
               'accept',
               'reject',
               'ship',
               'deliver',
               'drop']

    def transfer_state(self, request, newstate, queryset):
        for order in queryset:
            try:
                method = getattr(order, newstate)
                method()
            except InvalidOrderStateError as e:
                self.message_user(request, str(e), messages.WARNING)
            order.save()

    def review(self, request, queryset):
        self.transfer_state(request, 'review', queryset)
    def accept(self, request, queryset):
        self.transfer_state(request, 'accept', queryset)
    def reject(self, request, queryset):
        self.transfer_state(request, 'reject', queryset)
    def ship(self, request, queryset):
        self.transfer_state(request, 'ship', queryset)
        



@admin.register(models.PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    pass