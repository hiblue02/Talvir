#!/usr/bin/python3
print("Content-type:text/html\n")

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
print('''
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<form action="new_test.py" method="post">
<p><textarea cols="70" rows="10" name="query"></textarea></p>
<input type="submit">
</form>
</body>
</html>
''')
