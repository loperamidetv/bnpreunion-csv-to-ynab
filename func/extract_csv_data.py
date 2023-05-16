import csv

def extract_csv_data(path: str) -> list:
    """
    This fuction aims to take the raw csv file from BNP PARIBAS REUNION and 
    extract the data in a raw format to process it. 
    The output list is formatted as :
        - index 0 : []
        - index 1 : ['account type', "Account number"]
        - all indexes below are the operations from the most recent to the most ancient. 
    """
    raw_csv_data = list()

    with open(file = path, mode = 'r') as csv_input:
        reader = csv.reader(csv_input, delimiter = ';')

        for row in reader:
            raw_csv_data.append(row)
    
    return raw_csv_data