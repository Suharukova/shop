from django.urls import path

from cart import views

urlpatterns=[
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart_list/', views.cart_list, name='cart_list')
]