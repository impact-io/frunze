from django.urls import path
from .views import UserCreateView, UserViewSet



urlpatterns = [
    path('', UserCreateView.as_view()),
    path('api/user', UserViewSet.as_view({'get':'list'}), name='user'),
]
