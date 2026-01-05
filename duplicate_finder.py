import os
import hashlib    #create unique code for file content

def find_duplicates(folder_path):
    hashes= {}  #store unique files
    duplicates= [] #store duplicates files

    for root, _, files in os.walk(folder_path):  #walk through all folders and subfolders
        for file in files:
            path=os.path.join(root,file)  #create full path
            with open(path, 'rb') as f:    #read file in binary mode
                file_hash = hashlib.md5(f.read()).hexdigest()  #create unique hash for file content

            if file_hash in hashes:  #check if hash already exists
                duplicates.append(path)  #add to duplicate list
            else:
                hashes[file_hash] = path  #store unique file

    return duplicates



