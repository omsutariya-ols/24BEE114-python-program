print("OM SUTARIYA")
print("24BEE114")
import os
import shutil

def create_and_copy_file(source_subdir, filename, target_subdir):
   
    if not os.path.exists(target_subdir):
        os.makedirs(target_subdir)
    
    
    source_path = os.path.join(source_subdir, filename)
    target_path = os.path.join(target_subdir, filename)
    
   
    if os.path.exists(source_path):
        shutil.copy(source_path, target_path)
        print(f"File '{filename}' copied to '{target_subdir}'.")
    else:
        print(f"Source file '{filename}' not found in '{source_subdir}'.")


create_and_copy_file("source_folder", "example.txt", "new_target_folder")

