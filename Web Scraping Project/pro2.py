import pandas as pd
import requests
from bs4 import BeautifulSoup   #BeautifulSoup is a popular Python library used for web scraping and parsing HTML and XML documents.

# Set the max_colwidth option to a higher value (e.g., 1000) to prevent truncation in the CSV file
pd.set_option("max_colwidth", 1000)

Product_name = []          #These lines initialize empty lists to store the extracted information from the web page.
                           #The data for product names, prices, descriptions, reviews, and ratings will be collected in these lists.
Prices = []
Description = []
Reviews = []
Ratings = []

for i in range(2, 12):
    url = "https://www.flipkart.com/search?q=best+laptop+under+60000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_6_10_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_6_10_na_na_na&as-pos=6&as-type=RECENT&suggestionId=best+laptop+under+60000&requestId=d6661854-7375-496d-a564-ce2b0834994c&as-searchtext=best%20lapti&pages=" + str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")                #"lxml" refers to the lxml parser, which is a fast and feature-rich XML and HTML parser library in Python.
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")    # This is typically a container element that holds information about the laptops on the Flipkart page.  

    names = box.find_all("div", class_="_4rR01T")       #These lines use the find_all() method from BeautifulSoup to extract all the relevant elements for product names, prices,
                                                            #descriptions, and reviews from the box container.
    prices = box.find_all("div", class_="_3tbKJL")
    desc = box.find_all("ul", class_="_1xgFaf")
    reviews = box.find_all("div", class_="_3LWZlK")

    # Find the maximum length among ratings, names, prices, descriptions, and reviews
    max_length = max(len(names), len(prices), len(desc), len(reviews))       #This line calculates the maximum length among the lists of names, prices, descriptions, and reviews.
                                                                             #It is used to ensure that we handle cases where the number of entries for each attribute might be different.

    # Iterate through the range of the maximum length
    for index in range(max_length):                       #It will be used to iterate through the extracted data and append it to the corresponding lists.
        # Append product name
        if index < len(names):                           #This block appends the product name of the current index from the names list to the Product_name list.
                                                         #If the names list is shorter than max_length, it appends None to the Product_name list for the remaining indices.

                                                         #Similarly, the following blocks append prices, descriptions, reviews, and ratings (if available) to their respective lists
                                                         #or append None if the lists are shorter than max_length.
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

df = pd.DataFrame({                          #These lines create a pandas DataFrame using the data stored in the lists Product_name, Prices, Description, Reviews, and Ratings.
                                             #Each list becomes a column in the DataFrame.
    "Product Name": Product_name,
    "Prices": Prices,
    "Description": Description,
    "Reviews": Reviews,
    "Ratings": Ratings
})

df.to_csv("hello_Rahul_60000.csv", index=False)   #Finally, this line saves the DataFrame as a CSV file named "hello_Pandey_60000.csv" in the current working directory.
                                                    #The index=False argument ensures that the index column is not included in the CSV file.
