from django.contrib import admin
from django.urls import path
from products.views import MainView, ProductsView, ProductDetailView, CategoryView, CreateProduct
# main, product_view, detail_view, categories_view, crate_prducts_view
from django.conf.urls.static import static
from Stor.settings import MEDIA_URL, MEDIA_ROOT
from users.views import LoginView, LogoutView, RegisterView
# login_view, logout_view, register_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('products/', ProductsView.as_view()),
    path('products/<int:id>/', ProductDetailView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('products/create/', CreateProduct.as_view()),
    # users
    path('users/login/', LoginView.as_view()),
    path('users/register/', RegisterView.as_view()),
    path('users/logout/', LogoutView.as_view())
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
