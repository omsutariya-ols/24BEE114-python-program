print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")
a = int (input("Enter the first number"))
b=int(input("Enter the second number"))
n = int (input("Enter the range of the series"))
c=0
while(c<=n):
    c = a+b 
    print(c ,end=" ")
    a=b
    b=c
    c+=1
