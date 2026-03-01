from django.db import models
from pgvector.django import VectorField

class Product(models.Model):
    name = models.TextField()
    category = models.TextField()
    subcategory = models.TextField()

    def __str__(self):
        return self.name


class ProductDescription(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    full_description = models.TextField()
    embedding = VectorField(dimensions=384, null=True, blank=True)


class ProductReview(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    review_count = models.IntegerField()
    top_feedback_summary = models.TextField()


class ProductPricing(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='INR')
    discount_percentage = models.IntegerField()