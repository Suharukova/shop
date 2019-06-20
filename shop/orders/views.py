from django.shortcuts import render

# Create your views here.
from django.views import View

from orders.forms import NewOrderForm


class OrderView(View):
    def get(self, request):
        context = {
            'form': NewOrderForm()
        }
        return render (request, 'order_add.html', context)

    def post(self, request):
        form = NewOrderForm(request.POST)
        if form.is_valid():
            cart = request.cart
            order = form.save()
            for item in cart.items:
                pass

