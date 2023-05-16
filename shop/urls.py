from django.urls import path
from .views import *



urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list'}), name="products"),
    path('api/category/', CategorylistView.as_view(), name='category'),
]

#HW
# 1. Pycharm
# 2. git/github
# 4. Detailed page of Product


# 1. Django Rest Framework
# 2. Databases (w3school)
# 3. Cointainers/ Docker
# 4. python webservers
# 5. ubuntu/linux
# 6. git / github
# 7. Python / Django
# 8. Algorithms
# 9. Debug
