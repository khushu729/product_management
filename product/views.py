import json
from django.views.generic import TemplateView
from .models import Category

# Create your views here.
class ProductTemplateView(TemplateView):
	"""
	Tempplate view to list all products for the customer and Admin
	"""
	template_name = "product/products.html"

	def get_context_data(self, **kwargs):
		context = super(ProductTemplateView, self).get_context_data(**kwargs)
		context['categories'] = json.dumps(Category().get_level_tree_display())
		# import pdb;pdb.set_trace()
		return context


class CategoryTemplateView(TemplateView):
	"""
	Tempplate view to list all categories for the customer and Admin
	"""
	template_name = "product/category.html"



