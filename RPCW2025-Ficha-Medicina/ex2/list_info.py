from rdflib import Graph, Namespace
from pprint import pprint

g = Graph()
g.parse("12med_doentes.ttl")

namespace = Namespace("http://example.org/medicina#")

# 13. (doença, nº de doentes)
q1 = """
SELECT ?d (COUNT(?p) AS ?numPatients)
WHERE {
    ?p a :Patient .
    ?p :hasDisease ?d .
}
GROUP BY ?d
"""
result1 = [(str(row.d).split("#")[-1], int(row.numPatients)) for row in g.query(q1)]
result1 = sorted(result1, key=lambda x: x[1], reverse=True)
print("Distribuição dos doentes pelas doenças:")
pprint(result1)

# 14. (sintoma, nº de doenças com o sintoma)
q2 = """
SELECT ?s (COUNT(?d) AS ?numDiseases)
WHERE {
    ?d a :Disease .
    ?d :hasSymptom ?s .
}
GROUP BY ?s
"""
result2 = [(str(row.s).split("#")[-1], int(row.numDiseases)) for row in g.query(q2)]
result2 = sorted(result2, key=lambda x: x[1], reverse=True)
print("\nDistribuição das doenças pelos sintomas:")
pprint(result2)

# 15. (tratamento, nº de doenças com o tratamento)
q3 = """
SELECT ?t (COUNT(?d) AS ?numDiseases)
WHERE {
    ?d a :Disease .
    ?d :hasTreatment ?t .
}
GROUP BY ?t
"""
result3 = [(str(row.t).split("#")[-1], int(row.numDiseases)) for row in g.query(q3)]
result3 = sorted(result3, key=lambda x: x[1], reverse=True)
print("\nDistribuição das doenças pelos tratamentos:")
pprint(result3)