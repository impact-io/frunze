from django.urls import path
from .views import *



urlpatterns = [
    path('', MainViewSet.as_view({'get':'list'}), name='homepage'),
    path('api/product/', ProductViewSet.as_view({'get': 'list'}), name="products"),
    path('api/order/', OrderViewSet.as_view({'get': 'list', 'post':'create'}), name="orders"),
    path('api/cagtegory/<int:cat_id>/', CategoryViewSet.as_view({'get': 'list'}), name="cat"),
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
