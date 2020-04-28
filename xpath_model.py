from lxml import etree

root = etree.parse('filename.xml')
print(root.findall("."))

# All 'neighbor' grand-children of 'country' children of the top-level
# elements

n = 0
PATH_1 = '//element'
PATH_2 = '//element[@id]/title'
PATH_3 = '//element[@id=1]/title'
PATH_4 = '//element::text()'
PATH_5 = 'numer'
PATH_6 = '(//element/*)[1]'
PATH_7 = '(//element/*)[2]'
PATH_8 = '(//element/*)[3]'
PATH_9 = '//element[contains(title, "Focus")][price < 18000]/title'
PATH_10 = '//element[position( ) mod 5 = 0]/title|//element[position( ) mod 5 = 0]/location'
PATH_11 = '//element[position( ) mod 2 = 0]/price|//element[position( ) mod 2 = 0]/@id'#типы

print ('Number of elements',len(root.findall("//element")))
# Nodes with name='Singapore' that have a 'year' child
titles = root.findall("//title")
print(titles)
for title in titles:             # Iterates through all found links
     title.attrib["title"] = "blank"


# 'year' nodes that are children of nodes with name='Singapore'
root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' nodes that are the second child of their parent
root.findall(".//neighbor[2]")


find_key = etree.XPath("//element[position( ) mod 2 = 0]/price|//element[position( ) mod 2 = 0]/@id")
values_arr = find_key(root)
list_keys = []
for i in range(0, len(values_arr)):
     if(isinstance(values_arr[i],etree._ElementUnicodeResult) ):
          list_keys.append(values_arr[i])
     else:
          list_keys.append(values_arr[i].text)
print (list_keys)