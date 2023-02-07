from django.shortcuts import render, HttpResponse, redirect
from products.models import Product, Comment, Category
from Stor.forms import ProductCreateForm, ReviewCreateForm


# Create your views here.
PAGIMATION_LIMIT = 3


def main(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def product_view(request):
    products = Product.objects.all()
    max_page = products.__len__() / PAGIMATION_LIMIT
    if request.method == 'GET':
        products = Product.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        if search is not None:
            products = Product.objects.filter(title__icontains=search)
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)
        products = products[PAGIMATION_LIMIT * (page - 1): PAGIMATION_LIMIT * page]


        context = {
            'products': products,
            'max_page': range(1, max_page+1)
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
                author_id=request.user.id,
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
                author_id=request.user.id,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                # rate=form.clea ned_data['rate'] if form.cleaned_data['rate'] is not None else 5,
                price=form.cleaned_data['price']
            )
            return redirect('/products')

        return render(request, 'products/create.html', context={
            'form': form
        })
