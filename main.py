import csv

def form(fieldnames):
    values = {}
    for fieldname in fieldnames:
        value = input("please enter the "+fieldname+" :")
        values[fieldname] = value
    return values

def create(file, fieldnames):
    with open(file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        writer.writerow(form(fieldnames))

def main():
    file = "user.csv"
    fieldnames = ['first_name', 'last_name', 'age', 'city']
    create(file, fieldnames)

if __name__ == '__main__':
    main()