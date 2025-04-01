# RPCW2025-Ficha-Medicina

## Exercícios que faltam fazer:
    12, 13, 14, 15

## Estrutura do Repositório

- **ex1/**
  - `historia.ttl`: Ontologia em Turtle com a representação dos conceitos de doenças, sintomas, tratamentos e pacientes.
  - `queries.txt`: Consultas SPARQL para extrair informações da ontologia (Ex1).
- **ex2/**
  - `povoar ontologia.py`: Script Python que gera as instâncias a partir dos dados em CSV e JSON.
  - **datasets/**
    - `Disease_Description.csv`
    - `Disease_Treatment.csv`
    - `Disease_Syntoms.csv`
    - `doentes.json`
  - `medical.ttl`: Arquivo base com a ontologia médica.
  - `med_doencas.ttl`: Arquivo de saída com mais instâncias de doenças (gerado pelo script).
  - `med_tratamentos.ttl`: Arquivo de saída com mais instâncias de tratamentos (gerado pelo script).
  - `med_doentes.ttl`: Arquivo de saída com mais instâncias de pacientes (gerado pelo script).
  - `queries2.txt`: SPARQL queries para extrair informações da ontologia (Ex2).

## povoar_ontologia.py

O script `povoar_ontologia.py` processa conjuntos de dados (CSV e JSON) para gerar novas instâncias de doenças, sintomas, tratamentos e pacientes no formato .ttl. O script lê os ficheiros de entrada, transforma os dados e acrescenta novas instâncias ao ficheiro base da ontologia.

Notavelmente, caracteres como espaços e parêntesis em nomes são substituídos por underscores (por exemplo, substituindo "(" e ")" por "_") para evitar problemas ao carregar a ontologia no Protegé.