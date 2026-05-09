from rest_framework import routers

from brands.views import BrandsViewSet

router = routers.SimpleRouter()
router.register(r'', BrandsViewSet, basename='brand')

urlpatterns = router.urls