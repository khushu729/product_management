import django_filters
from django_filters import rest_framework as filters
from product.models import Product


class CategoryFilter(filters.FilterSet):
	""" """
	filter_by_category = django_filters.CharFilter(method="filter_products_by_category")

	class Meta:
		model = Product
		fields = ["filter_by_category"]

	def filter_products_by_category(self, queryset, name, value):
		return queryset.filter(category__id=value)
