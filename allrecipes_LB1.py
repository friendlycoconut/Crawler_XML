import codecs
import html.parser as htmlparser

import lxml
import requests
from urllib import request, response, error, parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import etree
import re

url = "https://www.allrecipes.com/"#считываем html документ
html = urlopen(url)
soup = BeautifulSoup(html, "lxml")
print(soup)#выводим то что считали
title_list =[]#словари для хранения данных
href_list =[]
ratings_list =[]
authors_list =[]
image_list =[]




titles = soup.find_all('span', { "class" : "fixed-recipe-card__title-link" })#считываем данные для заглавия
for title in titles:
    print(title.get_text())
    title_list.append(title.get_text())

hrefs = soup.find_all('a', { "class" : "ng-isolate-scope" })#считываем ссылки на рецепты
for href in hrefs:
    print(href.get('href'))
    href_list.append(href.get('href'))

ratings = soup.find_all('span', { "class" : "stars" })#считываем рейтинги обьявления
for rate in ratings:
    print(rate.get('aria-label'))
    ratings_list.append(rate.get('aria-label'))

authors = soup.find_all('ul', { "class" : "cook-submitter-info" })#считываем имя автора
for author in authors:
    print(author.get('h4'))
    authors_list.append(author.get_text())

images = soup.find_all('img', { "class" : "fixed-recipe-card__img" })#считываем ссылку на картинку
for image in images:
    print(image.get('data-original-src'))
    image_list.append(image.get('data-original-src'))


print(title_list)#выводим полученые результаты считывания
print(href_list )
print(ratings_list)
print(image_list )
print(authors_list)


i = 0
while i < len(title_list):
    print(title_list[i])
    print(href_list[i])
    print(ratings_list[i])
    print(image_list[i])
    print(authors_list[i])
    i += 1

root = etree.Element('root')#создание корня xml документа
j = 0
while j < len(title_list):
    child = etree.SubElement(root,'element', id = str(j+1))#создание елемента - обьявления

    title1 = etree.SubElement(child, 'title')#заглавие
    title1.text= title_list[j]

    price = etree.SubElement(child, 'href')
    price.text = href_list[j]

    location = etree.SubElement(child, 'ratings')
    location.text = ratings_list[j]
    print(location.text)

    engine = etree.SubElement(child, 'image')
    engine.text = image_list[j]


    mileage = etree.SubElement(child, 'author')
    mileage.text = authors_list[j]


    j += 1

s = etree.tostring(root, encoding='unicode')#перевод кодировки

tree = etree.ElementTree(root)
tree.write("parsed_allrecipes.xml",  xml_declaration=True, encoding="utf-8")#сохранение файла



xml_file = lxml.etree.parse("parsed_allrecipes.xml")#валидация файлов
xml_file_not_valid = lxml.etree.parse("parsed_allrecipes_notvalid.xml")
xml_validator = lxml.etree.XMLSchema(file="parsed_allrecipes.xsd")

is_valid = xml_validator.validate(xml_file)#нужно обновить xsd файл
is_not_valid = xml_validator.validate(xml_file_not_valid)


print(is_valid)#вывод валидности
print(is_not_valid)


