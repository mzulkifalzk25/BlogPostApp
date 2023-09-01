# C:/Users/talzu/OneDrive/Desktop/django23/django-rest/config/data/product_data.json
# python manage.py import_products C:/Users/talzu/OneDrive/Desktop/django23/django-rest/config/data/product_data.json

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
            price_str = item.get("price")

            # Extract numeric characters and the decimal point from the price string
            price_match = re.search(r"[\d.]+", price_str)
            if price_match:
                price = Decimal(price_match.group())
            else:
                price = Decimal("0.00")  # Set a default price if no valid price found

            image_url = item.get("image_url")
            image_path = item.get("image_path")

            product, created = Product.objects.get_or_create(
                name=name,
                price=price,
                image=image_path,
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Created product: {name}"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Product already exists: {name}"))
