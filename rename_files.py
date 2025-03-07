import os
import random

def rename_files(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                name, ext = os.path.splitext(filename)
                random_numbers = f"{random.randint(1000, 9999):02d}"  # Ensures two digits
                new_name = f"{name}_{random_numbers}{ext}"
                new_path = os.path.join(folder_path, new_name)
                
                os.rename(file_path, new_path)
                print(f"Renamed: {filename} -> {new_name}")
    
        print("Renaming completed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    folder = input("Enter the folder path: ").strip()
    if os.path.exists(folder):
        rename_files(folder)
    else:
        print("Invalid folder path.")
