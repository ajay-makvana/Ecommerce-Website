from math import ceil

import django
from django.http import HttpResponse
from django.shortcuts import render
from .models import product
from .models import Contact

def index(request):
    '''Only For One ingle row in the display'''
    """products = product.objects.all()
    n = len(products)
    noOfSlide = ((n//4) + ceil((n/4)-(n//4)))
    parameter = {'noOfSlide':noOfSlide,'products':products,'range':range(1,noOfSlide)}
    return render(request,'shop/index.html',parameter)"""

    allProduct = []
    allCategory = product.objects.values('product_category','id')
    categories = {item['product_category'] for item in allCategory}
    for category in categories:
        prod = product.objects.filter(product_category = category)
        noOfSlide = ((len(prod)//4) + ceil((len(prod)/4)-(len(prod)//4)))
        allProduct.append([prod,range(1,noOfSlide),noOfSlide])

    parameter = {'allProducts':allProduct}

    return render(request,'shop/index.html',parameter)

def prodectView(request ,myid):
    specific_product = product.objects.filter(id = myid)
    print(specific_product[0])
    return render(request,'shop/product.html',{'product':specific_product[0]})


def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        description = request.POST.get('description','')
        contact = Contact(name=name,email=email,phone=phone,description=description)
        contact.save()
    return render(request,'shop/contactus.html')