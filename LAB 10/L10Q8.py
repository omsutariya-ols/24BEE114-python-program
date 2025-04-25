print("OM SUTARIYA")
print("24BEE114")

def remove_articles(source_file, target_file):
    try:
        with open(source_file, 'r') as infile:
            content = infile.read()

        
        words_to_remove = {" a ", " an ", " the "}
        for word in words_to_remove:
            content = content.replace(word, " ")

        
        with open(target_file, 'w') as outfile:
            outfile.write(content)

        print(f"Processed file saved as '{target_file}'.")
    except FileNotFoundError:
        print(f"Error: '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


remove_articles("input.txt", "output.txt")

