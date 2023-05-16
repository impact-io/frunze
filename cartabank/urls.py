
from rest_framework import routers
from .views import CartabankviewSet

router = routers.DefaultRouter()
router.register('api/cartabank', CartabankviewSet, 'cartabank' )

urlpatterns = router.urls