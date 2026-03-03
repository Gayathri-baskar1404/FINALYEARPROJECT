from django.core.management.base import BaseCommand
from sentence_transformers import SentenceTransformer
from products.models import Product


class Command(BaseCommand):
    help = "Generate embeddings including product description and reviews"

    def handle(self, *args, **kwargs):
        model = SentenceTransformer('all-MiniLM-L6-v2')

        products = Product.objects.prefetch_related('reviews').all()

        for product in products:
            review_texts = " ".join(
                review.review_text for review in product.reviews.all()
            )

            combined_text = f"""
            {product.name}.
            {product.full_description}.
            Reviews: {review_texts}
            """

            embedding = model.encode(combined_text).tolist()

            product.embedding = embedding
            product.save()

            self.stdout.write(f"Updated embedding for: {product.name}")

        self.stdout.write(self.style.SUCCESS("All embeddings updated successfully."))