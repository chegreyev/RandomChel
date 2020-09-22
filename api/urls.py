from rest_framework.routers import DefaultRouter
from .views import BurgerViewSet

router = DefaultRouter()
router.register(r'burger' ,BurgerViewSet, basename='burgers' )

urlpatterns = router.urls