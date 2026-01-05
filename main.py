from file_organiser import organize_files
from renamer import rename_files
from duplicate_finder import find_duplicates
from backup import backup_folder

folder = input("Enter folder path: ")

while True:

        print("""
1. Organize files
2. Rename files
3. Find duplicate files
4. Backup folder
5. Exit
""")
        choice = input("Choose option: ")

        if choice == "1":
           organize_files(folder)
        elif choice == "2":
           prefix = input("Enter rename prefix: ")
           rename_files(folder, prefix)
        elif choice == "3":
           dups = find_duplicates(folder)
           for file in dups:
               print("Duplicate:", file)
        elif choice == "4":
            dest = input("Enter backup destination: ")
            backup_folder(folder, dest)
        elif choice == "5":
            break





