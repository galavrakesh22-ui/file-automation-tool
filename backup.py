import shutil
import os
from datetime import datetime    #to get current date and time

def backup_folder(source, destination):         #function to backup folder
    date = datetime.now().strftime("%Y-%m-%d_%H-%M")  #get current date and time
    backup_path = os.path.join(destination, f"backup_{date}")  #create backup folder path
    shutil.copytree(source, backup_path)   #copy entire folder to backup location
    
