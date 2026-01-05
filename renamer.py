import os

def rename_files(folder_path, prefix):                      #function to rename files with a given prefix
    for count, file in enumerate(os.listdir(folder_path)):  #enumerate to get index and file name
        file_path = os.path.join(folder_path, file) #create full path

        if os.path.isfile(file_path):                #check if it is a file
            extension = os.path.splitext(file)[1]    #get file extension
            new_name = f"{prefix}_{count}{extension}"#create new file name wth prefix and count
            os.rename(file_path, os.path.join(folder_path, new_name)) #rename the file with new name
