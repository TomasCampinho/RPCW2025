# RPCW2025-Ficha-Medicina

## Estrutura do Repositório

- **ex1/**
  - `historia.ttl`: Ontologia sobre a historia definida na ficha.
  - `queries.txt`: SPARQL queries para extrair informações da ontologia (Ex1).
- **ex2/**
  - `povoar ontologia.py`: Script Python que gera novas instâncias a partir dos datasets.
  - **datasets/**
    - `Disease_Description.csv`
    - `Disease_Treatment.csv`
    - `Disease_Syntoms.csv`
    - `doentes.json`
  - `medical.ttl`: Ontologia base com a ontologia médica.
  - `med_doencas.ttl`: Ontologia atualizada com mais instâncias de doenças.
  - `med_tratamentos.ttl`: Ontologia atualizada com mais instâncias de tratamentos.
  - `med_doentes.ttl`: Ontologia atualizada com mais instâncias de pacientes.
  - `queries2.txt`: SPARQL queries para extrair informações da ontologia (Ex2).

## povoar_ontologia.py

O script `povoar_ontologia.py` processa conjuntos de dados (CSV e JSON) para gerar novas instâncias de doenças, sintomas, tratamentos e pacientes no formato .ttl. O script lê os ficheiros .ttl (ontologias), transforma os dados e acrescenta novas instâncias sobre o ficheiro base da ontologia.

Notavelmente, caracteres como espaços e parêntesis em nomes são substituídos por underscores para evitar problemas ao carregar a ontologia para o Protegé.
