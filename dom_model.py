from xml.dom import minidom

doc = minidom.parse("filename.xml")



product = doc.getElementsByTagName("element")
for prod in product:
    main = doc.createElement('ParseDate')
    sub_main = doc.createElement('ParseTime')
    main2 = doc.createElement('ParserName')
    main.setAttribute('optional', 'True')
    main.setAttribute('browser-type', 'Chrome')
    main2.setAttribute('optional', 'True')
    main2.setAttribute('browser-type', 'Chrome')
    prod.appendChild(main)
    prod.appendChild(main2)
    textDate = doc.createTextNode('21.04.2020')
    textTime = doc.createTextNode('9:53')
    textParser = doc.createTextNode('BeautifulSoup')
    main.appendChild(sub_main)
    main.appendChild(textDate)
    main2.appendChild(textParser)
    sub_main.appendChild(textTime)

    decr = prod.getElementsByTagName("title")[0]
    text = prod.getElementsByTagName("location")[0]
    price = prod.getElementsByTagName("price")[0]
    print("описание: %s, location: %s, цена: %s" % (decr.firstChild.data, \
                                                    text.firstChild.data, price.firstChild.data))

print(doc.toprettyxml(indent='\t'))

import lxml.html
from lxml import etree

xslt_doc = etree.parse("filename.xsl")
xslt_transformer = etree.XSLT(xslt_doc)

source_doc = etree.parse("filename.xml")
output_doc = xslt_transformer(source_doc)

print(str(output_doc))
output_doc.write("output-toc.html", pretty_print=True, encoding="utf-8")
