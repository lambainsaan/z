import csv


def find_branch_by_ifsc(ifsc: str) -> dict:
    with open('data.csv', newline='') as bank_data_file_reader:
        bank_data_csv_reader = csv.DictReader(bank_data_file_reader)
        for branch in bank_data_csv_reader:
            if branch['ifsc'] == ifsc:
                return dict(branch)


def find_branches_by_name_city(name: str, city: str) -> list:
    with open('data.csv', newline='') as bank_data_file_reader:
        bank_data_csv_reader = csv.DictReader(bank_data_file_reader)
        return list(filter(lambda bank: bank['bank_name'] == name.upper() and bank['city'] == city.upper(), bank_data_csv_reader))