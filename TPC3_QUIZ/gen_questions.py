import requests
import random

def query_graphdb(endpoint_url, sparql_query):
    headers = {
        'Accept': 'application/json',
    }
    response = requests.get(endpoint_url, params={'query': sparql_query}, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

def generate_questions(total_questions=6):
    endpoint = "http://localhost:7200/repositories/HistoriaPT"

    num_question_types = 6  # change this when adding new questions
    questions_per_type = total_questions // num_question_types
    
    # MULTIPLE CHOICE QUESTIONS
    # 1: Qual é a data de nascimento do Rei x?
    sparql_query = """
        PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
        SELECT DISTINCT ?s ?p ?o WHERE {
            ?s a :Rei ;
            :nome ?p;
            :nascimento ?o.
        }
    """
    result = query_graphdb(endpoint, sparql_query)
    lista = [(r['s']['value'].split('#')[-1], r['p']['value'].split('#')[-1], r['o']['value'].split('#')[-1]) for r in result['results']['bindings']]
    
    multiple_choice_questions1 = []
    random.shuffle(lista)
    for item in lista:
        other_dates = [i[2] for i in lista if i != item]
        options = random.sample(other_dates, 3) + [item[2]]
        random.shuffle(options)
        
        question = {
            "question": f"Qual é a data de nascimento do Rei {item[1]}?",
            "options": options,
            "answer": item[2]
        }
        multiple_choice_questions1.append(question)

    # 2: Quantos reis fizeram parte da [Nome da Dinastia]?
    sparql_query = """
        PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
        SELECT ?dinastiaNome (COUNT(?s) AS ?numReis) WHERE {
            ?s a :Rei ;
            :nome ?nome ;
            :temReinado ?reinado .

            ?reinado :dinastia ?dinastia .
            ?dinastia :nome ?dinastiaNome .
        }
        GROUP BY ?dinastiaNome
    """
    result = query_graphdb(endpoint, sparql_query)
    dinastias = [(r['dinastiaNome']['value'], r['numReis']['value']) for r in result['results']['bindings']]
    
    multiple_choice_questions2 = []
    random.shuffle(dinastias)
    for item in dinastias:
        other_counts = [i[1] for i in dinastias if i != item]
        options = random.sample(other_counts, 3) + [item[1]]
        random.shuffle(options)
        
        question = {
            "question": f"Quantos reis fizeram parte da {item[0]}?",
            "options": options,
            "answer": item[1]
        }
        multiple_choice_questions2.append(question)

    # CORRESPOND QUESTIONS
    # 1: Corresponde os nomes dos reis aos seus cognomes:
    sparql_query = """
        PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
        SELECT ?nome ?cognomes WHERE {
            ?s a :Rei .
            ?s :nome ?nome .              
            ?s :cognomes ?cognomes . 
        }
        ORDER BY ?nome
    """
    result = query_graphdb(endpoint, sparql_query)
    correspond_questions = [(r['nome']['value'], r['cognomes']['value']) for r in result['results']['bindings']]
    random.shuffle(correspond_questions)
    
    correspond_questions_list = []
    for i in range(len(correspond_questions) // 4):  # Include all correspond questions
        question = {
            "question": "Corresponde os nomes dos reis aos seus cognomes:",
            "pairs": correspond_questions[i*4:(i+1)*4],  # 4 pairs per question
            "answer": correspond_questions[i*4:(i+1)*4]  # Correct pairs for checking
        }
        correspond_questions_list.append(question)
    
    # 2: Corresponde os descobrimentos às suas datas:
    sparql_query = """
        PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
        SELECT DISTINCT ?descricao ?data WHERE {
            ?s a :Descobrimento ;
                :notas ?descricao ;
                :data ?data .
        }
        ORDER BY ?data
    """
    result = query_graphdb(endpoint, sparql_query)
    correspond_questions2 = [(r['descricao']['value'], r['data']['value']) for r in result['results']['bindings']]
    random.shuffle(correspond_questions2)
    
    correspond_questions2_list = []
    for i in range(len(correspond_questions2) // 4):  # Include all correspond questions
        question = {
            "question": "Corresponde os descobrimentos às suas datas:",
            "pairs": correspond_questions2[i*4:(i+1)*4],  # 4 pairs per question
            "answer": correspond_questions2[i*4:(i+1)*4]  # Correct pairs for checking
        }
        correspond_questions2_list.append(question)


    #T/F QUESTIONS
    # 1: O rei [Nome do Rei] conquistou [Nome da Conquista]?
    sparql_query = """
        PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
        SELECT DISTINCT ?nomeConq ?nomeRei WHERE {
            ?s a :Conquista ;
                :nome ?nomeConq ;
                :temReinado ?reinado .
            
            ?reinado :temMonarca ?monarca .
            ?monarca :nome ?nomeRei .
        }
    """
    result = query_graphdb(endpoint, sparql_query)
    conquistas = [(r['nomeConq']['value'], r['nomeRei']['value']) for r in result['results']['bindings']]
    
    true_false_questions = []
    random.shuffle(conquistas)
    for item in conquistas:
        if random.choice([True, False]):
            question = {
                "question": f"A {item[0]} aconteceu durante o reinado de {item[1]}?",
                "options": ["Verdadeiro", "Falso"],
                "answer": "Verdadeiro"
            }
        else:
            other_rei = random.choice([i[1] for i in conquistas if i != item])
            question = {
                "question": f"A {item[0]} aconteceu durante o reinado de {other_rei}?",
                "options": ["Verdadeiro", "Falso"],
                "answer": "Falso"
            }
        true_false_questions.append(question)

    # 2: O presidente [Nome do Presidente] teve [Número de Mandatos] mandato(s)?
    sparql_query = """
        PREFIX : <http://www.semanticweb.org/andre/ontologies/2015/6/historia#>
        SELECT ?nome (COUNT(?mandato) AS ?numMandatos) WHERE {
            ?s a :Presidente .
            ?s :mandato ?mandato ;
                :nome ?nome .
        }
        GROUP BY ?nome
        ORDER BY ?nome
    """
    result = query_graphdb(endpoint, sparql_query)
    presidentes = [(r['nome']['value'], r['numMandatos']['value']) for r in result['results']['bindings']]
    
    true_false_questions2 = []
    random.shuffle(presidentes)
    for item in presidentes:
        if random.choice([True, False]):
            question = {
                "question": f"O presidente {item[0]} teve {item[1]} mandato(s)?",
                "options": ["Verdadeiro", "Falso"],
                "answer": "Verdadeiro"
            }
        else:
            other_num = random.choice([i[1] for i in presidentes if i != item])
            question = {
                "question": f"O presidente {item[0]} teve {other_num} mandato(s)?",
                "options": ["Verdadeiro", "Falso"],
                "answer": "Falso"
            }
        true_false_questions2.append(question)

    # Ensure the correct number of questions for each type
    evenly_distributed_questions = (
        random.sample(multiple_choice_questions1, questions_per_type) +
        random.sample(multiple_choice_questions2, questions_per_type) +
        random.sample(correspond_questions_list, questions_per_type) +
        random.sample(correspond_questions2_list, questions_per_type) +
        random.sample(true_false_questions, questions_per_type) +
        random.sample(true_false_questions2, questions_per_type)
    )
    
    random.shuffle(evenly_distributed_questions)
    return evenly_distributed_questions
