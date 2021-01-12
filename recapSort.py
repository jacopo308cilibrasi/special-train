####
##Questo è un file di recap per sostare un nuovo file,
#nella sua relativa sotto cartella.
#Stript for move from the terminal the given file in is own folder.


import os
import sys
import argparse
import shutil

#file = str(input("Quale file desideri spostare?"))# Which file are you willing to move?
#path to folder 
path = "/Users/jacopocilibrasi/desktop/FileOrganizer/files"
#creiamo una lista con il contenuto della cartella del path
#making a list of folders for the different file-type(image, audio, txt...)
names = os.listdir(path)

def sort(file):
    # i used a generator for create folder(if not already exists) for the new file 
    gen = [os.makedirs(path+'/files'+ x) for x in ('_audio', '_image', '_txt') if not os.path.exists(path+'/files'+ x)]
    for file in names:
        filename, file_ext = os.path.splitext(file)

        try:
            if not file_ext:
                pass
                
        
            elif file_ext in (".mp3"):
                shutil.move(path+'/'+ file, path+ '/files_audio/'+ file)
                return "file audio"
            
            elif file_ext in (".png", ".jpeg", ".jpg"):
                shutil.move(path+'/'+ file, path+ '/files_image/'+ file)
                return "file image"
                
            elif file_ext in ( ".txt", ".odt"):
                shutil.move(path+'/'+ file, path+ '/files_txt/'+ file)
                return "file txt"



        except(FileNotFoundError, PermissionError):
            pass
#using the argparse library , we are implementing our script in order to use it from the terminal.
parser = argparse.ArgumentParser(description="file-recap for move a file in the correct folder")
parser.add_argument("file", type=str, help="what file are you willing to move?")
args = parser.parse_args()



sort(args.file)


##
#
#

        



    

