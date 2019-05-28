from cart.models import Cart


class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.cart = self.get_cart(request.session)
        return self.get_response(request)

    @staticmethod
    def get_cart(session):
        try:
            cart = Cart.objects.get(pk=session['cart_id'])
        except (KeyError, Cart.DoesNotExist) as e:
            cart = Cart()
            cart.save()
            session['cart_id'] = cart.id
        return cart