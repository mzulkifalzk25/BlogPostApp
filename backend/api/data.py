import os
import re
from decimal import Decimal

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django

django.setup()

from api.models import Product

data = [
    {
        "name": "Tecno Spark 6 Go 64GB 4GB RAM",
        "price": "Rs. 17699",
        "image_url": "https://www.beebay.pk/uploads/products/1/Tecno-Spark-6-Go-64GB-4GB-RAM-1646819897.jpeg",
        "image_path": "images/phones/Tecno Spark 6 Go 64GB 4GB RAM.jpg",
    },
    {
        "name": "Tecno Camon 16 Pro 128GB 6GB R ...",
        "price": "Rs. 34397",
        "image_url": "https://www.beebay.pk/uploads/products/1/Tecno-Camon-16-Pro-128GB-6GB-RAM-1646815938.jpeg",
        "image_path": "images/phones/Tecno Camon 16 Pro 128GB 6GB R ....jpg",
    },
    {
        "name": "Tecno Pop 5 2GB 32GB",
        "price": "Rs. 11889",
        "image_url": "https://www.beebay.pk/uploads/products/1/Tecno-Pop-5-2GB-32GB-1646814897.jpeg",
        "image_path": "images/phones/Tecno Pop 5 2GB 32GB.jpg",
    },
    {
        "name": "Tecno Pova 2 6GB 128GB",
        "price": "Rs. 26999",
        "image_url": "https://www.beebay.pk/uploads/products/1/Tecno-Pova-2-6GB-128GB-1646813215.png",
        "image_path": "images/phones/Tecno Pova 2 6GB 128GB.jpg",
    },
    {
        "name": "Tecno Spark 7 4GB 64GB",
        "price": "Rs. 22230",
        "image_url": "https://www.beebay.pk/uploads/products/1/Tecno-Spark-7-4GB-64GB-1646803324.png",
        "image_path": "images/phones/Tecno Spark 7 4GB 64GB.jpg",
    },
    {
        "name": "Tecno Camon 18 128GB 4GB RAM",
        "price": "Rs. 32759",
        "image_url": "https://www.beebay.pk/uploads/products/1/Tecno-Camon-18-128GB-4GB-RAM-1646717919.jpeg",
        "image_path": "images/phones/Tecno Camon 18 128GB 4GB RAM.jpg",
    },
    {
        "name": "Tecno Spark 8 Pro 64GB 4GB",
        "price": "Rs. 23199",
        "image_url": "https://www.beebay.pk/uploads/products/1/Tecno-Spark-8-Pro-64GB-4GB-1646294042.jpeg",
        "image_path": "images/phones/Tecno Spark 8 Pro 64GB 4GB.jpg",
    },
    {
        "name": "Tecno Spark 7T 64GB 4GB",
        "price": "Rs. 20199",
        "image_url": "https://www.beebay.pk/uploads/products/1/Tecno-Spark-7T-64GB-4GB-1646287840.jpeg",
        "image_path": "images/phones/Tecno Spark 7T 64GB 4GB.jpg",
    },
    {
        "name": "Tecno Camon 18P 128GB 8GB",
        "price": "Rs. 31499",
        "image_url": "https://www.beebay.pk/uploads/products/1/Tecno-Camon-18P-128GB-8GB-1646286714.jpeg",
        "image_path": "images/phones/Tecno Camon 18P 128GB 8GB.jpg",
    },
    {
        "name": "Tecno Camon 18T 128GB 4GB",
        "price": "Rs. 25099",
        "image_url": "https://www.beebay.pk/uploads/products/1/Tecno-Camon-18T-128GB-4GB-1646286089.jpeg",
        "image_path": "images/phones/Tecno Camon 18T 128GB 4GB.jpg",
    },
    {
        "name": "OnePlus 9 256GB 12GB Ram",
        "price": "Rs. 99999",
        "image_url": "https://www.beebay.pk/uploads/products/1/OnePlus-9-256GB-12GB-Ram-1641369288.jpeg",
        "image_path": "images/phones/OnePlus 9 256GB 12GB Ram.jpg",
    },
    {
        "name": "OnePlus 9 Pro 256GB 12GB Ram",
        "price": "Rs. 129999",
        "image_url": "https://www.beebay.pk/uploads/products/1/OnePlus-9-Pro-256GB-12GB-Ram-1641366716.jpeg",
        "image_path": "images/phones/OnePlus 9 Pro 256GB 12GB Ram.jpg",
    },
    {
        "name": "Samsung Galaxy S21 plus 256GB ...",
        "price": "Rs. 176999",
        "image_url": "https://www.beebay.pk/uploads/products/1/Samsung-Galaxy-S21-plus-256GB-8GB-1640847438.jpeg",
        "image_path": "images/phones/Samsung Galaxy S21 plus 256GB ....jpg",
    },
    {
        "name": "Samsung Galaxy A72 128GB 8GB R ...",
        "price": "Rs. 77699",
        "image_url": "https://www.beebay.pk/uploads/products/1/Samsung-Galaxy-A72-128GB-8GB-Ram-1639735497.jpeg",
        "image_path": "images/phones/Samsung Galaxy A72 128GB 8GB R ....jpg",
    },
    {
        "name": "Samsung Galaxy A03s 3GB 32GB",
        "price": "Rs. 21299",
        "image_url": "https://www.beebay.pk/uploads/products/1/Samsung-Galaxy-A03s-3GB-32GB-1639734863.jpeg",
        "image_path": "images/phones/Samsung Galaxy A03s 3GB 32GB.jpg",
    },
    {
        "name": "Samsung Galaxy A03s 4GB 64GB",
        "price": "Rs. 22116",
        "image_url": "https://www.beebay.pk/uploads/products/1/Samsung-Galaxy-A03s-4GB-64GB-1639727157.jpeg",
        "image_path": "images/phones/Samsung Galaxy A03s 4GB 64GB.jpg",
    },
    {
        "name": "Samsung Galaxy A52s 5G 128GB 8 ...",
        "price": "Rs. 78699",
        "image_url": "https://www.beebay.pk/uploads/products/1/Samsung-Galaxy-A52s-5G-128GB-8GB-1639726680.jpeg",
        "image_path": "images/phones/Samsung Galaxy A52s 5G 128GB 8 ....jpg",
    },
    {
        "name": "Apple iPhone 12 Pro Max 256GB ...",
        "price": "Rs. 164999",
        "image_url": "https://www.beebay.pk/uploads/products/1/Apple-iPhone-12-Pro-Max-256GB-Single-Sim-1639400429.jpeg",
        "image_path": "images/phones/Apple iPhone 12 Pro Max 256GB ....jpg",
    },
    {
        "name": "Apple iPhone SE 2nd Generation ...",
        "price": "Rs. 76999",
        "image_url": "https://www.beebay.pk/uploads/products/1/Apple-iPhone-SE-2nd-Generation-64GB-1639398131.jpeg",
        "image_path": "images/phones/Apple iPhone SE 2nd Generation ....jpg",
    },
    {
        "name": "Apple iPhone SE 2nd Generation ...",
        "price": "Rs. 97000",
        "image_url": "https://www.beebay.pk/uploads/products/1/Apple-iPhone-SE-2nd-Generation-256GB-1639397865.jpeg",
        "image_path": "images/phones/Apple iPhone SE 2nd Generation ....jpg",
    },
]

for item in data:
    name = item.get("name")
    price_str = item.get("price")
    price_match = re.search(r"[\d.]+", price_str)

    if price_match:
        price = Decimal(price_match.group())
    else:
        price = Decimal("0.00")

    image_url = item.get("image_url")
    image_path = item.get("image_path")

    product, created = Product.objects.get_or_create(
        name=name,
        price=price,
        image=image_url,
    )

    if created:
        print(f"Created product: {name}")
    else:
        print(f"Product already exists: {name}")

print("Data population completed.")
