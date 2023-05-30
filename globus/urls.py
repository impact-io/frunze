from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('carta/', include('cartabank.urls')),
    path('user/',include('user.urls'))
]

