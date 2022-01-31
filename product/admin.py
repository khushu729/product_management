from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'code', 'price', 'user']
	search_fields = ['user__email', 'name', 'code']
	list_filter = ['expiry_date', 'manufacture_date', 'status']
	readonly_fields = ['created_at', 'updated_at']


class CategoryAdmin(MPTTModelAdmin):
	tree_auto_open = True
	list_display = ['name', 'slug', 'description', 'enabled']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
