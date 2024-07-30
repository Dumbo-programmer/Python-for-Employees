import os
import shutil

def file_management():
    print("Welcome to the File Management Script!")
    action = input("Do you want to (1) Rename or (2) Move files? ")

    if action == "1":
        old_name = input("Enter the current file name: ")
        new_name = input("Enter the new file name: ")
        os.rename(old_name, new_name)
        print(f"File renamed to {new_name}")

    elif action == "2":
        file_path = input("Enter the file path: ")
        destination = input("Enter the destination path: ")
        shutil.move(file_path, destination)
        print(f"File moved to {destination}")

    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    file_management()
