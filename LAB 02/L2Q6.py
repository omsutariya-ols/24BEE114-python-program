print("name: om sutariya")
print("roll no.: 24bee114")
a= int(input("enter a number"))
c=0
n=0
while(a>0):   
    n=a%10
    c+=1
    a//=10
print(f"the number of digits is {c}")
