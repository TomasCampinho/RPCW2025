import requests
import shutil

API_URL = 'http://dbpedia.org/sparql'

def fetch_movies():
    query = """
    SELECT DISTINCT ?film ?title ?abstract ?countryName ?directorName ?genreName ?actorName ?releaseDate ?runtime ?languageName WHERE {
        ?film a dbo:Film .
        ?film rdfs:label ?title .
        ?film dbo:abstract ?abstract .
        OPTIONAL { ?film dbo:country ?country . ?country rdfs:label ?countryName . FILTER (lang(?countryName) = 'en') }
        OPTIONAL { ?film dbo:director ?director . ?director rdfs:label ?directorName . FILTER (lang(?directorName) = 'en') }
        OPTIONAL { ?film dbo:genre ?genre . ?genre rdfs:label ?genreName . FILTER (lang(?genreName) = 'en') }
        OPTIONAL { ?film dbo:starring ?actor . ?actor rdfs:label ?actorName . FILTER (lang(?actorName) = 'en') }
        OPTIONAL { ?film dbo:releaseDate ?releaseDate . }
        OPTIONAL { ?film dbo:runtime ?runtime . }
        OPTIONAL { ?film dbo:language ?language . ?language rdfs:label ?languageName . FILTER (lang(?languageName) = 'en') }
        FILTER (lang(?title) = 'en') .
        FILTER (lang(?abstract) = 'en') .
    }
    ORDER by ?title
    LIMIT 500
    """
    response = requests.get(API_URL, params={'query': query, 'format': 'json'})
    data = response.json()
    return data['results']['bindings']

def get_existing_ids(filepath):
    existing_ids = set()
    with open(filepath, 'r') as file:
        for line in file:
            if line.startswith(':') and 'rdf:type owl:NamedIndividual' in line:
                existing_ids.add(line.split()[0][1:])
    return existing_ids

def write_to_ttl(movies, source_filepath, target_filepath):
    # Copy existing data from cinema.ttl to cinema2.ttl
    shutil.copyfile(source_filepath, target_filepath)
    
    existing_ids = get_existing_ids(source_filepath)
    new_ids = set()
    
    with open(target_filepath, 'a') as file:
        for movie in movies:
            film_id = movie['film']['value'].split('/')[-1]
            if film_id not in existing_ids and film_id not in new_ids:
                new_ids.add(film_id)
                file.write(f':{film_id} rdf:type owl:NamedIndividual , :Filme ;\n')
                file.write(f'    :titulo "{movie["title"]["value"]}" ;\n')
                file.write(f'    :data "{movie.get("releaseDate", {"value": "Unknown"})["value"]}" ;\n')
                file.write(f'    :duracao {movie.get("runtime", {"value": "Unknown"})["value"]} ;\n')
                file.write(f'    :temGenero :{movie.get("genreName", {"value": "Unknown"})["value"].replace(" ", "_")} ;\n')
                file.write(f'    :temPaisOrigem :{movie.get("countryName", {"value": "Unknown"})["value"].replace(" ", "_")} ;\n')
                file.write(f'    :temLingua :{movie.get("languageName", {"value": "Unknown"})["value"].replace(" ", "_")} .\n\n')
                
                if 'actorName' in movie:
                    actor_id = movie['actorName']['value'].replace(" ", "_")
                    if actor_id not in existing_ids and actor_id not in new_ids:
                        new_ids.add(actor_id)
                        file.write(f':{actor_id} rdf:type owl:NamedIndividual , :Pessoa ;\n')
                        file.write(f'    :atuou :{film_id} ;\n')
                        file.write(f'    :temSexo "Unknown" .\n\n')
                
                if 'directorName' in movie:
                    director_id = movie['directorName']['value'].replace(" ", "_")
                    if director_id not in existing_ids and director_id not in new_ids:
                        new_ids.add(director_id)
                        file.write(f':{director_id} rdf:type owl:NamedIndividual , :Pessoa ;\n')
                        file.write(f'    :realizou :{film_id} ;\n')
                        file.write(f'    :temSexo "Unknown" .\n\n')

if __name__ == "__main__":
    movies = fetch_movies()
    write_to_ttl(movies, 'cinema.ttl', 'cinema2.ttl')
