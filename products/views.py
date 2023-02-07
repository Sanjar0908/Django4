from django.shortcuts import render, redirect
from products.models import Product, Comment, Category
from Stor.forms import ProductCreateForm, ReviewCreateForm
from django.views.generic import ListView, CreateView, DetailView

# Create your views here.
PAGINATION_LIMIT = 3


class MainView(ListView):
    model = Product
    template_name = 'layouts/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'layouts/index.html')


class ProductsView(ListView):
    model = Product
    template_name = 'products/products.html'

    def get(self, request, **kwargs):
        products = self.get_queryset()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search is not None:
            products = Product.objects.filter(
                name__icontains=search,
                description__icontains=search
            )

        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        """ slice posts """
        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context = {
            'products': products,
            'user': request.user,
            'max_page': range(1, max_page + 1),
        }

        return render(request, self.template_name, context=context)


class ProductDetailView(DetailView, CreateView):
    model = Product
    template_name = 'products/detail.html'
    pk_url_kwarg = 'id'
    queryset = Product.objects.all()
    form_class = ProductCreateForm

    def get_context_data(self, **kwargs):
        return {
            'product': self.get_object(),
            'reviews': Comment.objects.filter(product=self.get_object()),
            'form': kwargs.get('form', self.form_class)
        }

    def post(self, request, *args, **kwargs):
        form = ReviewCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                author_id=request.user.id,
                product_id=id,
                text=form.cleaned_data.get('text'),
            )
            return redirect(f'/products/{id}/')


class CategoryView(ListView):
    model = Category
    template_name = 'categories/index.html'

    def get(self, request, **kwargs):
        categories = Category.objects.all()
        context = {
            'categories': categories,
        }
        return render(request, self.template_name, context=context)


class CreateProduct(ListView, CreateView):
    template_name = 'products/create.html'
    form_class = ProductCreateForm
    queryset = Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': ProductCreateForm,
        }

    def post(self, request, **kwargs):
        form = ProductCreateForm(request.POST, request.FILES)

        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data['price'] if form.cleaned_data['price'] is not None else 5,
            )
            return redirect('/products/')



#
# def main(request):
#     if request.method == 'GET':
#         return render(request, 'layouts/index.html')
#
#
# def product_view(request):
#     products = Product.objects.all()
#     max_page = products.__len__() / PAGINATION_LIMIT
#     if request.method == 'GET':
#         products = Product.objects.all()
#         search = request.GET.get('search')
#         page = int(request.GET.get('page', 1))
#         if search is not None:
#             products = Product.objects.filter(title__icontains=search)
#         if round(max_page) < max_page:
#             max_page = round(max_page) + 1
#         else:
#             max_page = round(max_page)
#         products = products[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * page]
#
#
#         context = {
#             'products': products,
#             'max_page': range(1, max_page+1)
#         }
#         return render(request, 'products/products.html', context=context)
#
#
# def detail_view(request, **kwargs):
#     if request.method == 'GET':
#         product = Product.objects.get(id=kwargs['id'])
#         reviews = Comment.objects.filter(post=product)
#
#         data = {
#             'products': product,
#             'comments': reviews,
#             'form': ReviewCreateForm,
#         }
#
#         return render(request, 'products/detail.html', context=data)
#     if request.method == 'POST':
#         form = ReviewCreateForm(data=request.POST)
#         if form.is_valid():
#             Comment.objects.create(
#                 author_id=request.user.id,
#                 text=form.cleaned_data.get('text'),
#                 post_id=kwargs['id']
#             )
#             return redirect(f"/products/{kwargs['id']}/")
#
#
# def categories_view(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         context = {
#             'categories': categories
#         }
#         return render(request, 'categories/index.html', context=context)
#
#
# def crate_prducts_view(request):
#     if request.method == 'GET':
#         context = {
#             'form': ProductCreateForm
#         }
#         return render(request, 'products/create.html', context=context)
#
#     if request.method == 'POST':
#         form = ProductCreateForm(data=request.POST)
#
#         if form.is_valid():
#             Product.objects.create(
#                 author_id=request.user.id,
#                 title=form.cleaned_data.get('title'),
#                 description=form.cleaned_data.get('description'),
#                 # rate=form.clea ned_data['rate'] if form.cleaned_data['rate'] is not None else 5,
#                 price=form.cleaned_data['price']
#             )
#             return redirect('/products')
#
#         return render(request, 'products/create.html', context={
#             'form': form
#         })
