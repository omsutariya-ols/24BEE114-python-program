print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")
lst = ['madam','Python',"malayalam","12321"]
new_lst=[]
for char in lst:
    str=char[::-1]
    if(str==char):
        new_lst.append(char)
print(new_lst)
        
