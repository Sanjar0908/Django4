from django.shortcuts import render, HttpResponse, redirect
from products.models import Product, Comment, Category
from Stor.forms import ProductCreateForm, ReviewCreateForm


# Create your views here.

def main(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def product_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)


def detail_view(request, **kwargs):
    if request.method == 'GET':
        product = Product.objects.get(id=kwargs['id'])
        reviews = Comment.objects.filter(post=product)

        data = {
            'products': product,
            'comments': reviews,
            'form': ReviewCreateForm,
        }

        return render(request, 'products/detail.html', context=data)
    if request.method == 'POST':
        form = ReviewCreateForm(data=request.POST)
        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                post_id=kwargs['id']
            )
            return redirect(f"/products/{kwargs['id']}/")


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'categories/index.html', context=context)


def crate_prducts_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data
            )
