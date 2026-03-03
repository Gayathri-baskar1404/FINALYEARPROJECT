import csv
from django.core.management.base import BaseCommand
from sentence_transformers import SentenceTransformer
from products.models import Product

class Command(BaseCommand):
    help = "Import electronics products from CSV"

    def handle(self, *args, **kwargs):
        model = SentenceTransformer('all-MiniLM-L6-v2')

        with open('electronics_250_products.csv', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                combined_text = f"{row['name']}. {row['full_description']}"

                embedding = model.encode(combined_text).tolist()

                product = Product.objects.create(
                    name=row['name'],
                    brand=row['brand'],
                    category=row['category'],
                    subcategory=row['subcategory'],
                    full_description=row['full_description'],
                    rating=row['rating'],
                    base_price=row['base_price'],
                    currency=row['currency'],
                    discount_percentage=row['discount_percentage'],
                    embedding=embedding
                )

                self.stdout.write(f"Inserted: {product.name}")

        self.stdout.write(self.style.SUCCESS("All products imported successfully"))