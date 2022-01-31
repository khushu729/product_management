from django.urls import path, include
from rest_framework import routers
from .resources import ProductViewSet, CategoryViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)

urlpatterns = router.urls