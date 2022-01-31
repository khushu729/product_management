from datetime import datetime
from django.db import models
from django.conf import settings

from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Category(MPTTModel):
	name = models.CharField(max_length=255, verbose_name="Category Name")
	description = models.TextField(null=True, blank=True)
	parent = TreeForeignKey(
		'self',
		null=True,
		blank=True,
		related_name='children',
		db_index=True,
		on_delete=models.CASCADE
	)
	enabled = models.BooleanField(default=True)
	slug = models.SlugField(max_length=255, unique=True)

	class MPTTMeta:
		order_insertion_by = ['name']

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name

	@classmethod
	def get_level_tree_display(cls):
		"""
		This will return list of level with tree representation
		"""
		level_list = []

		def add_nodes(categories):
			for product_category in categories:
				level_list.append([product_category.id, ('-- ' * product_category.level) + product_category.name])
				if not product_category.is_leaf_node():
					add_nodes(product_category.children.filter(enabled=True))
		add_nodes(cls.objects.filter(parent=None, enabled=True))
		return level_list


class Product(models.Model):
	STATUS_CHOICES = (
		('in_stock', "In Stock"),
		('out_of_stock', "Out Of Stock"),
	)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owner", verbose_name="Owner")
	name = models.CharField(max_length=100, verbose_name="Product Name")
	code = models.CharField(max_length=15, verbose_name="Product code")
	price = models.FloatField(verbose_name="Product Price")
	category = models.ManyToManyField(Category, blank=True)
	manufacture_date = models.DateTimeField()
	expiry_date = models.DateTimeField()
	status = models.CharField(choices=STATUS_CHOICES, verbose_name="Product Status", max_length=15, default="in_stock")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	price_updated_at = models.DateTimeField(auto_now_add=True)

	def __init__(self, *args, **kwargs):
		super(Product, self).__init__(*args, **kwargs)
		self._price = self.price

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if self.pk and self._price != self.price:
			self.price_updated_at = datetime.now()
		super(Product,self).save(*args, **kwargs)

	@property
	def get_product_categories_str(self):
		return ",".join(self.category.values_list('name', flat=True))