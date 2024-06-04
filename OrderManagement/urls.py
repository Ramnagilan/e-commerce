from django.urls import path
from .views import *


urlpatterns = [
    path("customers/",list_customer),
    path("customers/add/",add_customer),
    path("customers/update/<int:id>/",update_customer,name='update_customer'),
    path("customers/delete/<int:id>/",delete_customer,name='delete_customer'),
    
    path("add_order/",add_order),
    path("orders/",orders),
    path("delete_order/<int:id>/",order_delete,name="delete_order"),
    path("update_order/<int:id>/",update_order,name="update_order"),


]