print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")
import csv

students_dict = {}

with open('q2 students.csv', mode='r') as file:
    reader = csv.reader(file)
    
    next(reader)
    
    for row in reader:
        rollno = int(row[0])
        name = row[1]
        sub1 = int(row[2])  
        sub2 = int(row[3])
        sub3 = int(row[4])
        total = sub1 + sub2 + sub3
        
        students_dict[rollno] = {
            'Name': name,
            'Subject1': sub1,
            'Subject2': sub2,
            'Subject3': sub3,
            'Total': total
        }

for rollno, details in students_dict.items():
    print(f"Roll No: {rollno}")
    for key, value in details.items():
        print(f"  {key}: {value}")
    print()
