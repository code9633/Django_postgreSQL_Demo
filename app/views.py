from django.shortcuts import render
from django.http import HttpResponse

from app.models import Product
# Create your views here.

def index(request):
    products = Product.objects.all() 
    return render(request, 'app/index.html', {'products': products})

def checkout(request):
    return HttpResponse("This is the checkout page")
