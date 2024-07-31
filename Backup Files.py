#Backup Files
import shutil
import os

def backup_files():
    print("Welcome to the File Backup Script!")
    source_dir = input("Enter the source directory: ")
    backup_dir = input("Enter the backup directory: ")

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    for filename in os.listdir(source_dir):
        full_file_name = os.path.join(source_dir, filename)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, backup_dir)
    print(f"Files backed up to {backup_dir}")

if __name__ == "__main__":
    backup_files()
