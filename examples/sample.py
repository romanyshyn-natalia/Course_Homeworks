import json
import re


def simple_parser():
    '''
    () -> ()
    function with quick look at data and example of working with it.
    '''
    with open("docs/rec_1", encoding="utf-8") as f:
        data = f.read()
        inf = {}
        inf['patient_id'] = (re.findall(r'(?<= \#)\d+', data))
        inf['date'] = (re.findall(r'(?<=Discharge Date:)\s\d/\d{2}/\d{4}', data))
        inf['age'] = re.findall(r'(?<= COURSE\n)\d\d yo', data)
        inf['medication'] = (re.findall(r'(?<= MEDICATIONS:\n)\w+\s\w+\s\d{3}\s\w+', data))
    with open('patient1.json', 'w') as file:
        json.dump(inf, file)