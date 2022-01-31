from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.renderers import AdminRenderer
from django_filters.rest_framework import DjangoFilterBackend
from product.models import Product, Category
from .serializers import ProductSerilizer, CategorySerilizer
from .filters import CategoryFilter


class ProductViewSet(viewsets.ModelViewSet):
	authentication_classes = (SessionAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Product.objects.all()
	serializer_class = ProductSerilizer
	filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
	search_fields = ("name", "code")
	filter_class = CategoryFilter

	def check_permissions(self, request):
		super(ProductViewSet, self).check_permissions(request)
		if request.method in ["DELETE", "PUT", "PATCH"]:
			product = self.get_object()
			user = request.user
			if product and product.user != user and not user.is_superuser:
				self.permission_denied(request)

	def list(self, request, *args, **kwargs):
		self.object_list = self.filter_queryset(self.get_queryset())
		return super(ProductViewSet, self).list(request, *args, **kwargs)


class CategoryViewSet(viewsets.ModelViewSet):
	authentication_classes = (SessionAuthentication,)
	permission_classes = (IsAuthenticated, IsAdminUser)
	queryset = Category.objects.filter(enabled=True)
	serializer_class = CategorySerilizer
