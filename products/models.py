from django.db import models
from pgvector.django import VectorField


class Product(models.Model):
    name = models.TextField()
    brand = models.TextField()
    category = models.TextField()
    subcategory = models.TextField()

    full_description = models.TextField()
    embedding = VectorField(dimensions=384, null=True, blank=True)

    rating = models.DecimalField(max_digits=3, decimal_places=2)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="INR")
    discount_percentage = models.IntegerField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="reviews")
    review_text = models.TextField()
    review_rating = models.DecimalField(max_digits=3, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.email} - {self.product.name}"