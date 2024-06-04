
from django.urls import path
from .views import *

urlpatterns = [
    # path('home/',homepage),
    # path('service/',servicepage),
    # path('about/',aboutpage),
    # path('contact/',contactpage),
    path('productadd/',product_add_page),
    path('products/',products),
    path('delete/<int:id>/',delete_product,name="delete_data"),
    path('update/<int:id>/',update_product,name="update_data"),

]