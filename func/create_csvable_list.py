from .get_account_info import get_account_info
import re

def create_csvable_list(raw_csv_data: list) -> list:
    """
    This function has ... simple functions. 
        1) Modify the header line to add 
            - type
            - account number
        2) Add the account information to each operation lines
        3) Check by RE 

    NB: the old header is:
    ['DATE OPERATION', 'MONTANT', 'DEVISE', 'LIBELLE', 'INFO COMPLEMENTAIRE', 'DATE VALEUR', 'TYPE DE COMPTE', 'NUMERO DE COMPTE']
    """
    # 1) Modify the header line
    header = ['DATE', 'PAYEE', 'MEMO', 'OUTFLOW', 'INFLOW', 'TYPE DE COMPTE', 'NUMERO DE COMPTE']
    returned_data = list()
    returned_data.append(header)

    # 2) Add the account information to each operation line
    account_info = get_account_info(raw_csv_data)

    expression = "[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]"

    raw_csv_data.pop(0)
    raw_csv_data.pop(0)

    for row in raw_csv_data:
            row.append(account_info.get("type"))
            row.append(account_info.get("account_number"))

    

    for row in raw_csv_data:
        new_line = [None] * 7 
        if re.match(pattern = expression, string = row[0]):
            new_line = [None] * 7 
            # This "if" condition is equivalent to "if the line contains a date then..."
            # This is a reminder of the new header structure
            # ['DATE', 'PAYEE', 'MEMO', 'OUTFLOW', 'INFLOW', 'TYPE DE COMPTE', 'NUMERO DE COMPTE']

            # Check if montant is neg or pos, if neg, transform it into a debit, 
            # if pos, transform it into a credit
            
            # Convert the amount to float
            # Transform "-1 545,24" to "-1545.24"
            amount = row[1]
            amount = amount.split(",")

            integer_part = amount[0]
            decimal_part = amount[1]

            amount = list()

            integer_part = integer_part.split(" ")
            integer_part = "".join(integer_part)

            amount.append(integer_part)
            amount.append(decimal_part)

            amount = ".".join(amount)

            amount = float(amount)
            
            
            if amount < 0: 
                new_line[3] = format(abs(amount), ".2f")
                new_line[4] = "0.00"
            if amount == 0:
                new_line[3] = "0.00"
                new_line[4] = "0.00"
            if amount > 0:
                new_line[3] = "0.00"
                new_line[4] = format(abs(amount), ".2f")
            
            new_line[0] = row[0] # DATE = DATE OPERATION
            new_line[1] = row[4] # PAYEE = INFO COMPLEMENTAIRE
            new_line[2] = row[3] # MEMO = LIBELLE
            new_line[-2] = row[-2]
            new_line[-1] = row[-1]
        
            returned_data.append(new_line)

    return returned_data
    

    

