# DBPedia Movie Data Harvester

## 1. SPARQL QUERIES

### Faz o fetch da informação sobre filmes: 

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
LIMIT 100
```

### Faz o fetch da informação sobre atores para um filme específico:

```sparql
SELECT DISTINCT ?actor ?name ?birthDate ?birthPlaceName WHERE {
    <FILM_ID> dbo:starring ?actor .
    ?actor rdfs:label ?name .
    OPTIONAL { ?actor dbo:birthDate ?birthDate . }
    OPTIONAL { ?actor dbo:birthPlace ?birthPlace . ?birthPlace rdfs:label ?birthPlaceName . FILTER (lang(?birthPlaceName) = 'en') }
}
ORDER by ?name
LIMIT 20
```
É possivel ajustar os limites (LIMIT) para obter maiores/menores resultados

## 2. JSON FILE
Escreve a informação num ficheiro JSON com a seguinte estrutura:

### movies.json:
```json
[
    { "id": "http://dbpedia.org/resource/Film_ID",
      "titulo": "Film Title",
      "sinopsis/abs": "Abstract",
      "pais": "Country",
      "realizador": "Director",
      "genero": "Genre",
      "elenco": [
          { "id": "http://dbpedia.org/resource/Actor_ID",
            "nome": "Actor Name",
            "dataNas": "Birth Date",
            "origem": "Birth Place"
          }
      ]
    }
]
```

## 3. DEBUGGING

Imprime para o terminal o número total de filmes e atores fetched da DBPedia e escritos no ficheiro JSON:

```
INFO:root:Total movies fetched: 100
INFO:root:Total movies written: 86
INFO:root:Total actors fetched: 1023
INFO:root:Total actors written: 629
```

A discrepância entre o número de entradas fetched e written pode ser atribuída a vários fatores:
- Dados incompletos: Algumas entradas podem não ter todos os campos necessários (por exemplo, título ou sinopse para filmes).
- Dados duplicados: Entradas duplicadas são removidas.