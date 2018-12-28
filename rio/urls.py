from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('order/new', views.order_new, name='order_new'),
]
