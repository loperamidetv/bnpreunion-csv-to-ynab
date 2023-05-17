import csv
from .extract_csv_data import extract_csv_data
from .create_csvable_list import create_csvable_list


def format_bnp_to_ynab_csv(file_path: str = "input.csv") -> None:
    """
    This function take the csv file and format it to the correct way
    returns nothing because we want to write it to the disk


    """
    data = extract_csv_data(path=file_path)
    data = create_csvable_list(data)


    with open(file='output.csv', mode='w', newline='') as output_csv:
        writer = csv.writer(output_csv)

        for row in data:
            writer.writerow(row)

    return None    