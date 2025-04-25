Print("Name: Om Sutariya")
Print("Roll No.: 24BEE114")

Subject1 = int(input("Enter marks for Subject 1: "))
Subject2 = int(input("Enter marks for Subject 2: "))
Subject3 = int(input("Enter marks for Subject 3: "))

Total = subject1 + subject2 + subject3
Average = total / 3

If subject1 <= 39 or subject2 <= 39 or subject3 <= 39:
    Result = "Fail"
Else:
    Result = "Pass"

If subject1 >= 80:
    Grade1 = "O"
Elif subject1 >= 60:
    Grade1 = "A"
Elif subject1 >= 40:
    Grade1 = "B"
Else:
    Grade1 = "F"

If subject2 >= 80:
    Grade2 = "O"
Elif subject2 >= 60:
    Grade2 = "A"
Elif subject2 >= 40:
    Grade2 = "B"
Else:
    Grade2 = "F"

If subject3 >= 80:
    Grade3 = "O"
Elif subject3 >= 60:
    Grade3 = "A"
Elif subject3 >= 40:
    Grade3 = "B"
Else:
    Grade3 = "F"

Print(f"Result: {result}")
Print(f"Subject 1 Grade: {grade1}")
Print(f"Subject 2 Grade: {grade2}")
Print(f"Subject 3 Grade: {grade3}")
Print(f"Total Marks: {total}")
Print(f"Average Marks: {average:.2f}")

