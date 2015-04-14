from rdflib import Graph, URIRef

g = Graph()
g.parse("http://dbpedia.org/resource/Elvis_Presley")
len(g)
for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/spouse")):
    print "the person represented by", str(stmt[0]), "was married to", str(stmt[1])

for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/birthDate")):
    print "the person represented by", str(stmt[0]), "was born on", str(stmt[1])

for stmt in g.subject_objects(URIRef("http://dbpedia.org/ontology/thumbnail")):
     print stmt[1]


