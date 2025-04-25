print("OM SUTARIYA")
print("24BEE114")
def merge_alternate_lines(file1, file2, output_file):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
            
            lines1 = f1.readlines()
            lines2 = f2.readlines()
            
           
            merged_lines = []
            max_length = max(len(lines1), len(lines2))
            
            for i in range(max_length):
                if i < len(lines1):
                    merged_lines.append(lines1[i].strip() + '\n') 
                if i < len(lines2):
                    merged_lines.append(lines2[i].strip() + '\n')
            
           
            out.writelines(merged_lines)
        
        print(f"Merged content written to '{output_file}' successfully.")
    except FileNotFoundError:
        print("Error: One or both files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


merge_alternate_lines("file1.txt", "file2.txt", "merged_output.txt")

