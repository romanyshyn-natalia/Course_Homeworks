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
    inp = input("Enter path to patient report (e.g. /tests/976089): ")
    print("It may last 27 seconds.")
    try:
        report1 = read_reports(inp)
        patient1 = RecordADT(report1)
        with open('report1.json', 'w+', encoding='utf-8') as file:
            for entity in patient1:
                json.dump(entity, file, indent=2)
    except FileNotFoundError:
        print("You need to pass valid path!")


main()
