import re

def get_account_info(raw_csv_data: list) -> dict:
    """
    From the raw data we extracted and by using this function, we mean to 
    extract the account type and number. 
    We know for sure that the account information are located inside the 
    list index no. 2 because of the regular structure of the file.
    As a reminder, the raw data is a list structured as followed: 
        - Index 0 : empty list
        - Index 1 : list with:
            - index 0 : account type 
            - index 1 : account number (but uncorrectly formatted - undesired characters)

        1) We use a simple regular expression to extract the numbers 
        2) We simplify the account number to a human understandable form (the number used to log into the bank app)
        3) We get the account type
    """

    account_number = raw_csv_data[1][1]
    account_type = raw_csv_data[1][0]

    temp = list()
    for character in account_number:
        if re.match(pattern = "[0-9]", string = character):
            temp.append(character)
    account_number = "".join(temp)
    del temp

    return {"type": account_type, 
            "account_number": account_number, 
            "account_number_simplified": account_number[8:16]}




