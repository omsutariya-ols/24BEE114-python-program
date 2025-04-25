print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")
num = int(input("Enter a number"))
def armstrong(a):
    n=0
    sum=0
    f=a
    while(a>0):
        n=a%10
        sum=(n*n*n)+sum
        a=a//10
    if f==sum:
        print(f"{f} is an Armstrong number")
    else:
        print(f"{f} is not an armstrong number")

armstrong(num)

def prime(a):
    c=0
    for i in range (1,a+1):
        if(a%i==0):
            c+=1
    if(c==2):
        print(f"{a} is a prime number")
    else:
        print(f"{a} is not a prime number")
prime(num)

def palindrome(a):
    f=a
    rev=0
    n=0
    while(a>0):
        n=a%10
        rev=rev*10+n
        a//=10
    if(f==rev):
        print(f"{f} is a palindrome number")
    else:
        print(f"{f} is not a palindrome number")
palindrome(num)

def perfect(a):
    sum=0
    for i in range (1,a):
        
        
        if(a%i==0):
           sum= sum + i
    
    if(sum==a):
        print(f"{a} is a perfect number")
    else:
        print(f"{a} is not a perfect number")
perfect(num)

def automorphic(a):
    square = a*a
    lasttwo = square%100
    if(a==lasttwo):
        print(f"{a} is an automorphic number")
    else:
        print(f"{a} is not an automorphic number")
automorphic (num)
