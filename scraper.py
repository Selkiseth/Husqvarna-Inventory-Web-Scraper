from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as uReq 
#Example page, full page list is on main folder
url = "http://www.husqvarna.com/us/products/commercial-weed-trimmers/"
uClient = uReq(url)
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# Find the Container of the products
containers = page_soup.findAll("li", {"class": "product"})

# name the output file however you want
out_filename = "items.csv"
# header of csv file to be written
headers = "product_name,article_number,price \n"

# opens file, and writes headersshipping
f = open(out_filename, "w")
f.write(headers)

for container in containers:

 
    product_name = container.div.div.div.div.div.h4.a.text

    article_number = container.div.div.div.div.div.p.text.strip()

    price = container.findAll("span", {"class": "price"})[0].text.strip().replace("$", "")

 
  
    # prints the dataset to console
    print("name: " + product_name + "\n")
    print("article: " + article_number + "\n")
    print("price: " + price + "\n")

    # writes the dataset to file
    f.write(product_name + ", " + article_number.replace(",", "|") + ", " + price + "\n")

f.close()  
