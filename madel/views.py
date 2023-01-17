from django.shortcuts import render
from .models import Product

# Create your views here.

from django.shortcuts import HttpResponse, redirect
from datetime import datetime


def main_view(request):
    return render(request, 'layouts/index.html')

def products_view(request):
    context = {
        "posts": Product.objects.all()
    }
    return render(request, 'products/products.html', context=context)