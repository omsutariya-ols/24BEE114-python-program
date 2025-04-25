print("name: om sutariya")
print("roll no.: 24bee114")

x1 = int(input("enter x1 for point 1: "))
y1 = int(input("enter y1 for point 1: "))
x2 = int(input("enter x2 for point 2: "))
y2 = int(input("enter y2 for point 2: "))
x3 = int(input("enter x3 for point 3: "))
y3 = int(input("enter y3 for point 3: "))
area = x1 * (y2 – y3) + x2 * (y3 – y1) + x3 * (y1 – y2)
if area == 0:
    print("the points lie on the same line")
else:
    print("the points don’t lie on the same line")
