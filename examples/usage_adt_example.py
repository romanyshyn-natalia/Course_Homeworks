import json
from modules.RecordADT import RecordADT, Patient

def read_reports(filename):
    doc = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            doc.append(line)
    w = [word.strip("\n") for word in doc]
    return w

def main():
    report1 = read_reports("/docs/995611")
    report2 = read_reports("/docs/10364")
    patient1 = RecordADT(report1)
    patients = Patient()
    patients.add_patient(patient1)
    patients.add_patient(RecordADT(report2))
    print(patients)
    print(patients.comming_patient()) # prints patients in front of a queue
    patients.delete_patient() # deletes first patient
    print(patients)
    with open('patient1.json', 'w+', encoding='utf-8') as file:
        for patient in patients:
            for entity in patient:
                json.dump(entity, file)
                file.write('\n')
main()
