print('Name: OM SUTARIYA')
print('Roll No.: 24BEE114')

a = input("Enter a string")
a.lower()
b=len(a)
c=0
for i in range (b):
    if(a[i]=='a' or a[i]=='e' or
a[i]=='o' or a[i]=='u' or a[i]=='i' ):
        c+=1
print(f"The number of vowels are : {c}")
