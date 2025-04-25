print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")
import random
list =[]
def occurences (l):
    l =[random.randrange(1,100) for _ in range (20)]
    print(f"The randomly generated list of 20 numbers is : {l}")
    c=0
    d=19
    n = int(input("Enter the number between 1-100 for which you want to check the occurences for :"))
    
    for i in range (len(l)) :
        if(n==l[i]):
            c+=1
    
        else:
            d-=1
    
    print(f"The number of occurences of {n} is {c}")
    print(f"The number of occurences of {n} is {d}")
occurences(list)

