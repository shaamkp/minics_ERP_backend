from django.urls import path
from web.views import index
from web.views import subscribe


app_name = "web"

urlpatterns = [
    path("", index, name="index"),
    path("subscribe/",subscribe, name ="subscribe"),
    path("subscribe/",subscribe, name ="subscribe")
]