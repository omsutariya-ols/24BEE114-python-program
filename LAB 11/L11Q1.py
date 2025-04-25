print("Name: OM SUTARIYA")
print("Roll no.: 24BEE114")
def get_integer_input():
    while True:
        try:
            num = int(input("Enter an integer: "))
            print(f"You entered: {num}")
            return num
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

get_integer_input()
