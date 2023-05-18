from django.contrib import admin
from django.urls import path, include



def jls_extract_def():
    return 'user/'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('shop/', include('shop.urls')),
    path('carta/', include('cartabank.urls')),
]
