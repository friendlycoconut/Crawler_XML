from xml.dom import minidom

file_read = minidom.parse("parsed_allrecipes.xml")



product = file_read.getElementsByTagName("element")#вывод всех елементов
for prod in product:
    recommended_var = file_read.createElement('Recommended')#создание нового елемента
    recommended_var.setAttribute('optional', 'True')#созданние новых атрибутов
    recommended_var.setAttribute('recommendedBy', 'FC Chief')
    recommended_text = file_read.createTextNode('TRUE')#создание текстового зничения поля
    recommended_var.appendChild(recommended_text)


    sub_recommended = file_read.createElement('RecipeFoTheDay')#создание нового елемента (тега)
    recommended_var.appendChild(sub_recommended)
    textTime = file_read.createTextNode('day of 04/29/20')#создание текстового значения поля
    sub_recommended.appendChild(textTime)

    borsch = file_read.createElement('BetterThanBorsch')#создание нового тега (елемента)

    borsch.setAttribute('required', 'True')
    borsch.setAttribute('attr-type', 'Validation')
    prod.appendChild(recommended_var)
    prod.appendChild(borsch)


    borschText = file_read.createTextNode('FALSE')


    borsch.appendChild(borschText)


    decr = prod.getElementsByTagName("title")[0]#вывод всех нод
    href_link = prod.getElementsByTagName("href")[0]
    ratings = prod.getElementsByTagName("ratings")[0]
    image = prod.getElementsByTagName("image")[0]
    author = prod.getElementsByTagName("author")[0]
    print("описание: %s, ссылка: %s, рейтинг: %s, ссылка на изображение: %s, автор: %s" % (decr.firstChild.data, \
                                                                                           href_link.firstChild.data, ratings.firstChild.data,
                                                                                           image.firstChild.data, author.firstChild.data))

print(file_read.toprettyxml(indent='\t'))

import lxml.html
from lxml import etree

xslt_doc = etree.parse("parsed_allrecipes.xsl")#парсинг таблицы стилей
xslt_transformer = etree.XSLT(xslt_doc)

source_doc = etree.parse("parsed_allrecipes.xml")
output_doc = xslt_transformer(source_doc)#преобразование документа в веб странцу

print(str(output_doc))
output_doc.write("parsed_allrecipes.html", pretty_print=True, encoding="utf-8")
