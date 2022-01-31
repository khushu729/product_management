from datetime import datetime
from rest_framework import serializers
from product.models import Category, Product


class ProductSerilizer(serializers.ModelSerializer):
	product_categories = serializers.SerializerMethodField()

	def get_product_categories(self, obj):
		return obj.get_product_categories_str

	class Meta:
		model = Product
		fields = '__all__'

	def validate(self, attrs):
		user = self.context['request'].user
		if self.instance and self.instance.user != user and not user.is_superuser:
			raise serializers.ValidationError("You are not authorized person to perform this action!!")
		return attrs

	def validate_price(self, price):
		if self.instance:
			old_price = self.instance.price
			max_price_value = old_price * (100 + 10) / 100
			min_price_value = old_price * (100 - 10) / 100
			if not (min_price_value <= price <= max_price_value):
				raise serializers.ValidationError(f"You can set price in between {min_price_value} and {max_price_value}")
			if self.instance.price_updated_at.date == datetime.now().date or datetime.now().hour > 11:
				raise serializers.ValidationError(f"You can set the price only once in a day and also between 12 AM to 11 AM")
		return price


class CategorySerilizer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'
