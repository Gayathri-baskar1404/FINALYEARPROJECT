from django.contrib import admin
from .models import Product, ProductDescription, ProductReview, ProductPricing

admin.site.register(Product)
admin.site.register(ProductDescription)
admin.site.register(ProductReview)
admin.site.register(ProductPricing)