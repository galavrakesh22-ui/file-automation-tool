import os          #Gives Python access to folders, paths, files
import shutil      #Used to move files from one place to another

def organize_files(folder_path):
     for file in os.listdir(folder_path):   #return all fies names inside the folder
          file_path =os.path.join(folder_path,file)   #creates full path

          if os.path.isfile(file_path):  #checks if it is a file
               ext=file.split('.')[-1] #gets the file extension
               ext_folder = os.path.join(folder_path, ext) #create path for extension folder

               if not os.path.exists(ext_folder):  #checks if folder exists
                  os.mkdir(ext_folder)  #creates folder it does not exist
                
                  shutil.move(file_path, os.path.join(ext_folder, file))  #movesfile to the exension folder





          
          