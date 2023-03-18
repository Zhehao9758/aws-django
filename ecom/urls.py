from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path("<int:pk>", views.product_detail, name='product_detail'),
    path("add_to_cart/<int:pk>/", views.add_to_cart, name="add_to_cart"),
    path("cart/incre/<int:pk>/", views.incre, name="incre"),
    path("cart/decre/<int:pk>/", views.decre, name="decre"),
    path("cart/delete/<int:pk>/", views.delete, name="delete"),
]