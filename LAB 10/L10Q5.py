print("OM SUTARIYA")
print("24BEE114")
def copy_and_convert_to_uppercase(source_file, target_file):
    try:
        
        with open(source_file, 'r') as infile:
            content = infile.read()
        
       
        modified_content = content.upper()
        
        
        with open(target_file, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Contents copied from '{source_file}' to '{target_file}' with all lowercase letters converted to uppercase.")
    except FileNotFoundError:
        print(f"Error: '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


copy_and_convert_to_uppercase("input.txt", "output.txt")

