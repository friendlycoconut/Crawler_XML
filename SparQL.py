import rdflib

g = rdflib.Graph()
g.parse('old_rdf.rdf')
print("Вывод числа триплетов")
qres = g.query(
    """SELECT (COUNT(*) AS ?amount) 
        WHERE { ?s ?p ?o } """)
for row in qres:
    print(row)


print("Вывод названия одного ресурса")
qres2 = g.query(
    """SELECT  ?title 
        WHERE   
        { <https://auto.ria.com/1> my:Title ?title } """)

for row in qres2:
    print(row)

print("Вывод список всех ресурсов одного сложного класса")
qres3 = g.query(
    """PREFIX my: <https://auto.ria.com#>
       SELECT  ?resource
        WHERE   
        { ?resource rdf:type my:Mustang} """)

for row in qres3:
    print(row)

print("Вывод информации по одной из х-к")
qres4 = g.query(
    """SELECT  ?description
        WHERE   
        { 
          ?x dc:description ?description
        }""")

for row in qres4:
    print(row)

qres5 = g.query(
    """PREFIX my:<https://auto.ria.com#>
       SELECT ?class
       WHERE {
        ?class rdfs:subClassOf my:Vehicle
        }""")
print('Вивести назви всіх підкласів для базового класу')
for row in qres5:
    print(row)


qres6 = g.query(
    """SELECT  ?x ?title ?description ?language
        WHERE   
        { ?x dc:lang ?language
          FILTER regex(?language, "^Ua").
          ?x my:Title ?title.
          ?x dc:description ?description
        }""")
print("Вывод с описанием всех ua обьявлений:")
for row in qres6:
    print(row)

print("Вывод с описанием всех  обьявлений с бензиновым двигателем и AKP:")
qres = g.query(
    """SELECT  ?x  ?fuelType ?transmission
           WHERE   
           { ?x my:Transmission ?transmission
             FILTER  regex(?transmission, "^AKP").
             ?x my:FuelType ?fuelType
             FILTER  regex(?fuelType, "^Benzin").
           
           }""")
for row in qres:
    print(row)


