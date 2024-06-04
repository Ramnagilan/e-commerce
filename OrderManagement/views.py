from django.shortcuts import render,redirect
from .models import Customer,Order
from .form import Customer_form,Order_form
from Inventory.models import Product

# Create your views here.
def list_customer(request):
    x=Customer.objects.all()
    return render(request,'customers.html',context={'x':x})

def add_customer(request):
    x=Customer_form()

    if request.method=="POST":
        x=Customer_form(request.POST)
        x.save()
        return redirect('/orders/customers/')

    return render(request,'customer_add.html',context={'x':x})


def update_customer(request,id):
    selected_customer=Customer.objects.get(id=id)
    x=Customer_form(instance=selected_customer)

    if request.method=="POST":
        x=Customer_form(request.POST,instance=selected_customer)
        if x.is_valid():
            x.save()
            return redirect('/orders/customers/')
    return render(request,'customer_add.html',context={'x':x})

def delete_customer(request,id):
     selected_customer=Customer.objects.get(id=id)
     selected_customer.delete()
     return redirect('/orders/customers/')

def add_order(request):
    context={
        "order_form":Order_form()
    }

    if request.method=="POST":
        selected_product=Product.objects.get(id=request.POST["product_reference"])

        amount=float(selected_product.price) * float(request.POST['quantity'])

        gst=(amount * selected_product.gst)/100

        bill_amount=amount + gst

        new_order=Order(customer_reference_id=request.POST['customer_reference'], product_reference_id=request.POST['product_reference'],
                        order_number=request.POST["order_number"], order_date=request.POST['order_date'], quantity=request.POST["quantity"],
                        amount=amount, gst=gst, bill_amount=bill_amount )
        
        new_order.save()
        return redirect('/orders/orders/')


    return render(request,"orders_add.html",context)


def orders(request):
    x=Order.objects.all()
    return render(request,"orders.html",context={'x':x})

def order_delete(request,id):
    selected_order=Order.objects.get(id=id)
    selected_order.delete()
    return redirect('/orders/orders/')

def update_order(request,id):
    selected_order=Order.objects.get(id=id)
    context={
        "order_form":Order_form(instance=selected_order)
    }

    if request.method=="POST":
        selected_product=Product.objects.get(id=request.POST["product_reference"])

        amount=float(selected_product.price) * float(request.POST['quantity'])

        gst=(amount * selected_product.gst)/100

        bill_amount=amount + gst

        order_filter=Order.objects.filter(id=id)
        order_filter.update(customer_reference_id=request.POST['customer_reference'], product_reference_id=request.POST['product_reference'],
                        order_number=request.POST["order_number"], order_date=request.POST['order_date'], quantity=request.POST["quantity"],
                        amount=amount, gst=gst, bill_amount=bill_amount)
        
        return redirect('/orders/orders/')


    return render(request,"orders_add.html",context)
