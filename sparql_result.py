#!/usr/bin/python3
print("content-type:text/html\n")
import rdflib
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF, RDF, RDFS
import cgi

g = rdflib.Graph()

g.parse("cocktail.rdf")

g.bind("rdf", RDF)
g.bind("rdfs", RDFS)
cock = Namespace('http://dh.aks.ac.kr/ontologies/cocktail/cock#')
g.bind("cock", cock)

form = cgi.FieldStorage()
query_text = form["query"].value
qres = g.query('''{}'''.format(query_text))
for row in qres:
    if len(row) == 1:
        print(row[0])
    elif len(row) == 2:
        print("{0},{1}\n".format(row[0], row[1]))
    else:
        print("{0},{1},{2}\n".format(row[0], row[1], row[2]))
