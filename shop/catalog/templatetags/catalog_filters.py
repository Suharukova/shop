from django.template import Library

register = Library()

@register.filter(name='in_stock')
def in_stock(count, arg):
    arg = arg.split('|')
    return arg[0] if count > 0 else arg[1]