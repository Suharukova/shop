from django.shortcuts import render, get_object_or_404, redirect

from cart.forms import AddToCartForm
from cart.models import Cart, CartItem


# Create your views here.
from catalog.models import Item


def add_to_cart(request):
    add_to_cart_form = AddToCartForm(request.GET)
    if add_to_cart_form.is_valid():
        add_item_to_cart(request.cart, get_object_or_404(Item,
                         pk=add_to_cart_form.cleaned_data['item_id']),
                         add_to_cart_form.cleaned_data['amount'])
    return redirect('item_list')

def add_item_to_cart(cart, item, amount=1):
    amount = amount if item.count - amount > 0 else item.count
    cart_item, created = CartItem.objects.update_or_create(defaults={'amount': amount}, item=item, cart=cart)
    return cart_item

def cart_item_list(request):
    return render(request, 'cart_item_list.html', {'cart': request.cart})
