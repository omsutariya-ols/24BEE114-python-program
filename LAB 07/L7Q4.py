print("Name : OM SUTARIYA")
print("Roll No. : 24BEE114")
string =[]
f = int(input("Enter the range of the string"))



for i in range (f) :
    string.append((input("Enter the string values of the dictionary")))
for word in string:
        char_count = {char: word.count(char) for char in set(word)}
        print(f"{word}: {char_count}")
