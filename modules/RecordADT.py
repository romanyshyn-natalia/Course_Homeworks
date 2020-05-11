# you have to have installed nltk, spacy and pretrained model en_ner_bc5cdr_md locally.

import re
from modules.linkedQueue import LinkedQueue
import csv
import os
import nltk
from nltk.corpus import stopwords
import en_ner_bc5cdr_md

# in case of ssl error dowloading NLTK data uncoment this:
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
# nltk.download("book")

STOPWORDS = set(stopwords.words('english'))


class RecordADT:
    '''
    Class for patient record data container.
    '''

    def __init__(self, raw_data):
        '''
        (RecordADT, str) -> NoneType
        Creates a Record.
        '''
        self.patient = []
        self.raw_data = raw_data
        self.general_data = "".join(self.raw_data)
        self.patient.append(self.get_patient_id())
        self.patient.append(self.get_admission_date())
        self.patient.append(self.get_discharge_date())
        self.patient.append({"GENDER": self.get_gender()})
        self.patient.append(self.get_age())
        self.patient.append(self.get_diagnosis())
        self.patient.append(self.get_medications())

    def __repr__(self):
        '''
        Returns a printable representational string of the object.
        '''
        return str(self.patient)

    def get_admission_date(self):
        '''
        RecordADT -> dct
        Returns dates of admission.
        '''
        pattern = re.compile(r"Admission Date: (\d{1,2}/\d{1,2}/\d{1,4})")
        return {'AD': pattern.findall(self.general_data)}

    def get_discharge_date(self):
        '''
        RecordADT -> dct
        Returns dates of discharge.
        '''
        pattern = re.compile(r"Discharge Date: (\d{1,2}/\d{1,2}/\d{1,4})")
        return {'DD': pattern.findall(self.general_data)}

    def get_age(self):
        '''
        RecordADT -> dct
        Returns the age of patients.
        '''
        pattern = re.compile(r"(\d{1,2}-?\s?year[s]?-?\s?old)")
        res = list(set(pattern.findall(self.general_data)))
        return {'AGE': res}

    @staticmethod
    def simple_gender(data):
        '''
        str -> lst
        Returns the gender of a patient.
        '''
        pattern = re.compile(r"(female|male)")
        return list(set(pattern.findall(data)))

    @staticmethod
    def gender_from_word(data):
        '''
        str -> lst
        Additional function for gettig a gender of patient in case it wasn't strictly mentioned in a record.
        '''
        res = set()
        pattern = re.compile(r"(woman|lady|girl|man|boy)")
        for pattern in pattern.findall(data):
            if pattern == 'woman' or pattern == 'lady' or pattern == "girl":
                res.add('female')
                break
            if pattern == 'man' or pattern == 'boy':
                res.add('male')
        return list(res)

    def get_gender(self):
        '''
        RecordADT -> dct
        Method for extracting gender of a patient.
        '''
        return list(set(self.simple_gender(self.general_data))) or list(set(self.gender_from_word(self.general_data)))

    def get_patient_id(self):
        '''
        RecordADT -> dct
        Extracts patients ID.
        '''
        pattern = re.compile(
            r"\|\s\d+\s\|\s\|\s(\d+)\s\|\s\d{1,2}/\d{1,2}/\d{1,4}")
        return {"ID": pattern.findall(self.general_data)}

    def preprocessing(self):
        '''
        RecordADT -> str
        Extracts sections with Diagnosis and Medications from raw text.
        '''
        res = []
        pattern1 = re.compile(r"((DIAGNOSIS))")
        pattern2 = re.compile(r"((MEDICATIONS))")
        for line in self.raw_data:
            if pattern1.findall(line):
                idx = self.raw_data.index(line)
                res.append(line)
                res.append(self.raw_data[idx+1])
            if pattern2.findall(line):
                idx = self.raw_data.index(line)
                res.append(line)
                res.append(self.raw_data[idx+1])
                res.append(self.raw_data[idx+2])
                res.append(self.raw_data[idx+3])
        splitet_diseases = " ".join(res).lower()
        almost_dis = nltk.word_tokenize(splitet_diseases)
        new_words = [word for word in almost_dis if word.isalpha()]
        stop_words = stopwords.words('english') + \
            ['doctor', 'patient', 'Patient', 'physician']
        tokens_without_sw = [
            word for word in new_words if not word in stop_words]
        return " ".join(tokens_without_sw)

    def display_entities(self):
        '''
        RecordADT -> list of tuples
        Using sciSpasy pretrained model  for extracting needed word entities.
        '''
        tokens = self.preprocessing()
        nlp = en_ner_bc5cdr_md.load()
        doc = nlp(tokens)
        entity_and_labels = [(X.text, X.label_) for X in doc.ents]
        return entity_and_labels

    def get_medications(self):
        '''
        RecordADT -> dct
        Method for getting extracted medications.
        '''
        return {"MEDICATIONS": [x for (x, y) in self.display_entities() if y == 'CHEMICAL']}

    def get_diagnosis(self):
        '''
        RecordADT -> dct
        Method for getting extracted diagnosis.
        '''
        return {"DIAGNOSIS": [x for (x, y) in self.display_entities() if y == 'DISEASE']}

    def __iter__(self):
        '''
        Provides iteration of the object.
        '''
        return iter(self.patient)

    def __len__(self):
        '''
        RecordADT -> int
        Returns number of entities of one patient.
        '''
        return len(self.patient)

    def __str__(self):
        '''
        RecordADT -> str
        Provides string representation.
        '''
        return str(self.patient)


class Patient:
    '''
    Represents data container for extracted patient (from RecordADT).
    '''

    def __init__(self):
        '''
        Patient -> NoneType
        '''
        self.queue = LinkedQueue()

    def add_patient(self, record):
        '''
        Add patients to container.
        '''
        return self.queue.add(record)

    def delete_patient(self):
        '''
        Deletes a patient.
        '''
        return self.queue.pop()

    def delete_all(self):
        '''
        Clear all container.
        '''
        return self.queue.clear()

    def comming_patient(self):
        '''
        Returns first patient in a queue.
        '''
        return self.queue.peek()

    def __repr__(self):
        '''
        Returns a printable representational string of the object.
        '''
        return str(self.queue)

    def __iter__(self):
        '''
        Provides iteration of the object.
        '''
        return iter(self.queue)

    def __len__(self):
        '''
        Returns number of created patients.
        '''
        return len(self.queue)
