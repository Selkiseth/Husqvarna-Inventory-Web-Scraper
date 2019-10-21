from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as uReq 

url = input("Please enter url ̣\n >: ")

uClient = uReq(url)

page_soup = soup(uClient.read(), "html.parser")
uClient.close()

containers = page_soup.findAll("li", {"class": "product"})

out_filename = "files.csv"

headers = "imagelink \n"

f = open(out_filename, "w")
f.write(headers)

for container in containers:

    image = container.div.div.div.div.div.div.a.picture.img
    imagelink = image['srcset']
    imglink = imagelink[2:]

    print("image link: " + imglink + "\n")

    f.write(imglink + "\n")

f.close()  
