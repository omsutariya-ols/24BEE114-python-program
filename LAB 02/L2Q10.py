print("name: om sutariya")
print("roll no.: 24bee114")

length = int(input("length: "))
breadth = int(input("breadth: "))
area = length * breadth
peri = 2 * (length + breadth)
if area > peri:
    print("area is greater than perimeter")
else:
    print("perimeter is greater than area")
