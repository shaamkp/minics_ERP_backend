import json
from django.shortcuts import render
from product.models import Product
from web.models import Subscribe
from django.http.response import HttpResponse


def index(request):
    products=Product.objects.all()

    context={
        "products":products
    }

    return render(request,"index.html",context=context) 


def subscribe(request):
    email = request.POST.get("email")

    if not Subscribe.objects.filter(email = email).exists():


        Subscribe.objects.create(
            email = email  
        )

        response_data = {
            "status" : "success",
            "title" : "You Successfully Registered",
            "message" : "You subscribe to our newsletter successfully."
        }
    else:  
        response_data = {
            "status" : "error",
            "title" : "You are already Subscribed",
            "message" : "You are already a member."
        }

    return HttpResponse(json.dumps(response_data), content_type ="application/javascript")


        