from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as uReq 

url = "http://www.husqvarna.com/us/products/commercial-weed-trimmers/"

 # opens the connection and downloads html page from url
uClient = uReq(url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()
# finds each product from the store page
containers = page_soup.findAll("li", {"class": "product"})

# name the output file to write to local disk
out_filename = "items.csv"
# header of csv file to be written
headers = "product_name,article_number,price \n"

# opens file, and writes headersshipping
f = open(out_filename, "w")
f.write(headers)

# loops over each product and grabs attributes about
# each product
for container in containers:

    # Grabs the text within the second "(a)" tag from within
    # the list of queries.
    product_name = container.div.div.div.div.div.h4.a.text
    #container.div.div.div.div.div[1].div[2].h4.a
    # Grabs the text within the second "(a)" tag from within
    # the list of queries.
    article_number = container.div.div.div.div.div.p.text.strip()

    # Grabs the product shipping information by searching
    # all lists with the class "price-ship".
    # Then cleans the text of white space with strip()
    # Cleans the strip of "Shipping $" if it exists to just get number
    price = container.findAll("span", {"class": "price"})[0].text.strip().replace("$", "")

 
  
    # prints the dataset to console
    print("name: " + product_name + "\n")
    print("article: " + article_number + "\n")
    print("price: " + price + "\n")

    # writes the dataset to file
    f.write(product_name + ", " + article_number.replace(",", "|") + ", " + price + "\n")

f.close()  
