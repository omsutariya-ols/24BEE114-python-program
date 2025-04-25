print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")
prices = {
    "apple": 2.50,
    "banana": 1.20,
    "milk": 3.00,
    "bread": 2.00,
    "eggs": 2.30
}


quantities = {
    "apple": 3,
    "banana": 5,
    "milk": 2,
    "bread": 1,
    "eggs": 1
}


total = 0

for item in prices:
    if item in quantities:  
        total += prices[item] * quantities[item]

print(f"Total Bill: Rupees {total:.2f}")
