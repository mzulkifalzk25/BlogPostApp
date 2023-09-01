import json
import re
from decimal import Decimal
from django.core.management.base import BaseCommand
from api.models import Product


class Command(BaseCommand):
    help = "Import products from a JSON file"

    def add_arguments(self, parser):
        parser.add_argument(
            "json_file",
            type=str,
            help="C:/Users/talzu/OneDrive/Desktop/django23/django-rest/config/data/product_data.json",
        )

    def handle(self, *args, **kwargs):
        json_file_path = kwargs["json_file"]

        with open(json_file_path, "r") as file:
            data = json.load(file)

        for item in data:
            name = item.get("name")

            # Preprocess the price value to remove non-numeric characters and convert to Decimal
            price_str = re.sub(r"[^\d.]", "", item.get("price"))
            price = Decimal(price_str)

            image_url = item.get("image_url")
            image_path = item.get("image_path")

            product, created = Product.objects.get_or_create(
                name=name,
                price=price,
                image=image_path,  # Provide the path to the image file
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Created product: {name}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Product already exists: {name}"))
