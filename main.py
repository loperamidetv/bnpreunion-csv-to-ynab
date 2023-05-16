from func.extract_csv_data import extract_csv_data
from func.create_csvable_list import create_csvable_list

def run() -> None:
    raw_csv_data = extract_csv_data(path = "input.csv")
    new_data = create_csvable_list(raw_csv_data)

    for elt in new_data:
        print(elt)

if __name__ == "__main__":
    run()