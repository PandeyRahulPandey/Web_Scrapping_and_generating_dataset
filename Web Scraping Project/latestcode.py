import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_data_from_url(url):
    pd.set_option("max_colwidth", 1000)

    Product_name = []
    Prices = []
    Description = []
    Reviews = []
    Ratings = []

    try:
        r = requests.get(url)
        r.raise_for_status()  # Check for any request errors
        soup = BeautifulSoup(r.text, "html.parser")

        # Replace the class names below with the appropriate ones for the target website
        product_boxes = soup.find_all("div", class_="product-box-class")
        # The product name, price, description, reviews, and ratings should be extracted from product_boxes.
        # You need to inspect the HTML to find the correct class names for these elements.

        for box in product_boxes:
            # Extract the product name
            product_name = box.find("div", class_="product-name-class")
            Product_name.append(product_name.text if product_name else None)

            # Extract the price
            price = box.find("div", class_="price-class")
            Prices.append(price.text if price else None)

            # Extract the description
            description = box.find("div", class_="description-class")
            Description.append(description.text if description else None)

            # Extract the reviews
            reviews = box.find("div", class_="reviews-class")
            Reviews.append(reviews.text if reviews else None)

            # Extract the ratings
            ratings = box.find("div", class_="ratings-class")
            Ratings.append(ratings.text if ratings else None)

        df = pd.DataFrame({
            "Product Name": Product_name,
            "Prices": Prices,
            "Description": Description,
            "Reviews": Reviews,
            "Ratings": Ratings
        })

        return df

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching the URL: {e}")
        return None
    except Exception as ex:
        print(f"An error occurred during scraping: {ex}")
        return None


# Now, you can call the function with any URL you want to scrape
url_to_scrape = "https://www.flipkart.com/search?q=lcd%20%20tv%20under%2080000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"  # Replace this with your desired URL
data_frame = scrape_data_from_url(url_to_scrape)

if data_frame is not None:
    data_frame.to_csv("scraped_data.csv", index=False)
    print("Data successfully scraped and saved to scraped_data.csv")
else:
    print("Data scraping failed.")
