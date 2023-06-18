import csv
import pandas as pd
from tabulate import tabulate


xlsx_file = pd.read_excel('employee_data.xlsx')

csv_file = 'employee_data.csv'
xlsx_file.to_csv(csv_file, index=False, encoding='utf-8')

        
def transform_user_details(csv_file_name):
    new_user_data = []
    
    with open(csv_file_name) as csvfile:
        user_details_csv = csv.reader(csvfile)
        for user in user_details_csv:
            if new_user_data.count(user) == 0 and user[13] == "":
                new_user_data.append(user)
    return new_user_data



def create_new_user_data(old_file="employee_data.csv", new_file="new_employee_data.csv"):
    new_user_data = transform_user_details(old_file)
    with open(new_file, "w") as newfile:
        csv_writer = csv.writer(newfile)
        csv_writer.writerows(new_user_data)
        
print(tabulate(transform_user_details(csv_file)))

