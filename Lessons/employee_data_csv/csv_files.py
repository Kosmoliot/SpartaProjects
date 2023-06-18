import csv
from tabulate import tabulate

# with open("user_details.csv") as csvfile:
#     csvreader = csv.reader(csvfile)
#     # print(list(csvreader)) # casting to list before printing
#     iterable_csv = iter(csvreader)
#     next(iterable_csv)
#     for line in csvreader:
#         print(line)
        
def transform_user_details(csv_file_name):
    new_user_data = []
    
    with open(csv_file_name) as csvfile:
        user_details_csv = csv.reader(csvfile)
        for user in user_details_csv:
            transformation = []
            transformation.append(user[1])
            transformation.append(user[2])
            transformation.append(user[-1])
            new_user_data.append(transformation)
    return new_user_data

print(tabulate(transform_user_details("user_details.csv")))

def create_new_user_data(old_file="user_details.csv", new_file="new_user_details.csv"):
    new_user_data = transform_user_details(old_file)
    with open(new_file, "w") as newfile:
        csv_writer = csv.writer(newfile)
        csv_writer.writerows(new_user_data)


    