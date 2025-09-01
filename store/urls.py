from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orderitem', OrderItemViewSet)

urlpatterns = router.urls