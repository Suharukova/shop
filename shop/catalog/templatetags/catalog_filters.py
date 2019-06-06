from django.template import Library

register = Library()

@register.filter(name='in_stock')
def in_stock(value, arg='In Stock|Out of stock'):
    arg = str(arg).split('|')
    assert len(arg) == 2, "arg must have 2 values"
    return arg[0] if value.count > 0 else arg[1]