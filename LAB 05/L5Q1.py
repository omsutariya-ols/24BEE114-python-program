print("Name : OM SUTARIYA")
print("Roll No.: 24BEE114")
import random
even=[random.randrange(2,100,2) for _ in range(4)]

odd=[random.randrange(1,100,2) for _ in range (5)]
print(f"The list of random odd numbers is : {odd}")
print(f"The list of random even numbers is : {even} ")
odd.pop(3)
print(f"The list after removing the third element from odd list is : {odd}")
odd[2] = even
print(f"The odd list after adding the even list to it at the third position is : {odd}")
flat =sorted( [*odd[:2],*even, *odd[3:]])
print(f"The flattened list is : {flat}")
