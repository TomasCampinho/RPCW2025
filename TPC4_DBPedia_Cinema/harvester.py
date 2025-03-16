import json
import logging
from query import query_graphdb

logging.basicConfig(level=logging.INFO)

endpoint = "https://dbpedia.org/sparql"

# Query to get movies
movies_query = """
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
"""

# Fetch movies data
movies_result = query_graphdb(endpoint, movies_query)
movies = []
movie_ids = set()

logging.info(f"Total movies fetched: {len(movies_result['results']['bindings'])}")

for m in movies_result["results"]["bindings"]:
    movie_id = m["film"]["value"]
    if movie_id not in movie_ids:
        movie_ids.add(movie_id)
        movie_data = {
            "id": movie_id,
            "titulo": m["title"]["value"],
            "sinopsis/abs": m["abstract"]["value"],
            "pais": m.get("countryName", {}).get("value", "Unknown"),
            "realizador": m.get("directorName", {}).get("value", "Unknown"),
            "genero": m.get("genreName", {}).get("value", "Unknown"),
            "elenco": []
        }
        movies.append(movie_data)

logging.info(f"Total movies written: {len(movies)}")

total_actors_fetched = 0

# Query actors for each movie individually
for movie in movies:
    actors_query = f"""
        SELECT DISTINCT ?actor ?name ?birthDate ?birthPlaceName WHERE {{
            <{movie['id']}> dbo:starring ?actor .
            ?actor rdfs:label ?name .
            OPTIONAL {{ ?actor dbo:birthDate ?birthDate . }}
            OPTIONAL {{ ?actor dbo:birthPlace ?birthPlace . ?birthPlace rdfs:label ?birthPlaceName . FILTER (lang(?birthPlaceName) = 'en') }}
        }}
        LIMIT 20
    """

    actors_result = query_graphdb(endpoint, actors_query)
    total_actors_fetched += len(actors_result['results']['bindings'])
    
    actor_ids = set()
    for a in actors_result["results"]["bindings"]:
        actor_id = a["actor"]["value"]
        if actor_id not in actor_ids:
            actor_ids.add(actor_id)
            actor_data = {
                "id": actor_id,
                "nome": a["name"]["value"],
                "dataNas": a.get("birthDate", {}).get("value", "Unknown"),
                "origem": a.get("birthPlaceName", {}).get("value", "Unknown")
            }
            movie["elenco"].append(actor_data)


total_actors = sum(len(movie["elenco"]) for movie in movies)
logging.info(f"Total actors fetched: {total_actors_fetched}")
logging.info(f"Total actors written: {total_actors}")

# Save movies data with cast to JSON file
with open('movies.json', 'w') as fout:
    json.dump(movies, fout, indent=4, ensure_ascii=False)