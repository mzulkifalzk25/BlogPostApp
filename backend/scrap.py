import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import os
import json  # Import the json library


# Function to download and save an image
def download_image(image_url, save_path):
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return True
    except Exception as e:
        print(f"Failed to download image: {e}")
    return False


url = "https://www.beebay.pk/products"
output_directory = "product_images"  # Directory to save the images
product_data = []  # Initialize an empty list to store product data

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Add a User-Agent header to mimic a web browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Create a session with a retry mechanism
retry_strategy = Retry(
    total=3, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504]
)

adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("http://", adapter)
session.mount("https://", adapter)

try:
    response = session.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        product_cards = soup.find_all(class_="single-product-wrap")

        for card in product_cards:
            product_image_url = card.find(class_="img-1")["src"]
            product_name = card.find(class_="product_name").text.strip()
            new_price = card.find(class_="new-price").text.strip()

            # Download and save the image
            image_filename = f"{product_name}.jpg"
            image_path = os.path.join(output_directory, image_filename)

            if download_image(product_image_url, image_path):
                print(f"Downloaded and saved image: {image_path}")
            else:
                print(f"Failed to download image for {product_name}")

            print(f"Product Name: {product_name}")
            print(f"New Price: {new_price}")

            # Create a dictionary for the product and add it to the list
            product_dict = {
                "name": product_name,
                "price": new_price,
                "image_url": product_image_url,
                "image_path": image_path,
            }
            product_data.append(product_dict)

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while making the request: {e}")

# Convert the product data list to a JSON object and save it to a file
with open("product_data.json", "w") as json_file:
    json.dump(product_data, json_file, indent=4)

print("Product data saved to product_data.json")
