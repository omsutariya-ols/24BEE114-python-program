print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")
list =[]
def temp(l):
    l=[]
    c=[]
    for i in range (5):
        l.append((int(input("Enter the temperatures in Fahrenheit"))))   
        a=l[i]
        g = (a-32)*(5/9)
        c.append(g)
    print(f"The list in celsius is : {c}")
temp(list)
