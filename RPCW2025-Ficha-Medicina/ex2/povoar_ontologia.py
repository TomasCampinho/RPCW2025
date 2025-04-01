import csv
import shutil
from collections import defaultdict
import json

symptoms_csv = "datasets/Disease_Syntoms.csv"
description_csv = "datasets/Disease_Description.csv"
treatment_csv = "datasets/Disease_Treatment.csv"

medical_ttl = "medical.ttl"
output_ttl = "med_doentes.ttl"

def load_symptoms():
    with open(symptoms_csv, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        diseases = defaultdict(set)
        symptoms = set()

        for row in reader:
            disease_name = row[0].strip().replace(" ", "_").replace("(", "_").replace(")", "_")
            symptoms_list = [symptom.strip().replace(" ", "_").replace("(", "_").replace(")", "_") 
                             for symptom in row[1].split(",")]

            for symptom in symptoms_list:
                diseases[disease_name].add(symptom)
                symptoms.add(symptom)

        return diseases, symptoms

def load_descriptions():
    descriptions = {}
    with open(description_csv, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            disease_name = row[0].strip().replace(" ", "_").replace("(", "_").replace(")", "_")
            description = row[1].strip()
            descriptions[disease_name] = description

    return descriptions

def load_treatments():
    treatments = defaultdict(set)
    treatment_instances = set()

    with open(treatment_csv, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            disease_name = row[0].strip().replace(" ", "_").replace("(", "_").replace(")", "_")
            treatment_list = [treatment.strip().replace(" ", "_").replace("(", "_").replace(")", "_")
                              for treatment in row[1].split(",")]

            for treatment in treatment_list:
                treatments[disease_name].add(treatment)
                treatment_instances.add(treatment)

    return treatments, treatment_instances

def load_patients():
    with open("datasets/doentes.json", "r") as jsonfile:
        patients_data = json.load(jsonfile)

    patients = []
    
    for i, patient in enumerate(patients_data, start=1):
        pid = f"Patient{i+ 2}"
        name = patient["nome"].strip()
        symptoms = [sym.strip().replace(" ", "_").replace("(", "_").replace(")", "_") for sym in patient["sintomas"]]
        patients.append({"id": pid, "nome": name, "sintomas": symptoms})

    return patients

def write_to_ttl(diseases, symptoms, descriptions, treatments, treatment_instances, patients):
    shutil.copyfile(medical_ttl, output_ttl)

    with open(output_ttl, "a") as ttlfile:
        existing_lines = set()
        with open(medical_ttl, "r") as medical_file:
            existing_lines.update(line.strip() for line in medical_file)

        ttlfile.write("\n# New Disease instances\n")
        for disease, disease_symptoms in diseases.items():
            if f":{disease} a :Disease ;" not in existing_lines:
                ttlfile.write(f":{disease} a :Disease ;\n")
                ttlfile.write(f"    :hasSymptom {', '.join(f':{symptom}' for symptom in disease_symptoms)}")
                if disease in treatments:
                    ttlfile.write(f" ;\n    :hasTreatment {', '.join(f':{treatment}' for treatment in treatments[disease])}")
                if disease in descriptions:
                    escaped_description = descriptions[disease].replace('\"', '\\\"')
                    ttlfile.write(f" ;\n    :hasDescription \"{escaped_description}\"")
                ttlfile.write(" .\n\n")

        ttlfile.write("\n# New Symptom instances\n")
        for symptom in symptoms:
            line = f":{symptom} a :Symptom ."
            if line not in existing_lines:
                ttlfile.write(line + "\n")

        ttlfile.write("\n# New Treatment instances\n")
        for treatment in treatment_instances:
            line = f":{treatment} a :Treatment ."
            if line not in existing_lines:
                ttlfile.write(line + "\n")
                
        ttlfile.write("\n# New Patient instances\n")
        for patient in patients:
            lines = []
            lines.append(f"    :name \"{patient['nome']}\"")
            for symptom in patient['sintomas']:
                lines.append(f"    :exhibitsSymptom :{symptom}")
            ttlfile.write(f":{patient['id']} a :Patient ;\n" + " ;\n".join(lines) + " .\n\n")

if __name__ == "__main__":
    diseases, symptoms = load_symptoms()
    descriptions = load_descriptions()
    treatments, treatment_instances = load_treatments()
    patients = load_patients()
    write_to_ttl(diseases, symptoms, descriptions, treatments, treatment_instances, patients)
