from django.contrib import admin
from django.urls import path
from products.views import main, product_view, detail_view, categories_view, crate_prducts_view
from django.conf.urls.static import static
from Stor.settings import MEDIA_URL, MEDIA_ROOT
from users.views import login_view, logout_view, register_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('products/', product_view),
    path('products/<int:id>/', detail_view),
    path('categories/', categories_view),
    path('products/create/', crate_prducts_view),
    # users
    path('users/login/', login_view),
    path('users/register/', register_view),
    path('users/logout/', logout_view)
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
