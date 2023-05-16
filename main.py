from func.extract_csv_data import extract_csv_data
from func.get_account_info import get_account_info

def run() -> None:
    raw_csv_data = extract_csv_data(path = "input.csv")

    account = get_account_info(raw_csv_data)

    for key, value in account.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    run()