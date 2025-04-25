print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")
list =[("24BEE114","Hello",19),("24BEE116","Hi",18),("24BEE124","Bye",20)]
rollnum =[]
age=[]
name=[]
for i in list:
    rollnum.append(i[0])
    age.append(i[2])
    name.append(i[1])
print(f"Roll number : {rollnum}")
print(f"Name : {name}")
print(f"Age:{age}")
