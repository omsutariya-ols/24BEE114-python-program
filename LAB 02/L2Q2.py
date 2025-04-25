print("name: om sutariya")
print("roll no.: 24bee114")

no1 = int(input("enter number 1: "))
no2 = int(input("enter number 2: "))
no3 = int(input("enter number 3: "))

if no1 > no2:
    if no1 > no3:
        largest = no1
    else:
        largest = no3
else:
    if no2 > no3:
        largest = no2
    else:
        largest = no3

if no1 < no2:
    if no1 < no3:
        smallest = no1
    else:
      smallest = no3
else:
    if no2 < no3:
        smallest = no2
    else:
        smallest = no3

print("the largest number is:",largest)
print("the smallest number is:",smallest)
