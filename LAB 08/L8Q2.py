print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")
import random
randomset = {random.randrange (15,45) for _ in range (10)}
print(set)
removeset= set()
print(randomset)
c=0
for i in randomset :
    if(i<30):
        c+=1
    else:
        removeset.add(i)
randomset-=removeset
print(randomset)

