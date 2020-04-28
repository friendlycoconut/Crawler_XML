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
PATH_5 = '//element[contains(location, str)][contains(location, " ")]/@id'
PATH_6 = '(//element/*)[1]'
PATH_7 = '(//element/*)[2]'
PATH_8 = '(//element/*)[3]'
PATH_9 = '//element[contains(title, "Focus")][price < 18000]/title'
PATH_10 = '//element[position( ) mod 5 = 0]/title|//element[position( ) mod 5 = 0]/location'
PATH_11 = '//element[position( ) mod 2 = 0]/price|//element[position( ) mod 2 = 0]/@id'#типы

print ('\n Number of elements \n',len(root.findall(PATH_1)))

#info for all complex attributes
find_key = etree.XPath(PATH_2)
values_arr = find_key(root)
list_keys = []
for i in range(0, len(values_arr)):
     if(isinstance(values_arr[i],etree._ElementUnicodeResult) ):
          list_keys.append(values_arr[i])
     else:
          list_keys.append(values_arr[i].text)
print ('\n інформація за однією із характеристик для всіх описаних складних елементів \n ',list_keys)

#info for one complex attribute
find_key = etree.XPath(PATH_3)
values_arr = find_key(root)
list_keys = []
for i in range(0, len(values_arr)):
     if(isinstance(values_arr[i],etree._ElementUnicodeResult) ):
          list_keys.append(values_arr[i])
     else:
          list_keys.append(values_arr[i].text)
print ('\n ***інформація за однією із характеристик для одного складного елементу ****\n',list_keys)

#info for one complex attribute
find_key = etree.XPath(PATH_5)
values_arr = find_key(root)
list_keys = []
for i in range(0, len(values_arr)):
     list_keys.append(values_arr[i])
print ('\n ***номер елемента, назва якого складається більше, ніж із одного слова ****\n',list_keys)

#info for one complex attribute
find_key = etree.XPath(PATH_6)
values_arr = find_key(root)
list_keys = []
for i in range(0, len(values_arr)):
     if(isinstance(values_arr[i],etree._ElementUnicodeResult) ):
          list_keys.append(values_arr[i])
     else:
          list_keys.append(values_arr[i].text)
print ('\nтільки перший параметр одного складного елемента\n',list_keys)

find_key = etree.XPath(PATH_7)
values_arr = find_key(root)
list_keys = []
for i in range(0, len(values_arr)):
     if(isinstance(values_arr[i],etree._ElementUnicodeResult) ):
          list_keys.append(values_arr[i])
     else:
          list_keys.append(values_arr[i].text)
print ('\nтільки другий параметр одного складного елемента\n',list_keys)

find_key = etree.XPath(PATH_8)
values_arr = find_key(root)
list_keys = []
for i in range(0, len(values_arr)):
     if(isinstance(values_arr[i],etree._ElementUnicodeResult) ):
          list_keys.append(values_arr[i])
     else:
          list_keys.append(values_arr[i].text)
print ('\nтільки третій параметр одного складного елемента\n',list_keys)

find_key = etree.XPath(PATH_9)
values_arr = find_key(root)
list_keys = []
for i in range(0, len(values_arr)):
     if(isinstance(values_arr[i],etree._ElementUnicodeResult) ):
          list_keys.append(values_arr[i])
     else:
          list_keys.append(values_arr[i].text)
print ('\nназву елемента, якщо його ціна (або кількість відгуків, зірочок, тощо) знаходиться в заданому діапазоні4, а також містить задану послідовність літер у назві\n',list_keys)

find_key = etree.XPath(PATH_10)
values_arr = find_key(root)
list_keys = []
for i in range(0, len(values_arr)):
     if(isinstance(values_arr[i],etree._ElementUnicodeResult) ):
          list_keys.append(values_arr[i])
     else:
          list_keys.append(values_arr[i].text)
print ('\nінформацію1 за двома параметрами кожного п’ятого елемента\n',list_keys)

find_key = etree.XPath(PATH_11)
values_arr = find_key(root)
list_keys = []
for i in range(0, len(values_arr)):
     if (isinstance(values_arr[i], etree._ElementUnicodeResult)):
          list_keys.append(values_arr[i])
     else:
          list_keys.append(values_arr[i].text)
print ('\nномер елементу (товару, послуги тощо) та додатково, ще один параметр (напр. ціна) для кожного другого складного елемента в документі.\n',list_keys)