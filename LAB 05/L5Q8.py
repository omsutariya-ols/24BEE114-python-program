print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")

queue = []

def enqueue():
    item = input("Enter item to add: ")
    queue.append(item)
    print(f"{item} added to the queue.")

def dequeue():
    if not queue:
        print("Queue is empty.")
    else:
        item = queue.pop(0)
        print(f"{item} removed from the queue.")

def display():
    if not queue:
        print("Queue is empty.")
    else:
        print("Queue:", queue)

while True:
    print("\nQueue Menu")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
