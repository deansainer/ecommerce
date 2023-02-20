from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('thanks_page/', views.thanks_page, name='thanks_page'),
    path('update_item/', views.updateItem, name='update_item'),
]
