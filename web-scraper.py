from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json

url = "https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99"

driver = webdriver.Chrome('./chromedriver')
driver.get(url)

time.sleep(1)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")
driver.close()

data = {}
data['product_name'] = soup.select('h1.product-name')[0].text
data['price'] = float(soup.select('meta[itemprop="price"]')[0].attrs['content'])
data['color'] = soup.select('span[itemprop="color"]')[0].text
available_sizes = soup.select('span.size-available')

data['size'] = []

for size in available_sizes:
    data['size'].append(size.attrs['data-size'])


with open('product.txt', 'w') as outfile:
    json.dump(data, outfile)

