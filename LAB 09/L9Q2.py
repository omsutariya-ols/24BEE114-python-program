print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")
def compute(n):
   
    n1 = int(str(n))
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    n4 = int(str(n) * 4)
    
    return n1 + n2 + n3 + n4


for i in range(4, 8):
    print(f"compute({i}) = {compute(i)}")

