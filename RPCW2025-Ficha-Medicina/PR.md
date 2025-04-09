# RPCW2025-Ficha-Medicina

## Estrutura do Repositório

- **ex1/**
  - `historia.ttl`: Ontologia com a representação dos conceitos de doenças, sintomas, tratamentos e pacientes.
  - `queries.txt`: SPARQL queries para extrair informações da ontologia (Ex1).
- **ex2/**
  - `povoar_ontologia.py`: Script Python que gera as instâncias a partir dos dados em CSV e JSON.
  - `diagnose_doentes.py`: Script que diagnostica pacientes com base nos sintomas e doenças.
  - `list_info.py`: Script que executa as queries dos exs 2.13, 2.14 e 2.15.
  - **datasets/**
    - `Disease_Description.csv`
    - `Disease_Treatment.csv`
    - `Disease_Syntoms.csv`
    - `doentes.json`
  - `medical.ttl`: Ontologia médica base.
  - `med_doencas.ttl`: Ontologia com mais instâncias de doenças (gerado pelo script).
  - `med_tratamentos.ttl`: Ontologia com mais instâncias de tratamentos (gerado pelo script).
  - `med_doentes.ttl`: Ontologia com mais instâncias de pacientes (gerado pelo script).
  - `12med_doentes.ttl`: Ontologia com doentes diagnosticados (Ex2.12)
  - `queries2.txt`: SPARQL queries para extrair informações da ontologia (Ex2.11).
  - `131415info.txt`: Resultado das SPARQL queries dos exs 2.13, 2.14 e 2.15.

## povoar_ontologia.py

O script `povoar_ontologia.py` processa conjuntos de dados (CSV e JSON) para gerar novas instâncias de doenças, sintomas, tratamentos e pacientes no formato .ttl. O script lê os ficheiros de entrada, transforma os dados e acrescenta novas instâncias ao ficheiro base da ontologia.

Notavelmente, caracteres como espaços e parêntesis em nomes são substituídos por underscores (por exemplo, substituindo "(" e ")" por "_") para evitar problemas ao carregar a ontologia no Protegé.