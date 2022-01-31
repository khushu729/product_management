from django.urls import path
from .views import ProductTemplateView, CategoryTemplateView

urlpatterns = [
    path("product", ProductTemplateView.as_view(), name="product"),
	path("category", CategoryTemplateView.as_view(), name="category"),
]
