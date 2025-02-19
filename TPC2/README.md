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
| 1   | 32             |


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
|     | nome               | nascimento               | cognomes                                                                                 | dinastiaNome                                |
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
```sparql
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT ?dinastiaNome (COUNT(?s) AS ?numReis) WHERE {
    ?s a :Rei ;
       :nome ?nome ;
       :nascimento ?nascimento ;
       :cognomes ?cognomes ;
       :temReinado ?reinado .

    ?reinado :dinastia ?dinastia .
    ?dinastia :nome ?dinastiaNome .
}
GROUP BY ?dinastiaNome
ORDER BY DESC(?numReis)
```

### Resultado
|     | dinastiaNome                                 | numReis |
|-----|----------------------------------------------|---------|
|  1  | Dinastia de Bragança / Dinastia Brigantina   | 12      |
|  2  | Dinastia de Avis / Dinastia Joanina          | 10      |
|  3  | Dinastia de Borgonha / Dinastia Afonsina     | 9       |
|  4  | Dinastia Filipina                            | 3       |


## h. Lista os descobrimentos (sua descrição) por ordem cronológica.

### SPARQL Query
```sparql
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT DISTINCT ?data ?descricao WHERE {
    ?s a :Descobrimento ;
    	:notas ?descricao ;
    	:data ?data .
}
ORDER BY ?data
```

### Resultado
|     | data | descricao |
|-----|------|-----------|
| 1 | 1336 | "Provável primeira expedição às ilhas Canárias, a que se seguiram expedições adicionais em 1340 e 1341, embora tal seja disputado." |
| 2 | 1415 | "Tropas portuguesas sob o comando de João I de Portugal conquistam Ceuta. Este acontecimento é geralmente referido como o início da expansão ou descobrimentos Portugueses" |
| 3 | 1419 | "João Gonçalves Zarco e Tristão Vaz Teixeira descobrem a Ilha de Porto Santo, na Madeira." |
| 4 | 1420 | "Os mesmos navegadores, com Bartolomeu Perestrelo, descobrem a Ilha da Madeira, que foi de imediato colonizada." |
| 5 | 1422 | "Após sucessivas viagens, o cabo Não, considerado o limite navegável a sul por árabes e europeus, é ultrapassado, alcançando-se o Bojador." |
| 6 | 1427 | "Diogo de Silves descobre (ou redescobre) as ilhas açorianas ocidentais e centrais, que seriam colonizadas em 1431 por Gonçalo Velho Cabral." |
| 7 | 1434 | "Gil Eanes dobra o Cabo Bojador, dissipando o terror que este promontório inspirava." |
| 8 | 1435-1436 | "Gil Eanes e Afonso Gonçalves Baldaia descobrem Angra de Ruivos e este último chegou ao Rio de Ouro, no Saara Ocidental." |
| 9 | 1441 | "Nuno Tristão chega ao Cabo Branco com Gonçalo Afonso." |
| 10 | 1443 | "O regente D. Pedro decreta o monopólio da navegação na costa oeste Africana, reconhecido pela bula Rex regum, que atribui ao irmão Infante D. Henrique "o Navegador"." |
| 11 | 1443 | "Nuno Tristão entrou no golfo de Arguim." |
| 12 | 1444 | "Dinis Dias descobriu o cabo Cabo Verde (Dakar) e a Ilha de Palma (Goreia)." |
| 13 | 1445 | "Álvaro Fernandes passou além do Cabo Verde (cabo), Goreia e chegou ao "Cabo dos Mastros" (Cabo Roxo? provavelmente entre o Cabo Verde e o rio Gâmbia)." |
| 14 | 1446 | "Álvaro Fernandes chegou ao norte da Guiné-Bissau." |
| 15 | 1452 | "Diogo de Teive descobriu as ilhas Flores e Corvo nos Açores." |
| 16 | 1455 | "Bula Romanus Pontifex do Papa Nicolau V confirma as explorações portuguesas e declara que todas as terras e mares a sul do Cabo Bojador e do Cabo Não são pertença dos reis de Portugal." |
| 17 | 1455 | "Alvise Cadamosto explora do Rio Gâmbia ao Rio Geba (Guiné-Bissau) e o arquipélago dos Bijagós. Na foz do Gâmbia, ao notar o quase desaparecimento da estrela polar no horizonte, esboçou a primeira representação da constelação Cruzeiro do Sul." |
| 18 | 1456-1460 | "Viagens de Alvise Cadamosto, Diogo Gomes e António da Noli descobriram as primeiras ilhas do arquipélago de Cabo Verde (Boavista, Santiago, Maio e Sal)." |
| 19 | 1459 | "Afonso V encomenda o mapa-múndi que reúne o conhecimento geográfico da época aos venezianos Fra Mauro e Andrea Bianco." |
| 20 | 1460 | "Morte do Infante D. Henrique. A sua exploração sistemática do Atlântico alcançou em vida os 8º N na costa africana, com a chegada de Pêro de Sintra à que chama Serra Leoa, e os 40º O no oceano Atlântico (Mar dos Sargaços)." |
| 21 | 1461 | "Diogo Gomes e Antonio da Noli descobrem mais ilhas de Cabo Verde." |
| 22 | 1462 | "Diogo Afonso descobre as cinco ilhas mais ocidentais do arquipélago de Cabo Verde (Brava, São Nicolau, São Vicente, Santo Antão e os ilhéus Branco e Raso)." |
| 23 | 1469 | "Contrato de Fernão Gomes para a exploração da costa da Guiné a sul da Serra Leoa e comércio de Pimenta-da-Guiné que duraria até 1475." |
| 24 | 1471 | "João de Santarém e Pêro Escobar encontram a costa da Mina, chegam região do Cabo Três Pontos (Gana) e ao delta do Níger." |
| 25 | 1472 | "Rui de Sequeira chega a Benim nomeando a área Lagoa de Lagos (actual Lagos (Nigéria))." |
| 26 | 1472-1473 | "Fernão Pó explora o rio Wouri que nomeia "dos Camarões" e as ilhas Formosa (Bioko) e Ano Bom." |
| 27 | 1472-1474 | "João Vaz Corte-Real e Álvaro Martins Homem poderão ter atingido a Terra Nova. Descoberta não comprovada" |
| 28 | 1473 | "Lopo Gonçalves descobre o Cabo Lopez, na boca do rio Ogooué e é creditado como o primeiro a cruzar a linha do equador e chegar ao Hemisfério Sul" |
| 29 | 1474 | "Afonso V consulta o geógrafo Toscanelli, que aconselha a navegação para oeste, para chegar à Índia" |
| 30 | 1475 | "Antes do contrato de Fernão Gomes terminar, Rui de Sequeira e Lopo Gonçalves chegam ao cabo de St. Catarina, 2º latitude Sul" |
| 31 | 1479 | "O Tratado das Alcáçovas estabelece o controlo português dos Açores, Guiné, Elmina, Madeira e Cabo Verde e o controlo castelhano das ilhas Canárias" |
| 32 | 1482-1484 | "Diogo Cão chegou ao estuário do Rio Congo (Congo) onde deixou um Padrão de pedra, substituindo as habituais cruzes de madeira; subiu 150Km a montante do rio até às cataratas de Ielala." |
| 33 | 1484-1486 | "Afonso de Paiva, Duarte Pacheco Pereira e José Vizinho contactam o Reino de Benim onde a presença de pimenta indicia a proximidade da Índia." |
| 34 | 1485-1486 | "Segunda viagem de Diogo Cão leva Martin Behaim como cosmógrafo, passa o Cabo Padrão (Cape Cross) e terá chegado a Walvis Bay, na Namíbia." |
| 35 | 1487 | "Afonso de Paiva e Pêro da Covilhã partiram de Lisboa, viajando por terra em busca do reino do Preste João, na Etiópia." |
| 36 | 1487 | "Gonçalo Eanes e Pêro de Évora sobem o rio Senegal numa expedição ao interior africano até Tucurol e Timbuctu." |
| 37 | 1487-1488 | "Bartolomeu Dias dobra o Cabo das Tormentas, futuro Cabo da Boa Esperança, coroando 50 anos de esforço e numerosas expedições, entrando pela primeira vez no Oceano Índico. Afonso de Paiva e Pêro da Covilhã chegam a Adém." |
| 38 | 1489-1492 | "Foram feitas várias expedições ao Atlântico Sul para mapear os ventos." |
| 39 | 1494 | "Assinado o Tratado de Tordesilhas "dividindo" o mundo por descobrir entre Portugal e o recém-formado Reino da Espanha, na sequência da contestação de D. João II às pretensões espanholas após a viagem de Cristovão Colombo." |
| 40 | 1495 ou 1500 | "Viagem de João Fernandes Lavrador e Pêro de Barcelos à Gronelândia (Terra do Bacalhau). Nesta viagem avistaram a terra que nomearam Labrador (lavrador)." |
| 41 | 1497-1499 | "Vasco da Gama comandou a primeira frota a contornar África e chegar a Calecute na Índia, e regressou." |
| 42 | 1498 | "Duarte Pacheco Pereira terá explorado o Atlântico Sul (e terá alcançado a foz do rio Amazonas e a ilha do Marajó no que terá sido uma expedição secreta - não existem provas)" |
| 43 | 1500 | "A 10 de Agosto Diogo Dias, navegador da frota de Pedro Álvares Cabral na segunda armada à Índia, descobriu uma ilha a que deu o nome de São Lourenço, mais tarde designada Madagáscar." |
| 44 | 1500-1501 | "Gaspar Corte Real e Miguel Corte Real atingiram a Terra Nova, que nomeou Terras de Corte Real (Canadá)." |
| 45 | 1500-1501 | "A segunda frota para a Índia comandada por Pedro Álvares Cabral atinge o Brasil, aportando em Porto Seguro." |
| 46 | 1502 | "Vasco da Gama vindo da Índia avistou as então chamadas Ilhas do Almirante (Seychelles)." |
| 47 | 1502 | "Miguel Corte-Real partiu para a Nova Inglaterra em busca do seu irmão Gaspar. João da Nova descobriu a Ilha de Ascensão. Fernão de Noronha descobriu as ilhas que mantêm o seu nome, Fernando Noronha, em Pernambuco." |
| 48 | 1503 | "De regresso do Oriente Estêvão da Gama descobriu a Ilha de Santa Helena." |
| 49 | 1503 | "A caminho da Índia António de Saldanha foi o primeiro europeu a ancorar na Baía de Saldanha e a ascender à Montanha da Mesa, que nomeou, na atual África do Sul." |
| 50 | 1505 | "Gonçalo Álvares, da frota do primeiro vice-rei, ruma a sul, onde "a água e até o vinho gelavam" descobrindo a Ilha de Gonçalo Álvares (Gough Island)" |
| 51 | 1505-1506 | "Lourenço de Almeida é enviado às Maldivas e chegou ao que chamou Ceilão (Sri Lanka), a "Taprobana" dos registos clássicos gregos." |
| 52 | 1506 | "Tristão da Cunha descobriu a Ilha de Tristão da Cunha no Atlântico Sul. Navegadores portugueses aportaram em Madagáscar." |
| 53 | 1507-1512 | "Os portugueses foram os primeiros europeus a aportar nas Ilhas Mascarenhas, no Índico, nomeadas em homenagem a Pedro Mascarenhas" |
| 54 | 1509 | "Diogo Lopes de Sequeira atravessou o golfo de Bengala e chegou a Sumatra e Malaca (Malásia), com ele viajava Fernão de Magalhães, que viria a fazer a primeira viagem de circum-navegação ao globo, ao serviço de Espanha em 1519-22." |
| 55 | 1511 | "Duarte Fernandes foi o primeiro europeu a chegar ao Reino do Sião (Tailândia), enviado por Afonso de Albuquerque durante a conquista de Malaca." |
| 56 | 1511 | "António de Abreu, Francisco Serrão e Simão Afonso Bisagudo são enviados por Albuquerque em busca das "ilhas das especiarias". Serrão naufraga em Ternate nas Molucas (Indonésia)." |
| 57 | 1511 | "Rui Nunes da Cunha foi o primeiro europeu a chegar a Pegu (Birmânia, Myanmar), enviado por Albuquerque." |
| 58 | 1512 | "António de Abreu chegou à ilha de Timor e às ilhas Banda, Ambão e Seram." |
| 59 | 1512 | "Pedro Mascarenhas descobriu a ilha Diego Garcia. Chegou também à ilha Maurícia, que poderia já ser conhecida em expedições anteriores de Diogo Dias e Afonso de Albuquerque." |
| 60 | 1512-1514 | "João de Lisboa e Estevão Fróis exploram o estuário do Rio da Prata e provavelmente o Golfo de San Matias a 42° Sul na Argentina22 Cristóvão de Haro, financiador da expedição, testemunha a viagem e as notícias que Lisboa e Fróis recolheram do Rei Branco(o imperador Inca), assim como o machado de prata obtido junto dos nativos e que ofereceram ao rei D. Manuel I." |
| 61 | 1513 | "Jorge Álvares partindo de Malaca é o primeiro europeu a aportar no sul da China, na Ilha de Lintin, no estuário do Rio das Pérolas." |
| 62 | 1513 | "Afonso de Albuquerque atravessa o estreito de Bab-el-Mandeb no Mar Vermelho liderando a primeira frota europeia a navegar nessas águas." |
| 63 | 1516 | "Portugueses aportam em Da Nang, no Reino de Champa que nomeiam Cochinchina, (actual Vietname)." |
| 64 | 1516-1517 | "Rafael Perestrelo comandou o primeiro navio comercial a aportar na China continental, em Cantão. Fernão Pires de Andrade e Tomé Pires foram enviados de D. Manuel I para estabelecer relações oficiais entre o Império Português e a Dinastia Ming, no reinado do imperador Zhengde." |
| 65 | 1520 | "Francisco Álvares e uma embaixada portuguesa chegam à Etiópia onde encontram Pêro da Covilhã" |
| 66 | 1520 | "(Diogo Pacheco terá visitado Kimberley, na Austrália em busca da "Ilha do Ouro" a sul e a sudeste de Sumatra, Java e Sunda, informado por Malaios e Sumatreses, presentes na sua tripulação.- descoberta não reconhecida oficialmente)" |
| 67 | 1522 | "(Cristovão de Mendonça terá descoberto a Austrália e Nova Zelândia, partindo de Belém em 1521.[carece de fontes]- descoberta não reconhecida oficialmente)" |
| 68 | 1525 | "Aleixo Garcia explora o Rio da Prata ao serviço de Espanha, como membro da expedição de Juan Díaz de Solís e, mais tarde, liderando uma expedição privada de Europeus e indios Guarani, explora o Paraguai e a Bolívia. Aleixo Garcia foi o primeiro europeu a atravessar o Chaco e a conseguir penetrar nas defesas exteriores do Império Inca, já nas colinas dos Andes e na região de Sucre, na atual Bolívia. Aleixo Garcia foi o primeiro europeu a fazê-lo, realizando a façanha oito anos antes de Francisco Pizarro." |
| 69 | 1525 | "Gomes de Sequeira e Diogo da Rocha foram enviados pelo governador Jorge de Meneses, à descoberta de territórios a norte das Molucas, foram os primeiros europeus a chegar às Ilhas Carolinas, a nordeste da Nova Guiné, que então nomearam "Ilhas de Sequeira". (A Austrália teria sido descoberta por Cristóvão de Mendonça e Gomes de Sequeira em 1525 – descoberta não reconhecida oficialmente)" |
| 70 | 1526 | "Jorge de Meneses aportou na ilha Waigeo na Papua Ocidental (Nova Guiné)" |
| 71 | 1528 | "Diogo Rodrigues explorou o arquipélago das Mascarenhas, que nomeou em homenagem ao seu companheiro Pedro de Mascarenhas, que compreende a Reunião, Maurícia e Rodrigues." |
| 72 | 1529 | "É assinado o Tratado de Saragoça, que estabelece o antimeridiano de Tordesilhas, limite leste das explorações portuguesas e espanholas, para solucionar a chamada "Questão das Molucas"." |
| 73 | 1538 | "João Fogaça chega à Papua-Nova Guiné enviado por António Galvão." |
| 74 | 1542-1543 | "Fernão Mendes Pinto, Diogo Zeimoto e Cristovão Borralho chegaram ao Japão." |
| 75 | 1586 | "António da Madalena um frade Capuchinho foi um dos primeiros visitantes ocidentais a chegar a Angkor (actual Camboja)" |
| 76 | 1602-1606 | "Bento de Góis, missionário jesuíta, foi o primeiro europeu a percorrer o caminho terrestre da Índia para a China, através da Ásia Central." |
| 77 | 1606 | "Pedro Fernandes de Queirós alcançou as Novas Hébridas e aportou numa grande ilha que pensou ser parte do procurado continente a sul, a que chamou Ilha do Espírito Santo, actual Vanuatu." |
| 78 | 1606 | "Luís Vaz de Torres (nacionalidade incerta) descobriu o que é hoje chamado Estreito de Torres." |
| 79 | 1624 | "António de Andrade e Manuel Marques, missionários jesuítas, viajaram de Agra (Índia) a Chaparangue, sendo os primeiros europeus documentados a chegar ao Tibete" |
| 80 | 1626 | "Estêvão Cacella, missionário jesuíta, viajou através dos Himalaias e foi o primeiro europeu a entrar no Butão34" |
| 81 | 1636-1638 | "Pedro Teixeira partiu de Belém do Pará subindo o rio Amazonas e alcançou Quito, no Equador, numa expedição de mais de mil homens." |
| 82 | 1660-1662 | "(David Melgueiro partindo de Tanegashima poderá ter realizado a primeira travessia da passagem do Nordeste. 35 Viagem pouco documentada, ao serviço da marinha holandesa)" |


## i. Lista as várias conquistas, nome e data, juntamento com o nome que reinava no momento.

### SPARQL Query
```sparql
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT DISTINCT ?nomeConq ?dataConq ?nomeRei WHERE {
    ?s a :Conquista ;
   		:nome ?nomeConq ;
    	:data ?dataConq ;
        :temReinado ?reinado .
    
    ?reinado :temMonarca ?monarca .
   	?monarca :nome ?nomeRei .
}
```

### Resultado
|     | nomeConq          | dataConq | nomeRei |
|-----|-------------------|----------|---------|
| 1 | Conquista de Beja | 1159 | D. Afonso I |
| 2 | Conquista do Castelo de Cera | 1159 | D. Afonso I |
| 3 | Reconquista de Beja | 1162 | D. Afonso I |
| 4 | Conquista | 1158 | D. Afonso I |
| 5 | Conquista de Évora | 1165 | D. Afonso I |
| 6 | Tomada de Serpa | 1166 | D. Afonso I |
| 7 | Batalha do Salado | 1340 | D. Afonso IV |
| 8 | Batalha de Sacavém | 1147 | D. Afonso I |
| 9 | Conquista de Lisboa | 1147 | D. Afonso I |
| 10 | Tomada do Castelo | 1147 | D. Afonso I |
| 11 | Conquista de Évoramonte | 1159 | D. Afonso I |
| 12 | Batalha Navas de Tolosa | 1212 | D. Afonso II |
| 13 | Tomada de Moura | 1166 | D. Afonso I |
| 14 | Batalha de Badajoz | 1169 | D. Afonso I |
| 15 | Conquista de Alvor | 1189 | D. Sancho I |
| 16 | Cerco de Silves | 1189 | D. Sancho I |
| 17 | Fundação do Castelo | 1135 | D. Afonso I |
| 18 | Batalha de Ourique | 1139 | D. Afonso I |


## j. Calcula uma tabela com o nome, data de nascimento e número de mandatos de todos os presidentes portugueses.

### SPARQL Query
```sparql
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT ?nome ?nascimento (COUNT(?mandato) AS ?numMandatos) WHERE {
    ?s a :Presidente .
    ?s :mandato ?mandato ;
		:nome ?nome ;
		:nascimento ?nascimento .
}
GROUP BY ?nome ?nascimento
ORDER BY ?nome
```

### Resultado
|     | nome                                         | nascimento          | numMandatos |
|-----|----------------------------------------------|---------------------|-------------|
| 1 | Américo Deus Rodrigues Thomaz | 19 de novembro de 1894 | 1 |
| 2 | António José de Almeida | 17 de julho de 1866 | 1 |
| 3 | António Sebastião Ribeiro de Spínola | 11 de abril de 1910 | 2 |
| 4 | António de Oliveira Salazar | 28 de abril de 1889 | 1 |
| 5 | António Óscar de Fragoso Carmona | 24 de novembro de 1869 | 4 |
| 6 | Aníbal António Cavaco Silva | 15 de julho de 1939 | 1 |
| 7 | Bernardino Luís Machado Guimarães | 28 de março de 1851 | 2 |
| 8 | Francisco Higino Craveiro Lopes | 12 de abril de 1894 | 1 |
| 9 | Francisco da Costa Gomes | 30 de Junho de 1914 | 1 |
| 10 | Joaquim Teófilo Fernandes Braga | 24 de fevereiro de 1843 | 2 |
| 11 | José Mendes Cabeçadas Júnior | 19 de setembro de 1883 | 1 |
| 12 | João do Canto e Castro Silva Antunes Júnior | 19 de maio de 1862 | 2 |
| 13 | Manuel José de Arriaga Brum da Silveira e Peyrelongue | 8 de julho de 1840 | 1 |
| 14 | Manuel Teixeira Gomes | 27 de maio de 1860 | 1 |
| 15 | Manuel de Oliveira Gomes da Costa | 14 de janeiro de 1863 | 2 |
| 16 | Mário Alberto Nobre Lopes Soares | 7 de Dezembro de 1924 | 1 |
| 17 | Sidónio Bernardino Cardoso da Silva Pais | 1 de maio de 1872 | 2 |


## k. Quantos mandatos teve o presidente Sidónio Pais? Em que datas iniciaram e terminaram esses mandatos?

### SPARQL Query
```sparql
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT ?comeco ?fim WHERE {
    ?s a :Presidente .
    ?s :mandato ?mandato ;
       :nome ?nome .
    ?mandato :comeco ?comeco ;
    		 :fim ?fim .
    
    FILTER(?nome = "Sidónio Bernardino Cardoso da Silva Pais")
}
GROUP BY ?comeco ?fim
```

### Resultado
|     | comeco                    | fim                       |
|-----|---------------------------|---------------------------|
|  1  | "12 de dezembro de 1917"  | "27 de dezembro de 1917"  |
|  2  | "27 de dezembro de 1917"  | "14 de dezembro de 1918"  |


## l. Quais os nomes dos partidos políticos presentes na ontologia?

### SPARQL Query
```sparql
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT ?nome WHERE {
    ?p a :Partido .
    ?p :nome ?nome .
}
ORDER BY ?nome
```

### Resultado
|     | nome                   | 
|-----|------------------------|
|  1  | "Democrático"          |
|  2  | "Evolucionista"        |
|  3  | "Independente"         |
|  4  | "Liberal"              |
|  5  | "Nacional Republicano" |
|  6  | "Nacionalista"         |
|  7  | "Republicano"          |
|  8  | "Social Democrata"     |
|  9  | "Socialista"           | 
| 10  | "União Nacional"       |


## m&n. Qual a distribuição dos militantes por cada partido político? Qual o partido com maior número de presidentes militantes? 

### SPARQL Query
```sparql
PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
SELECT ?nome (COUNT(?militante) AS ?numMilitantes) WHERE {
    ?p a :Partido .
    ?p :nome ?nome ;
    	:temMilitante ?militante .
}
GROUP BY ?nome
ORDER BY DESC(?numMilitantes)
```

### Resultado
|     | nomePartido            | numMilitantes |
|-----|------------------------|---------------|
|  1  | "Independente"         | 4             |
|  2  | "União Nacional"       | 4             |
|  3  | "Nacional Republicano" | 2             |
|  4  | "Democrático"          | 2             |
|  5  | "Republicano"          | 2             |
|  6  | "Socialista"           | 1             |
|  7  | "Evolucionista"        | 1             |
|  8  | "Liberal"              | 1             |
|  9  | "Nacionalista"         | 1             |
| 10  | "Social Democrata"     | 1             |
