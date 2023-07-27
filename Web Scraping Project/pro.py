import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []
Ratings = []

for i in range(2, 12):
    url = "https://www.flipkart.com/search?q=best+laptop+under+60000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_6_10_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_6_10_na_na_na&as-pos=6&as-type=RECENT&suggestionId=best+laptop+under+60000&requestId=d6661854-7375-496d-a564-ce2b0834994c&as-searchtext=best%20lapti&pages=" + str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_="_4rR01T")
    prices = box.find_all("div", class_="_3tbKJL")
    desc = box.find_all("ul", class_="_1xgFaf")
    reviews = box.find_all("div", class_="_3LWZlK")

    # Find the maximum length among ratings, names, prices, descriptions, and reviews
    max_length = max(len(names), len(prices), len(desc), len(reviews))

    # Iterate through the range of the maximum length
    for index in range(max_length):
        # Append product name
        if index < len(names):
            Product_name.append(names[index].text)
        else:
            Product_name.append(None)

        # Append price
        if index < len(prices):
            Prices.append(prices[index].text)
        else:
            Prices.append(None)

        # Append description
        if index < len(desc):
            Description.append(desc[index].text)
        else:
            Description.append(None)

        # Append review
        if index < len(reviews):
            Reviews.append(reviews[index].text)
        else:
            Reviews.append(None)

        # Append rating
        rating = box.find_all("div", class_="_3L_3L4")
        if index < len(rating):
            Ratings.append(rating[index].text)
        else:
            Ratings.append(None)

df = pd.DataFrame({
    "Product Name": Product_name,
    "Prices": Prices,
    "Description": Description,
    "Reviews": Reviews,
    "Ratings": Ratings
})

df.to_csv("hello_Rahul_60000.csv", index=False)
