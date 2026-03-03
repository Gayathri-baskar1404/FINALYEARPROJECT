import random
from django.core.management.base import BaseCommand
from products.models import Product, Customer, Review

FIRST_NAMES = ["Rahul", "Priya", "Amit", "Sneha", "Arjun", "Meera", "Kiran", "Ananya", "Vikram", "Divya"]
LAST_NAMES = ["Sharma", "Reddy", "Iyer", "Patel", "Nair", "Gupta", "Kumar", "Joshi", "Verma", "Singh"]

REVIEW_TEXTS = [
    "Excellent performance and worth the price.",
    "Battery life is impressive and lasts all day.",
    "Build quality feels premium and solid.",
    "Value for money product.",
    "Performance is smooth and reliable.",
    "Exceeded my expectations.",
    "Good features but slightly overpriced.",
    "Highly recommended for daily use.",
    "User-friendly and easy to operate.",
    "Stylish design and fast performance."
]

class Command(BaseCommand):
    help = "Seed customers and reviews"

    def handle(self, *args, **kwargs):

        # Create Customers
        customers = []
        for i in range(150):
            first = random.choice(FIRST_NAMES)
            last = random.choice(LAST_NAMES)
            email = f"{first.lower()}{i}@gmail.com"

            customer = Customer.objects.create(
                first_name=first,
                last_name=last,
                email=email,
                phone_number=f"9{random.randint(100000000,999999999)}"
            )
            customers.append(customer)

        self.stdout.write("150 customers created.")

        # Add Reviews to Products
        products = Product.objects.all()

        for product in products:
            review_count = random.randint(3, 6)

            for _ in range(review_count):
                Review.objects.create(
                    product=product,
                    customer=random.choice(customers),
                    review_text=random.choice(REVIEW_TEXTS),
                    review_rating=round(random.uniform(3.5, 5.0), 1)
                )

        self.stdout.write(self.style.SUCCESS("Reviews added successfully."))