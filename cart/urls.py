from django.conf.urls import url
from cart import views as main_views

urlpatterns = [
    url(r'^$', main_views.cart, name='cart'),
    url(r'^add_item$', main_views.add_item, name='add_cart_item'),
    url(r'^delete_item$', main_views.del_item, name='del_cart_item'),
    url(r'^change_item_count$', main_views.change_item_count, name='change_cart_item_count'),

]
