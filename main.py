import codecs
import html.parser as htmlparser
import requests
from urllib import request, response, error, parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import etree
import re

url = "https://auto.ria.com/search/?year[0].gte=2015&categories.main.id=1&brand.id[0]=24&price.currency=1&abroad.not=0&custom.not=1&page=0&size=20"
html = urlopen(url)
soup = BeautifulSoup(html, "lxml")

title_list =[]
price_list =[]
location_list =[]
fuel_list =[]
description_list =[]
mileage_list =[]
transmission_list =[]



titles = soup.find_all('div', { "class" : "head-ticket" })
for title in titles:
    print(title.get_text())
    title_list.append(title.get_text())

titles = soup.find_all('span', { "data-currency" : "USD" })
for title in titles:
    print(title.get_text())
    price_list.append(title.get_text())

titles = soup.find_all('div', { "class" : "definition-data" })
for title in titles:
    print(title.get_text())
    description_list.append(title.get_text())

titles = soup.find_all('i', { "class" : "icon-mileage" })
for title in titles:
    print(title.parent.get_text())
    mileage_list.append(title.parent.get_text())

titles = soup.find_all('i', { "class" : "icon-location" })
for title in titles:
    print(title.parent.get_text())
    location_list.append(title.parent.get_text())

titles = soup.find_all('i', { "class" : "icon-transmission" })
for title in titles:
    print(title.parent.get_text())
    transmission_list.append(title.parent.get_text())

titles = soup.find_all('i', { "class" : "icon-fuel" })
for title in titles:
    print(title.parent.get_text())
    fuel_list.append(title.parent.get_text())

print(title_list)
print(price_list )
print(location_list)
print(fuel_list )
print(description_list)
print(mileage_list)
print(transmission_list)


i = 0
while i < len(title_list):
    print(title_list[i])
    print(price_list[i])
    print(location_list[i])
    print(description_list[i])
    print(mileage_list[i])
    print(transmission_list[i])
    print(fuel_list[i])
    i += 1

root = etree.Element('elements')
j = 0
while j < len(title_list):
    child = etree.SubElement(root,'element', id = str(j+1))

    title1 = etree.SubElement(child, 'title')
    title1.text= title_list[j]

    price = etree.SubElement(child, 'price')
    price.text = price_list[j]

    location = etree.SubElement(child, 'location')
    location.text = location_list[j]
    print(location.text)

    engine = etree.SubElement(child, 'engine')
    engine.text = fuel_list[j]

    description = etree.SubElement(child, 'description')
    print(f"{j} : ", re.sub(r"..*$", "", description_list[j]))
    description.text = description_list[j]

    mileage = etree.SubElement(child, 'mileage')
    mileage.text = mileage_list[j]

    transmission = etree.SubElement(child, 'transmission')
    transmission.text = transmission_list[j]
    j += 1

s = etree.tostring(root, encoding='unicode')
print(type(s))
tree = etree.ElementTree(root)
tree.write("filename228.xml",  xml_declaration=True, encoding="utf-8")
