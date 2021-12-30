from django.urls import path    
from product.views import product, cart

app_name = "product"

urlpatterns = [
    path("",product,name="product"),
    path("cart/",cart,name="cart")
]