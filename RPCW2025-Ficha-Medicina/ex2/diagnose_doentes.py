from rdflib import Graph
g = Graph()
g.parse("med_doentes.ttl")

# patient has disease if it has at least 3 symptoms in common with the disease
q = """
CONSTRUCT {
    ?p :hasDisease ?d .
}
WHERE {
    ?p a :Patient .
    ?d a :Disease .
    ?d :hasSymptom ?s1 .
    ?p :exhibitsSymptom ?s1 .
    ?d :hasSymptom ?s2 .
    ?p :exhibitsSymptom ?s2 .
    ?d :hasSymptom ?s3 .
    ?p :exhibitsSymptom ?s3 .

    FILTER (?s1 != ?s2 && ?s1 != ?s3 && ?s2 != ?s3)
}
"""
for r in g.query(q):
    g.add(r)

print(g.serialize())