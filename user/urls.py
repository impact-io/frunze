
from rest_framework import routers
from .views import UserViewsets

from .views import ShopViewSet

router = routers.DefaultRouter()
router.register('', UserViewsets, 'shop' ),
router.register('', ShopViewSet, 'shop' )

urlpatterns = router.urls


# router = routers.DefaultRouter()
# router.register('', ShopViewSet, 'shop' )

# urlpatterns = router.urls
