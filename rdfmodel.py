import rdflib

g = rdflib.Graph()
g.parse('rdf_data.rdf')

print("This graph has got %s statements." % len(g))

for subj, pred, obj in g:
   if (subj, pred, obj) not in g:
       raise Exception("Iterator / Container Protocols are Broken!!")

print("Вывод всех трилетов 'субъект-предикат-объект':")
for subj, pred, obj in g:
    print((subj,pred,obj))
#обьект модель
qres = g.query(
    """SELECT ?x  ?title ?lang
        WHERE   
        { ?x dc:lang ?lang
          FILTER regex(?lang, "^en").
          ?x dc:title ?title.
          ?x dc:lang ?lang
        }""")

print("Список всех англоязычных страниц с их соответствующим описанием:")
for row in qres:
 print(row)









