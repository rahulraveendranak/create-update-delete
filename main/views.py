from django.shortcuts import render,redirect
from main.forms import Productform 
from main.models import Product

# Create your views here.

def home(request):
    form  = Productform()
    products = Product.objects.all()
    if request.method == "POST":
        form = Productform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request, 'main/home.html',{'form':form})

def list(request):
    products = Product.objects.all()
    return render(request,'main/list.html',{'products':products})

def update(request,product_id):
    product = Product.objects.get(id=product_id)
    form  = Productform(instance=product)
    if request.method == 'POST':
        form = Productform(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request,'main/update.html',{'form':form,'product':product})

def delete(request,product_id):
    if request.method == 'POST':
        Product.objects.get(id=product_id).delete()
        return redirect('list')
