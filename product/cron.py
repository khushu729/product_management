from datetime import datetime
from .models import Product


def delete_expired_products():
	expired_products = Product.objects.filter(expiry_date__lte=datetime.now())
	expired_products.delete()