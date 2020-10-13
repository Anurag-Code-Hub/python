import csv
row_list = [["SN", "Name", "Experience"],
             [1, "Souvik", "1year"],
             [2, "Sonal", "2year"],
             [3, "Avik", "3year"]]
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)