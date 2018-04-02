import ftplib
import pymssql
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF, RDF, RDFS

g = Graph()

g.bind("rdf", RDF)
g.bind("rdfs", RDFS)

conn = pymssql.connect(host='digerati.aks.ac.kr', user='PCN', password='since_2017', database='PCN')

cur = conn.cursor()
cur.execute("select id, category, label from ca_nodes")
nodes = cur.fetchall()


nodeslist = [];

for i in nodes:
    node_id = i[0]
    category = i[1]
    label = i[2]
    id_temp = URIRef("http://dh.aks.ac.kr/ontologies/cocktail/cock#{}".format(i[0]))
    category_temp = URIRef("http://dh.aks.ac.kr/ontologies/cocktail/cock#{}".format(i[1]))
    label_temp = URIRef("http://dh.aks.ac.kr/ontologies/cocktail/cock#{}".format(i[2]))
    nodeslist.append([id_temp, category_temp, label_temp])

# print(nodeslist)
# print(node_id)

cur = conn.cursor()
cur.execute("select src, relation, target  from ca_links")
links = cur.fetchall()

linkslist = [];

for i in links:
    src = i[0]
    relation = i[1]
    target = i[2]
    src = URIRef("http://dh.aks.ac.kr/ontologies/cocktail/cock#{}".format(i[0]))
    relation = URIRef("http://dh.aks.ac.kr/ontologies/cocktail/cock#{}".format(i[1]))
    target = URIRef("http://dh.aks.ac.kr/ontologies/cocktail/cock#{}".format(i[2]))
    linkslist.append([src, relation, target])

#Class-ID, ID-Label
for i in nodeslist:
    # nodes[0] = BNode()
    # nodes[1] = BNode()
    g.add((i[0], RDF.type, i[1]))
    g.add((i[0], RDFS.label, i[2]))

# ID-ID
for i in linkslist:
    g.add((i[0], i[1], i[2]))
xml_temp = g.serialize(format='xml')
output = xml_temp.decode("utf-8")

# print(d)
#
f = open("cocktail.rdf", 'w', encoding='utf-8')
f.write(output)
