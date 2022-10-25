import csv

file = "user.csv"
fieldnames = ['first_name', 'last_name', 'age', 'city']

def form():
    values = {}
    for fieldname in fieldnames:
        value = input("please enter the "+fieldname+" :")
        values[fieldname] = value
    return values

def create():
    with open(file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        writer.writerow(form())

def main():
    create()

if __name__ == '__main__':
    main()