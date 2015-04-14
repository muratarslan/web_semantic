from SPARQLWrapper import SPARQLWrapper, JSON

term = "Kyrenia"
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
	SELECT ?loc WHERE {<http://dbpedia.org/resource/%s>
		<http://dbpedia.org/ontology/populationTotal> ?loc .
	}	
"""%(term))

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

try:
	loc = results.values()[1]['bindings'][0]['loc']['value']
except IndexError:
	loc = " "

print loc

