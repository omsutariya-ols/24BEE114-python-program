print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")
import csv

data = [
    ["Name", "Age", "Department"],
    ["Alice", 30, "HR"],
    ["Bob", 25, "Engineering"],
    ["Charlie", 28, "Marketing"]
]

filename = "q1 employees.csv"

with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"{filename} created successfully.")

