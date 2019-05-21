from django.shortcuts import render, get_object_or_404, redirect

from cart.forms import AddToCartForm
from cart.models import Cart, CartItem


# Create your views here.
from catalog.models import Item


def add_to_cart(request):
    add_to_cart_form = AddToCartForm(request.GET)
    if add_to_cart_form.is_valid():
        add_item_to_cart(get_cart(request.session), get_object_or_404(Item,
                         pk=add_to_cart_form.cleaned_data['item_id']),
                         add_to_cart_form.cleaned_data['amount'])
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
    amount = amount if item.count - amount > 0 else item.count
    cart_item, created = CartItem.objects.update_or_create(defaults={'amount': amount}, item=item, cart=cart)
    return cart_item

def cart_item_list(request):
    cart = get_cart(request.session)
    return render(request, 'cart_item_list.html', {'items': CartItem.objects.filter(cart=cart),
                                                   'total_price': cart.total_price})
