import datetime 
import shutil
import os

while True:
    source_dir = input("Enter the source location: ").strip()
    destination_dir = input("Enter the destination location: ").strip()

    if ":" and '\\' not in source_dir and ":" and '\\' not in destination_dir:
        print("Invalid Input.")
        continue
    break

def copy_file_to_dir(source,dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest,str(today))

    try:
        shutil.copytree(source,dest_dir)
        print(f"Folder copied to {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

copy_file_to_dir(source_dir,destination_dir)