import json
import re
from rdflib import Graph, Namespace, Literal, URIRef, RDF
from rdflib.namespace import XSD

URI_BASE = "http://www.semanticweb.org/tomas/ontologies/2025/4/sapienta#"
base = Namespace(URI_BASE)

g = Graph()
g.parse("sapientia_base.ttl", format="turtle")

g.bind("", base)

def load_json(caminho_ficheiro):
    with open(caminho_ficheiro, 'r', encoding='utf-8') as ficheiro:
        return json.load(ficheiro)


dados_disciplinas = load_json("disciplinas.json")
dados_conceitos = load_json("conceitos.json")
dados_mestres = load_json("mestres.json")
dados_obras = load_json("obras.json")
dados_aprendizes = load_json("pg57742.json")


individuos_criados = {}

tipos_conhecimento = set()
for disciplina in dados_disciplinas["disciplinas"]:
    if "tiposDeConhecimento" in disciplina:
        for tipo in disciplina["tiposDeConhecimento"]:
            tipos_conhecimento.add(tipo)


for tipo in tipos_conhecimento:
    tipo_uri = base[re.sub(r'[^\w]', '_', tipo)]
    g.add((tipo_uri, RDF.type, base.TipoDeConhecimento))
    g.add((tipo_uri, base.temNome, Literal(tipo, datatype=XSD.string)))
    individuos_criados[tipo] = tipo_uri

periodos_historicos = set()
for conceito in dados_conceitos["conceitos"]:
    if "períodoHistórico" in conceito:
        periodos_historicos.add(conceito["períodoHistórico"])


for mestre in dados_mestres["mestres"]:
    if "períodoHistórico" in mestre:
        periodos_historicos.add(mestre["períodoHistórico"])


for periodo in periodos_historicos:
    periodo_uri = base[re.sub(r'[^\w]', '_', periodo)]
    g.add((periodo_uri, RDF.type, base.PeríodoHistorico))
    g.add((periodo_uri, base.temNome, Literal(periodo, datatype=XSD.string)))
    individuos_criados[periodo] = periodo_uri


aplicacoes = set()
for conceito in dados_conceitos["conceitos"]:
    if "aplicações" in conceito:
        for aplicacao in conceito["aplicações"]:
            aplicacoes.add(aplicacao)


for aplicacao in aplicacoes:
    aplicacao_uri = base[re.sub(r'[^\w]', '_', aplicacao)]
    g.add((aplicacao_uri, RDF.type, base.Aplicação))
    g.add((aplicacao_uri, base.temNome, Literal(aplicacao, datatype=XSD.string)))
    individuos_criados[aplicacao] = aplicacao_uri


for disciplina in dados_disciplinas["disciplinas"]:
    disciplina_nome = disciplina["nome"]
    disciplina_uri = base[re.sub(r'[^\w]', '_', disciplina_nome)]
    g.add((disciplina_uri, RDF.type, base.Disciplina))
    g.add((disciplina_uri, base.temNome, Literal(disciplina_nome, datatype=XSD.string)))
    
    if "tiposDeConhecimento" in disciplina:
        tipos_desc = ", ".join(disciplina["tiposDeConhecimento"])
        g.add((disciplina_uri, base.temDescrição, Literal(tipos_desc, datatype=XSD.string)))
        
        for tipo in disciplina["tiposDeConhecimento"]:
            if tipo in individuos_criados:
                tipo_uri = individuos_criados[tipo]
                g.add((disciplina_uri, base.pertenceA, tipo_uri))
                g.add((tipo_uri, base.contém, disciplina_uri))
    
    individuos_criados[disciplina_nome] = disciplina_uri


for conceito in dados_conceitos["conceitos"]:
    conceito_nome = conceito["nome"]
    conceito_uri = base[re.sub(r'[^\w]', '_', conceito_nome)]
    g.add((conceito_uri, RDF.type, base.Conceito))
    g.add((conceito_uri, base.temNome, Literal(conceito_nome, datatype=XSD.string)))
    
    if "períodoHistórico" in conceito:
        periodo = conceito["períodoHistórico"]
        if periodo in individuos_criados:
            periodo_uri = individuos_criados[periodo]
            g.add((conceito_uri, base.surgeEm, periodo_uri))
            g.add((periodo_uri, base.éOrigemDe, conceito_uri))
    
    if "aplicações" in conceito:
        for aplicacao in conceito["aplicações"]:
            if aplicacao in individuos_criados:
                aplicacao_uri = individuos_criados[aplicacao]
                g.add((conceito_uri, base.temAplicaçãoEm, aplicacao_uri))
                g.add((aplicacao_uri, base.éAplicaçãoDe, conceito_uri))
    
    if "conceitosRelacionados" in conceito:
        for conceito_rel in conceito["conceitosRelacionados"]:
            if conceito_rel not in individuos_criados:
                conceito_rel_uri = base[re.sub(r'[^\w]', '_', conceito_rel)]
                g.add((conceito_rel_uri, RDF.type, base.Conceito))
                g.add((conceito_rel_uri, base.temNome, Literal(conceito_rel, datatype=XSD.string)))
                individuos_criados[conceito_rel] = conceito_rel_uri
            else:
                conceito_rel_uri = individuos_criados[conceito_rel]
            
            g.add((conceito_uri, base.temConceitoRelacionado, conceito_rel_uri))
            g.add((conceito_rel_uri, base.estáRelacionadoCom, conceito_uri))
    
    individuos_criados[conceito_nome] = conceito_uri


for disciplina in dados_disciplinas["disciplinas"]:
    if "conceitos" in disciplina:
        disciplina_uri = individuos_criados.get(disciplina["nome"])
        if disciplina_uri:
            for conceito_nome in disciplina["conceitos"]:
                if conceito_nome not in individuos_criados:
                    conceito_uri = base[re.sub(r'[^\w]', '_', conceito_nome)]
                    g.add((conceito_uri, RDF.type, base.Conceito))
                    g.add((conceito_uri, base.temNome, Literal(conceito_nome, datatype=XSD.string)))
                    individuos_criados[conceito_nome] = conceito_uri
                else:
                    conceito_uri = individuos_criados[conceito_nome]
                
                g.add((disciplina_uri, base.estuda, conceito_uri))
                g.add((conceito_uri, base.éEstudadoEm, disciplina_uri))


for mestre in dados_mestres["mestres"]:
    mestre_nome = mestre["nome"]
    mestre_uri = base[re.sub(r'[^\w]', '_', mestre_nome)]
    g.add((mestre_uri, RDF.type, base.Mestre))
    g.add((mestre_uri, base.temNome, Literal(mestre_nome, datatype=XSD.string)))
    
    if "períodoHistórico" in mestre:
        g.add((mestre_uri, base.temDescrição, Literal(mestre["períodoHistórico"], datatype=XSD.string)))
    
    if "disciplinas" in mestre:
        for disciplina_nome in mestre["disciplinas"]:
            if disciplina_nome not in individuos_criados:
                disciplina_uri = base[re.sub(r'[^\w]', '_', disciplina_nome)]
                g.add((disciplina_uri, RDF.type, base.Disciplina))
                g.add((disciplina_uri, base.temNome, Literal(disciplina_nome, datatype=XSD.string)))
                individuos_criados[disciplina_nome] = disciplina_uri
            else:
                disciplina_uri = individuos_criados[disciplina_nome]
            
            g.add((mestre_uri, base.ensina, disciplina_uri))
            g.add((disciplina_uri, base.éEnsinadaPor, mestre_uri))
    
    individuos_criados[mestre_nome] = mestre_uri


for obra in dados_obras["obras"]:
    obra_titulo = obra["titulo"]
    obra_uri = base[re.sub(r'[^\w]', '_', obra_titulo)]
    g.add((obra_uri, RDF.type, base.Obra))
    g.add((obra_uri, base.temNome, Literal(obra_titulo, datatype=XSD.string)))
    
    autor_nome = obra["autor"]
    if autor_nome not in individuos_criados:
        autor_uri = base[re.sub(r'[^\w]', '_', autor_nome)]
        g.add((autor_uri, RDF.type, base.Mestre))
        g.add((autor_uri, base.temNome, Literal(autor_nome, datatype=XSD.string)))
        individuos_criados[autor_nome] = autor_uri
    else:
        autor_uri = individuos_criados[autor_nome]
    
    g.add((obra_uri, base.foiEscritoPor, autor_uri))
    g.add((autor_uri, base.escreveu, obra_uri))
    
    if "conceitos" in obra:
        for conceito_nome in obra["conceitos"]:
            if conceito_nome not in individuos_criados:
                conceito_uri = base[re.sub(r'[^\w]', '_', conceito_nome)]
                g.add((conceito_uri, RDF.type, base.Conceito))
                g.add((conceito_uri, base.temNome, Literal(conceito_nome, datatype=XSD.string)))
                individuos_criados[conceito_nome] = conceito_uri
            else:
                conceito_uri = individuos_criados[conceito_nome]
            
            g.add((obra_uri, base.explica, conceito_uri))
            g.add((conceito_uri, base.éExplicadoPor, obra_uri))
            g.add((obra_uri, base.explicaConceito, conceito_uri))
            g.add((conceito_uri, base.temObraExplicativa, obra_uri))
    
    individuos_criados[obra_titulo] = obra_uri


for aprendiz in dados_aprendizes:
    if "nome" in aprendiz and aprendiz["nome"]:
        aprendiz_nome = aprendiz["nome"]
        aprendiz_uri = base[re.sub(r'[^\w]', '_', aprendiz_nome)]
        g.add((aprendiz_uri, RDF.type, base.Aprendiz))
        g.add((aprendiz_uri, base.temNome, Literal(aprendiz_nome, datatype=XSD.string)))
        
        if "idade" in aprendiz and aprendiz["idade"]:
            idade = aprendiz["idade"]
            g.add((aprendiz_uri, base.temIdade, Literal(idade, datatype=XSD.integer)))
        
        if "disciplinas" in aprendiz and aprendiz["disciplinas"]:
            for disciplina_nome in aprendiz["disciplinas"]:
                if not disciplina_nome:
                    continue
                    
                if disciplina_nome not in individuos_criados:
                    disciplina_uri = base[re.sub(r'[^\w]', '_', disciplina_nome)]
                    g.add((disciplina_uri, RDF.type, base.Disciplina))
                    g.add((disciplina_uri, base.temNome, Literal(disciplina_nome, datatype=XSD.string)))
                    individuos_criados[disciplina_nome] = disciplina_uri
                else:
                    disciplina_uri = individuos_criados[disciplina_nome]
                
                g.add((aprendiz_uri, base.aprende, disciplina_uri))
                g.add((disciplina_uri, base.éAprendidaPor, aprendiz_uri))
                g.add((aprendiz_uri, base.temDisciplina, disciplina_uri))
                g.add((disciplina_uri, base.éDisciplinaDe, aprendiz_uri))
        
        individuos_criados[aprendiz_nome] = aprendiz_uri

g.serialize(destination="sapienta_ind.ttl", format="turtle")
