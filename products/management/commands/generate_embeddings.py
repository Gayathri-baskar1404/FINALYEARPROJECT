from django.core.management.base import BaseCommand
from sentence_transformers import SentenceTransformer
from products.models import ProductDescription

class Command(BaseCommand):
    help = "Generate embeddings for all products"

    def handle(self, *args, **kwargs):
        model = SentenceTransformer('all-MiniLM-L6-v2')

        descriptions = ProductDescription.objects.select_related('product').all()

        for item in descriptions:
            text = f"{item.product.name}. {item.full_description}"
            embedding = model.encode(text).tolist()

            item.embedding = embedding
            item.save()

            self.stdout.write(f"Updated embedding for: {item.product.name}")

        self.stdout.write(self.style.SUCCESS("All embeddings updated successfully."))