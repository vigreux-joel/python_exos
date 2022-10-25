import csv

file = "user.csv"
with open(file, 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'age', 'city']
    writer = csv.DictWriter(csvfile, fieldnames)

    writer.writeheader()

    values = {}
    for fieldname in fieldnames:
        value = input("please enter the "+fieldname+" :")
        values[fieldname] = value
    writer.writerow(values)