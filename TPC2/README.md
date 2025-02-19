# a. Quantos triplos existem na Ontologia?

## SPARQL Query
```sparql
SELECT (COUNT(*) AS ?totalTriples) WHERE {  
    ?s ?p ?o .  
}
```

## Resultado
| No. | totalTriples     |
|-----|------------------|
| 1   | 6603             |


# b. Que classes estão definidas?

## SPARQL Query
```sparql
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT DISTINCT ?prop WHERE {
    ?s a :Rei .
    ?s ?prop ?o .
}
ORDER BY ?prop
```
## Resultado

| No. | class                                                                                              |
|-----|----------------------------------------------------------------------------------------------------|
| 1   | rdf:Property                                                                                       |
| 2   | rdfs:Class                                                                                        |
| 3   | rdfs:Resource                                                                                     |
| 4   | owl:SymmetricProperty                                                                              |
| 5   | owl:TransitiveProperty                                                                             |
| 6   | owl:AsymmetricProperty                                                                             |
| 7   | owl:Class                                                                                         |
| 8   | owl:Thing                                                                                         |
| 9   | owl:AllDisjointProperties                                                                          |
| 10  | owl:ObjectProperty                                                                                 |
| 11  | owl:DatatypeProperty                                                                               |
| 12  | owl:ReflexiveProperty                                                                               |
| 13  | owl:IrreflexiveProperty                                                                           |
| 14  | owl:NamedIndividual                                                                                |
| 15  | owl:AllDisjointClasses                                                                             |
| 16  | owl:Nothing                                                                                        |
| 17  | rdf:List                                                                                          |
| 18  | rdf:Statement                                                                                     |
| 19  | rdfs:Literal                                                                                      |
| 20  | rdf:Alt                                                                                           |
| 21  | rdfs:Container                                                                                   |
| 22  | rdf:Bag                                                                                           |
| 23  | rdf:Seq                                                                                           |
| 24  | rdfs:ContainerMembershipProperty                                                                   |
| 25  | rdf:XMLLiteral                                                                                     |
| 26  | rdfs:Datatype                                                                                     |
| 27  | owl:AllDifferent                                                                                  |
| 28  | owl:Annotation                                                                                     |
| 29  | owl:AnnotationProperty                                                                              |
| 30  | owl:Axiom                                                                                         |
| 31  | owl:DataRange                                                                                     |
| 32  | owl:DeprecatedClass                                                                                |
| 33  | owl:DeprecatedProperty                                                                             |
| 34  | owl:FunctionalProperty                                                                             |
| 35  | owl:InverseFunctionalProperty                                                                      |
| 36  | owl:NegativePropertyAssertion                                                                       |
| 37  | owl:Ontology                                                                                       |
| 38  | owl:OntologyProperty                                                                                |
| 39  | owl:Restriction                                                                                    |
| 40  | xsd:nonNegativeInteger                                                                              |
| 41  | xsd:anyURI                                                                                         |
| 42  | xsd:base64Binary                                                                                    |
| 43  | xsd:boolean                                                                                         |
| 44  | xsd:byte                                                                                            |
| 45  | xsd:dateTime                                                                                        |
| 46  | xsd:dateTimeStamp                                                                                  |
| 47  | xsd:decimal                                                                                         |
| 48  | xsd:double                                                                                         |
| 49  | xsd:float                                                                                          |
| 50  | xsd:hexBinary                                                                                      |
| 51  | xsd:int                                                                                            |
| 52  | xsd:integer                                                                                       |
| 53  | xsd:language                                                                                       |
| 54  | xsd:long                                                                                           |
| 55  | xsd:Name                                                                                           |
| 56  | xsd:NCName                                                                                         |
| 57  | xsd:negativeInteger                                                                                 |
| 58  | xsd:NMTOKEN                                                                                       |
| 59  | xsd:nonPositiveInteger                                                                              |
| 60  | xsd:normalizedString                                                                                |
| 61  | rdf:PlainLiteral                                                                                    |
| 62  | xsd:positiveInteger                                                                                 |
| 63  | owl:rational                                                                                        |
| 64  | owl:real                                                                                            |
| 65  | xsd:short                                                                                          |
| 66  | xsd:string                                                                                         |
| 67  | xsd:token                                                                                          |
| 68  | xsd:unsignedByte                                                                                   |
| 69  | xsd:unsignedInt                                                                                    |
| 70  | xsd:unsignedLong                                                                                   |
| 71  | xsd:unsignedShort                                                                                  |
| 72  | historia:Rainha                                                                                   |
| 73  | historia:Monarca                                                                                  |
| 74  | _:node1                                                                                           |
| 75  | _:node3                                                                                           |
| 76  | historia:Casa                                                                                     |
| 77  | historia:Individuo                                                                                 |
| 78  | historia:Regime                                                                                   |
| 79  | historia:Batalha                                                                                  |
| 80  | historia:Acontecimento                                                                             |
| 81  | historia:Partido                                                                                  |
| 82  | historia:Dinastia                                                                                 |
| 83  | historia:Descobrimento                                                                             |
| 84  | historia:Local                                                                                     |
| 85  | historia:Reinado                                                                                   |
| 86  | _:node5                                                                                           |
| 87  | _:node6                                                                                           |
| 88  | _:node7                                                                                           |
| 89  | _:node8                                                                                           |
| 90  | _:node9                                                                                           |
| 91  | _:node10                                                                                          |
| 92  | _:node11                                                                                          |
| 93  | _:node12                                                                                          |
| 94  | _:node14                                                                                          |
| 95  | historia:Conquista                                                                                 |
| 96  | historia:Mandato                                                                                  |
| 97  | historia:Rei                                                                                      |
| 98  | _:node16                                                                                          |
| 99  | _:node18                                                                                          |
| 100 | historia:Presidente                                                                                |
| 101 | _:node20                                                                                          |
| 102 | _:node22                                                                                          |

# c. Que propriedades tem a classe "Rei"?

## SPARQL Query
```sparql
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT DISTINCT ?prop WHERE {
    ?s a :Rei .
    ?s ?prop ?o .
}
ORDER BY ?prop
```

## Resultado
| No. | Propriedade             |
|-----|-------------------------|
| 1   | :ascendente             |
| 2   | :casa                   |
| 3   | :cognomes               |
| 4   | :descendente            |
| 5   | :enterro                |
| 6   | :localNascimento        |
| 7   | :morte                  |
| 8   | :nascimento             |
| 9   | :nome                   |
| 10  | :notas                  |
| 11  | :posicao                |
| 12  | :predecessor            |
| 13  | :sucessor               |
| 14  | :temReinado             |
| 15  | rdf:type                |
| 16  | owl:topObjectProperty   |




d. Quantos reis aparecem na ontologia?
e. Calcula uma tabela com o seu nome, data de nascimento e cognome.
f. Acrescenta à tabela anterior a dinastia em que cada rei reinou.
g. Qual a distribuição de reis pelas 4 dinastias?
h. Lista os descobrimentos (sua descrição) por ordem cronológica.
i. Lista as várias conquistas, nome e data, juntamento com o nome que reinava no momento.
j. Calcula uma tabela com o nome, data de nascimento e número de mandatos de todos os presidentes portugueses.
k. Quantos mandatos teve o presidente Sidónio Pais? Em que datas iniciaram e terminaram esses mandatos?
l. Quais os nomes dos partidos políticos presentes na ontologia? Qual a distribuição dos militantes por cada partido político? n. Qual o partido com maior número de presidentes militantes?
m. Qual a distribuição dos militantes por cada partido político?
n. Qual o partido com maior número de presidentes militantes? 
