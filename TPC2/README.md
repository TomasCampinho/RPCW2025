# TPC2: Descarregar o dataset sobre a História de Portugal e sobre ele responder às seguintes questões:

## a. Quantos triplos existem na Ontologia?

### SPARQL Query
```sparql
SELECT (COUNT(*) AS ?totalTriples) WHERE {  
    ?s ?p ?o .  
}
```

### Resultado
|     | totalTriples     |
|-----|------------------|
| 1   | 6603             |


## b. Que classes estão definidas?

### SPARQL Query
```sparql
PREFIX owl: <http://www.w3.org/2002/07/owl#>
SELECT DISTINCT ?class WHERE {  
    ?class a owl:Class .  
}
```

### Resultado
|     | class                                |
|-----|--------------------------------------|
| 1   | rdf:Property                         |
| 2   | rdfs:Class                           |
| 3   | rdfs:Resource                        |
| 4   | owl:SymmetricProperty                |
| 5   | owl:TransitiveProperty               |
| 6   | owl:AsymmetricProperty               |
| 7   | owl:Class                            |
| 8   | owl:Thing                            |
| 9   | owl:AllDisjointProperties            |
| 10  | owl:ObjectProperty                   |
| 11  | owl:DatatypeProperty                 |
| 12  | owl:ReflexiveProperty                |
| 13  | owl:IrreflexiveProperty              |
| 14  | owl:NamedIndividual                  |
| 15  | owl:AllDisjointClasses               |
| 16  | owl:Nothing                          |
| 17  | rdf:List                             |
| 18  | rdf:Statement                        |
| 19  | rdfs:Literal                         |
| 20  | rdf:Alt                              |
| 21  | rdfs:Container                       |
| 22  | rdf:Bag                              |
| 23  | rdf:Seq                              |
| 24  | rdfs:ContainerMembershipProperty     |
| 25  | rdf:XMLLiteral                       |
| 26  | rdfs:Datatype                        |
| 27  | owl:AllDifferent                     |
| 28  | owl:Annotation                       |
| 29  | owl:AnnotationProperty               |
| 30  | owl:Axiom                            |
| 31  | owl:DataRange                        |
| 32  | owl:DeprecatedClass                  |
| 33  | owl:DeprecatedProperty               |
| 34  | owl:FunctionalProperty               |                                                              
| 35  | owl:InverseFunctionalProperty        |
| 36  | owl:NegativePropertyAssertion        |
| 37  | owl:Ontology                         |
| 38  | owl:OntologyProperty                 |                                                            
| 39  | owl:Restriction                      |                                                      
| 40  | xsd:nonNegativeInteger               |                                                      
| 41  | xsd:anyURI                           |                                                             
| 42  | xsd:base64Binary                     |                                                      
| 43  | xsd:boolean                          |                                                              
| 44  | xsd:byte                             |                                                              
| 45  | xsd:dateTime                         |                                                               
| 46  | xsd:dateTimeStamp                    |                                                              
| 47  | xsd:decimal                          |                                                               
| 48  | xsd:double                           |                                                            
| 49  | xsd:float                            |                                                             
| 50  | xsd:hexBinary                        |                                                             
| 51  | xsd:int                              |                                                             
| 52  | xsd:integer                          |                                                            
| 53  | xsd:language                         |                                                             
| 54  | xsd:long                             |                                                             
| 55  | xsd:Name                             |                                                             
| 56  | xsd:NCName                           |                                                             
| 57  | xsd:negativeInteger                  |                                                              
| 58  | xsd:NMTOKEN                          |                                                           
| 59  | xsd:nonPositiveInteger               |                                                             
| 60  | xsd:normalizedString                 |                                                              
| 61  | rdf:PlainLiteral                     |                                                             
| 62  | xsd:positiveInteger                  |                                                              
| 63  | owl:rational                         |                                                              
| 64  | owl:real                             |                                                              
| 65  | xsd:short                            |                                                             
| 66  | xsd:string                           |                                                             
| 67  | xsd:token                            |                                                             
| 68  | xsd:unsignedByte                     |                                                             
| 69  | xsd:unsignedInt                      |                                                            
| 70  | xsd:unsignedLong                     |                                                             
| 71  | xsd:unsignedShort                    |                                                             
| 72  | historia:Rainha                      |                                                            
| 73  | historia:Monarca                     |                                                            
| 74  | _:node1                              |                                                            
| 75  | _:node3                              |                                                            
| 76  | historia:Casa                        |                                                            
| 77  | historia:Individuo                   |                                                             
| 78  | historia:Regime                      |                                                            
| 79  | historia:Batalha                     |                                                            
| 80  | historia:Acontecimento               |                                                            
| 81  | historia:Partido                     |                                                            
| 82  | historia:Dinastia                    |                                                            
| 83  | historia:Descobrimento               |                                                             
| 84  | historia:Local                       |                                                             
| 85  | historia:Reinado                     |                                                             
| 86  | _:node5                              |                                                            
| 87  | _:node6                              |                                                            
| 88  | _:node7                              |                                                            
| 89  | _:node8                              |                                                            
| 90  | _:node9                              |                                                            
| 91  | _:node10                             |                                                            
| 92  | _:node11                             |                                                            
| 93  | _:node12                             |                                                            
| 94  | _:node14                             |                                                           
| 95  | historia:Conquista                   |                                                             
| 96  | historia:Mandato                     |                                                            
| 97  | historia:Rei                         |                                                            
| 98  | _:node16                             |                                                            
| 99  | _:node18                             |                                                            
| 100 | historia:Presidente                  |                                                            
| 101 | _:node20                             |
| 102 | _:node22                             |                                                            


## c. Que propriedades tem a classe "Rei"?

### SPARQL Query
```sparql
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT DISTINCT ?prop WHERE {
    ?s a :Rei .
    ?s ?prop ?o .
}
ORDER BY ?prop
```

### Resultado
|     | Propriedade             |
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

## d. Quantos reis aparecem na ontologia?

### SPARQL Query
```sparql
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT (COUNT(*) AS ?totalReis) WHERE {
    ?s a :Rei .
}
```

### Resultado
|     | totalReis      |
|-----|----------------|
| 1   | totalReis      |


## e. Calcula uma tabela com o seu nome, data de nascimento e cognome.

### SPARQL Query
```sparql
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT ?nome ?nascimento ?cognomes WHERE {
    ?s a :Rei .
    ?s :nome ?nome .              
    ?s :nascimento ?nascimento .
    ?s :cognomes ?cognomes . 
}
ORDER BY ?nome
```

### Resultado
|     | nome           | nascimento             | cognomes                                                                                 |
|-----|----------------|------------------------|------------------------------------------------------------------------------------------|
| 1   | D. Afonso I    | 1109                   | O Conquistador, O Fundador, O Grande                                                     |
| 2   | D. Afonso II   | 23 de abril de 1185    | O Gordo, O Crasso, O Gafo, O Legislador                                                  |
| 3   | D. Afonso III  | 5 de maio de 1210      | O Bolonhês                                                                               |
| 4   | D. Afonso IV   | 8 de fevereiro de 1291 | O Bravo                                                                                  |
| 5   | D. Afonso V    | 15 de janeiro de 1432  | O Africano                                                                               |
| 6   | D. Afonso VI   | 21 de agosto de 1643   | O Vitorioso, O Prisioneiro                                                               |
| 7   | D. Carlos I    | 28 de setembro de 1863 | O Diplomata, O Martirizado, O Mártir, O Oceanógrafo, O Rei-Pintor                        |
| 8   | D. Dinis I     | 9 de outubro de 1261   | O Lavrador, O Rei-Trovador, O Rei-Poeta, O Rei-Agricultor                                |
| 9   | D. Duarte I    | 31 de outubro de 1391  | O Eloquente, O Rei-Filósofo                                                              |
| 10  | D. Fernando I  | 31 de outubro de 1345  | O Formoso, O Belo, O Inconstante, O Inconsciente                                         |
| 11  | D. Henrique I  | 31 de janeiro de 1512  | O Casto, O Cardeal-Rei, O Eborense/O de Évora                                            |
| 12  | D. José I      | 6 de junho de 1714     | O Reformador                                                                             |
| 13  | D. João I      | 11 de abril de 1357    | O da Boa Memória                                                                         |
| 14  | D. João II     | 3 de março de 1455     | O Príncipe Perfeito, O Tirano                                                            |
| 15  | D. João III    | 7 de junho de 1502     | O Piedoso, O Pio                                                                         |
| 16  | D. João IV     | 19 de março de 1604    | O Restaurador, O Afortunado                                                              |
| 17  | D. João V      | 22 de outubro de 1689  | O Magnânimo, O Magnífico, O Rei-Sol Português, O Freirático                              |
| 18  | D. João VI     | 13 de maio de 1767     | O Clemente                                                                               |
| 19  | D. Luís I      | 31 de outubro de 1838  | O Popular, O Bom, O Rei-Marinheiro                                                       |
| 20  | D. Manuel I    | 31 de maio de 1469     | O Venturoso, O Bem-Aventurado, O Pomposo                                                 |
| 21  | D. Manuel II   | 15 de novembro de 1889 | O Patriota, O Desventurado, O Estudioso, O Bibliófilo, O Rei-Saudade                     |
| 22  | D. Miguel I    | 26 de outubro de 1802  | O Rei Absoluto, O Absolutista, O Tradicionalista, O Usurpador                            |
| 23  | D. Pedro I     | 8 de abril de 1320     | O Justiceiro, O Cruel, O Cru, O Vingativo, O Tartamudo, O Até-ao-Fim-do-Mundo-Apaixonado |
| 24  | D. Pedro II    | 26 de abril de 1648    | O Pacífico                                                                               |
| 25  | D. Pedro IV    | 12 de outubro de 1798  | O Rei-Soldado, O Rei-Imperador, O Libertador                                             |
| 26  | D. Pedro V     | 16 de setembro de 1837 | O Esperançoso, O Bem-Amado, O Muito Amado                                                |
| 27  | D. Sancho I    | 11 de novembro de 1154 | O Povoador                                                                               |
| 28  | D. Sancho II   | 8 de setembro de 1209  | O Capelo, O Piedoso, O Pio                                                               |
| 29  | D. Sebastião I | 20 de janeiro de 1554  | O Desejado, O Encoberto, O Adormecido                                                    |
| 30  | Filipe I       | 21 de maio de 1527     | O Prudente                                                                               |
| 31  | Filipe II      | 14 de abril de 1578    | O Pio, O Piedoso                                                                         |
| 32  | Filipe III     | 8 de abril de 1605     | O Grande                                                                                 |


## f. Acrescenta à tabela anterior a dinastia em que cada rei reinou.

### SPARQL Query
```sparql
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT DISTINCT ?nome ?nascimento ?cognomes ?dinastiaNome WHERE {
    ?s a :Rei ;
       :nome ?nome ;
       :nascimento ?nascimento ;
       :cognomes ?cognomes ;
       :temReinado ?reinado .

    ?reinado :dinastia ?dinastia .
    ?dinastia :nome ?dinastiaNome .
}
ORDER BY ?dinastiaNome
```

### Resultado
| No. | Nome               | Nascimento               | Cognomes                                                                                 | Dinastia Nome                               |
|-----|--------------------|--------------------------|------------------------------------------------------------------------------------------|---------------------------------------------|
|  1  | Filipe I           | 21 de maio de 1527       | O Prudente                                                                               | Dinastia Filipina                           |
|  2  | Filipe II          | 14 de abril de 1578      | O Pio, O Piedoso                                                                         | Dinastia Filipina                           | 
|  3  | Filipe III         | 8 de abril de 1605       | O Grande                                                                                 | Dinastia Filipina                           |
|  4  | D. Manuel I        | 31 de maio de 1469       | O Venturoso, O Bem-Aventurado, O Pomposo                                                 | Dinastia de Avis / Dinastia Joanina         |
|  5  | D. João I          | 11 de abril de 1357      | O da Boa Memória                                                                         | Dinastia de Avis / Dinastia Joanina         |
|  6  | D. Duarte I        | 31 de outubro de 1391    | O Eloquente, O Rei-Filósofo                                                              | Dinastia de Avis / Dinastia Joanina         |
|  7  | D. Afonso V        | 15 de janeiro de 1432    | O Africano                                                                               | Dinastia de Avis / Dinastia Joanina         |
|  8  | D. João II         | 3 de março de 1455       | O Príncipe Perfeito, O Tirano                                                            | Dinastia de Avis / Dinastia Joanina         |
|  9  | D. João III        | 7 de junho de 1502       | O Piedoso, O Pio                                                                         | Dinastia de Avis / Dinastia Joanina         |
| 10  | D. Sebastião I     | 20 de janeiro de 1554    | O Desejado, O Encoberto, O Adormecido                                                    | Dinastia de Avis / Dinastia Joanina         |
| 11  | D. Henrique I      | 31 de janeiro de 1512    | O Casto, O Cardeal-Rei, O Eborense/O de Évora                                            | Dinastia de Avis / Dinastia Joanina         |
| 12  | D. Pedro I         | 8 de abril de 1320       | O Justiceiro, O Cruel, O Cru, O Vingativo, O Tartamudo, O Até-ao-Fim-do-Mundo-Apaixonado | Dinastia de Borgonha / Dinastia Afonsina    |
| 13  | D. Afonso IV       | 8 de fevereiro de 1291   | O Bravo                                                                                  | Dinastia de Borgonha / Dinastia Afonsina    |
| 14  | D. Dinis I         | 9 de outubro de 1261     | O Lavrador, O Rei-Trovador, O Rei-Poeta, O Rei-Agricultor                                | Dinastia de Borgonha / Dinastia Afonsina    |
| 15  | D. Afonso III      | 5 de maio de 1210        | O Bolonhês                                                                               | Dinastia de Borgonha / Dinastia Afonsina    |
| 16  | D. Afonso II       | 23 de abril de 1185      | O Gordo, O Crasso, O Gafo, O Legislador                                                  | Dinastia de Borgonha / Dinastia Afonsina    |
| 17  | D. Sancho I        | 11 de novembro de 1154   | O Povoador                                                                               | Dinastia de Borgonha / Dinastia Afonsina    |
| 18  | D. Afonso I        | 1109                     | O Conquistador, O Fundador, O Grande                                                     | Dinastia de Borgonha / Dinastia Afonsina    |
| 19  | D. Sancho II       | 8 de setembro de 1209    | O Capelo, O Piedoso, O Pio                                                               | Dinastia de Borgonha / Dinastia Afonsina    |
| 20  | D. Fernando I      | 31 de outubro de 1345    | O Formoso, O Belo, O Inconstante, O Inconsciente                                         | Dinastia de Borgonha / Dinastia Afonsina    |
| 21  | D. João IV         | 19 de março de 1604      | O Restaurador, O Afortunado                                                              | Dinastia de Bragança / Dinastia Brigantina  |
| 22  | D. Afonso VI       | 21 de agosto de 1643     | O Vitorioso, O Prisioneiro                                                               | Dinastia de Bragança / Dinastia Brigantina  |
| 23  | D. Pedro II        | 26 de abril de 1648      | O Pacífico                                                                               | Dinastia de Bragança / Dinastia Brigantina  |
| 24  | D. João V          | 22 de outubro de 1689    | O Magnânimo, O Magnífico, O Rei-Sol Português, O Freirático                              | Dinastia de Bragança / Dinastia Brigantina  |
| 25  | D. José I          | 6 de junho de 1714       | O Reformador                                                                             | Dinastia de Bragança / Dinastia Brigantina  |
| 26  | D. João VI         | 13 de maio de 1767       | O Clemente                                                                               | Dinastia de Bragança / Dinastia Brigantina  |
| 27  | D. Pedro IV        | 12 de outubro de 1798    | O Rei-Soldado, O Rei-Imperador, O Libertador                                             | Dinastia de Bragança / Dinastia Brigantina  |
| 28  | D. Pedro V         | 16 de setembro de 1837   | O Esperançoso, O Bem-Amado, O Muito Amado                                                | Dinastia de Bragança / Dinastia Brigantina  |
| 29  | D. Miguel I        | 26 de outubro de 1802    | O Rei Absoluto, O Absolutista, O Tradicionalista, O Usurpador                            | Dinastia de Bragança / Dinastia Brigantina  |
| 30  | D. Luís I          | 31 de outubro de 1838    | O Popular, O Bom, O Rei-Marinheiro                                                       | Dinastia de Bragança / Dinastia Brigantina  |
| 31  | D. Carlos I        | 28 de setembro de 1863   | O Martir                                                                                 | Dinastia de Bragança / Dinastia Brigantina  |
| 32  | D. Manuel II       | 15 de novembro de 1889   | O Patriota, O Último Rei                                                                 | Dinastia de Bragança / Dinastia Brigantina  |


## g. Qual a distribuição de reis pelas 4 dinastias?

### SPARQL Query

### Resultado

## h. Lista os descobrimentos (sua descrição) por ordem cronológica.

### SPARQL Query

### Resultado

## i. Lista as várias conquistas, nome e data, juntamento com o nome que reinava no momento.

### SPARQL Query

### Resultado

## j. Calcula uma tabela com o nome, data de nascimento e número de mandatos de todos os presidentes portugueses.

### SPARQL Query

### Resultado

## k. Quantos mandatos teve o presidente Sidónio Pais? Em que datas iniciaram e terminaram esses mandatos?

### SPARQL Query

### Resultado

## l. Quais os nomes dos partidos políticos presentes na ontologia? Qual a distribuição dos militantes por cada partido político? n. Qual o partido com maior número de presidentes militantes?

### SPARQL Query

### Resultado

## m. Qual a distribuição dos militantes por cada partido político?

### SPARQL Query

### Resultado

## n. Qual o partido com maior número de presidentes militantes? 

### SPARQL Query

### Resultado
