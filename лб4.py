import rdflib

g = rdflib.Graph()
g.parse('Lb4.rdf')

print("This graph has got %s statements." % len(g))

for subj, pred, obj in g:
   if (subj, pred, obj) not in g:
       raise Exception("Iterator / Container Protocols are Broken!!")

print("Вывод всех трилетов 'субъект-предикат-объект':")
for subj, pred, obj in g:
    print((subj,pred,obj))

qres = g.query(
    """SELECT  ?x ?title ?description
        WHERE   
        { ?x dc:language ?language
          FILTER regex(?language, "^en").
          ?x dc:title ?title.
          ?x dc:description ?description
        }""")

print("Список всех англоязычных страниц с их соответствующим описанием:")
for row in qres:
 print(row)








