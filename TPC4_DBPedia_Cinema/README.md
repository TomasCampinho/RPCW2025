# DBPedia Cinema Data Harvester

## 1. Faz o fetch da informação sobre filmes e atores (SPARQL Queries): 

### Filmes:
```sparql
SELECT DISTINCT ?film ?title ?abstract ?countryName ?directorName ?genreName WHERE {
    ?film a dbo:Film .
    ?film rdfs:label ?title .
    ?film dbo:abstract ?abstract .
    OPTIONAL { ?film dbo:country ?country . ?country rdfs:label ?countryName . FILTER (lang(?countryName) = 'en') }
    OPTIONAL { ?film dbo:director ?director . ?director rdfs:label ?directorName . FILTER (lang(?directorName) = 'en') }
    OPTIONAL { ?film dbo:genre ?genre . ?genre rdfs:label ?genreName . FILTER (lang(?genreName) = 'en') }
    FILTER (lang(?title) = 'en') .
    FILTER (lang(?abstract) = 'en') .
}
ORDER by ?title
```
### Atores:
```sparql
SELECT DISTINCT ?actor ?name ?birthDate ?birthPlaceName WHERE {
    ?actor a dbo:Actor .
    ?actor rdfs:label ?name .
    OPTIONAL { ?actor dbo:birthDate ?birthDate . }
    OPTIONAL { ?actor dbo:birthPlace ?birthPlace . ?birthPlace rdfs:label ?birthPlaceName . FILTER (lang(?birthPlaceName) = 'en') }
}
ORDER by ?name
```

## 2. Escreve essa informação em ficheiros JSON com as seguintes estruturas:

### movies.json:
```json
[
    { "id": "http://dbpedia.org/resource/Film_ID",
      "titulo": "Film Title",
      "pais": "Country",
      "realizador": "Director",
      "genero": "Genre",
      "sinopsis/abs": "Abstract"
    }
]
```

### actors.json:
```json
[
    { "id": "http://dbpedia.org/resource/Actor_ID",
      "nome": "Actor Name",
      "dataNas": "Birth Date",
      "origem": "Birth Place"
    }
]
```

## 3. Debugging

Por fim, imprime para o terminal o número total de filmes e atores fetched da DBPedia e escritos nos ficheiros JSON:

```
INFO:root:Total movies fetched: 10000
INFO:root:Total movies written: 9476
INFO:root:Total actors fetched: 10000
INFO:root:Total actors written: 4433
```

A discrepância entre o número de entradas fetched e written pode ser atribuída a vários fatores:
- Dados incompletos: Algumas entradas podem não ter todos os campos necessários (por exemplo, título ou abstract para filmes, nome para atores).
- Dados duplicados: Entradas duplicadas são removidas durante o processamento.

Embora as queries não tenham um limite explícito, os resultados são limitados a 10000 entradas devido a possíveis restrições de desempenho e limitações impostas pelo endpoint da DBPedia.