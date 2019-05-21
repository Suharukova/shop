from django.shortcuts import render, get_object_or_404, redirect

from cart.forms import AddToCartForm
from cart.models import Cart, CartItem


# Create your views here.
from catalog.models import Item


def add_to_cart(request):
    add_to_cart_form = AddToCartForm(request.GET)
    cart = get_cart(request.session)
    if add_to_cart_form.is_valid():
        add_item_to_cart(cart, get_object_or_404(Item, pk=add_to_cart_form.cleaned_data['item_id']), add_to_cart_form.cleaned_data['amount'])
    return redirect('item_list')


def get_cart(session):
    try:
        cart = Cart.objects.get(pk=session['cart_id'])
    except (KeyError, Cart.DoesNotExist) as e:
        cart = Cart()
        cart.save()
        session['cart_id'] = cart.id
    return cart


def add_item_to_cart(cart, item, amount=1):
    #if not CartItem.amount:
        cart_item = CartItem(cart=cart, item=item, amount=amount)
        cart_item.save()
        return cart_item

def cart_list(request):
    return render(request, 'cart_list.html', {'carts': Cart.objects.all()})
