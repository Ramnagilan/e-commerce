from django.shortcuts import render,redirect
from .forms import Product_form
from .models import Product

# Create your views here.

# def homepage(request):
#     data={
#         'name':'ram',
#         'roll':'admin',
#         'numbers':[1,2,3,6,5,4],
#         'marks':{
#             'english':100,
#             'tamil':80
#         }

#     }
#     return render(request,"home.html",data)


# def aboutpage(request):
#     return render(request,"about.html")


# def contactpage(request):
#     return render(request,"contact.html")


# def servicepage(request):
#     return render(request,"service.html")


def product_add_page(request):
    context={
        "x":Product_form()
    }

    if request.method=="POST":
        x=Product_form(request.POST)
        if x.is_valid():

            x.save()
            return redirect('/inventory/products/')

    return render(request,"product_add.html",context)


def products(request):
    x=Product.objects.all()
    return render(request,"products.html",context={'x':x})

def delete_product(request,id):
    selete_product=Product.objects.get(id=id)
    selete_product.delete()
    return redirect('/inventory/products/')

def update_product(request,id):
    selete_product=Product.objects.get(id=id)
    context={
         'x':Product_form(instance=selete_product)
    }
   

    if request.method=='POST':
        value=Product_form(request.POST,instance=selete_product)
        if value.is_valid():
            value.save()
            return redirect('/inventory/products/')
        
    return render(request,"product_add.html",context)


    