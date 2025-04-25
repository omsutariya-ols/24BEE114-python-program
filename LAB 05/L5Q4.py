print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")
import random 
list =[]
def pos_neg(l):
    l = [random.randrange(-50, 50) for _ in range (30)]
    print("The randomly generated list is " ,l)
    pos =[]
    neg=[]
    for i in range (len(l)):
        if(l[i]>0):
            pos.append(i)
        else:
            neg.append(i)
    print(f"The list of negative integers is {neg}")
    print(f"The list of positive integers is {pos}")
pos_neg(list)
