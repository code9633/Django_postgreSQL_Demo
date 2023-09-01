from django.shortcuts import render, redirect
from django.http import HttpResponse

from app.models import Product, MyModel
from app.forms import MyForm
# Create your views here.

def index(request):
    products = Product.objects.all() 
    return render(request, 'app/index.html', {'products': products})

def checkout(request):
    return HttpResponse("This is the checkout page")


def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")       
    else:
        form = MyForm()
            
    return render(request, 'app/my_form_template.html', {'form':form})   


def success_view(request):
    return render(request, "app/success_template.html" )


def report_view(request):
    data = MyModel.objects.all()
    return render(request, "app/report_template.html", {'data': data})