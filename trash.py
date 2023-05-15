import csv
import re

def run() -> None:
    temp_csv = list()
    account_type = str()
    account_number = str()

    expression = "[0-9]"

    with open("input.csv", "r") as csv_input:
        reader = csv.reader(csv_input, delimiter=";")

        for row in reader:
            temp_csv.append(row)
    
    for i, element in enumerate(temp_csv):
        if len(element) == 0:
            del(temp_csv[i])

    for i, element in enumerate(temp_csv):
        if len(element) == 2:
            account_type = element[0]
            account_number = element[1]
            del(temp_csv[i])
    
    temp = list()
    for character in account_number:
        if re.match(expression, character):
            temp.append(character)
    account_number = "".join(temp)

    if temp_csv[0] == ['DATE OPERATION', 'MONTANT', 'DEVISE', 'LIBELLE', 'INFO COMPLEMENTAIRE', 'DATE VALEUR']:
        del temp_csv[0]

    print(account_number[8:16])
    for elt in temp_csv:
        print(elt)

    for elt in temp_csv

    

if __name__ == "__main__":
    run()