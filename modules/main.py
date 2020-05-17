import json
from RecordADT import RecordADT

def read_reports(filename):
    doc = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            doc.append(line)
    w = [word.strip("\n") for word in doc]
    return w


def main():
    '''
    Main function with reading raw report and returning results in json.
    '''
    inp = input("Enter path to patient report (e.g. 976089): ")
    print("It may last 27 seconds.")
    try:
        report1 = read_reports(inp)
        patient1 = RecordADT(report1)
        keys = ["ID", "AD", "DD", "GENDER", "AGE", "DIAGNOSIS", "MEDICATIONS"]
        result = dict(zip(keys, patient1))
        with open('report1.json', 'w+', encoding='utf-8') as file:
            json.dump(result, file, indent=2)
        print("Find a json with extracted entities in your working directory.")
    except FileNotFoundError:
        print("You need to pass valid path!")
main()

   

