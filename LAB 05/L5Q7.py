print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")
stack = []

while True:
    print("Stack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter item to push: ")
        stack.append(item)
    elif choice == '2':
        if stack:
            print("Popped item:", stack.pop())
        else:
            print("Stack is empty.")
    elif choice == '3':
        if stack:
            print("Top element:", stack[-1])
        else:
            print("Stack is empty.")
    elif choice == '4':
        if stack:
            print("Stack elements:", stack)
        else:
            print("Stack is empty.")
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
