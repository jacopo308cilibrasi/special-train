####
##Questo è un file di recap per sostare un nuovo file,
#nella sua relativa sotto cartella.

import os
import sys
import argparse
import shutil

#file = str(input("Quale file desideri spostare?"))
#stabiliamo il percorso per accedere alla cartella 
path = "/Users/jacopocilibrasi/desktop/FileOrganizer/files"
#creiamo una lista con il contenuto della cartella del path
names = os.listdir(path)

def sort(file):
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
#impostamo tramite la libreria argparse gli strumenti necessari a gestire lo script da terminale.
parser = argparse.ArgumentParser(description="file di recap per spostare file nella relativa sottocartella")
parser.add_argument("file", type=str, help="Quale file?")
args = parser.parse_args()

sort(args.file)


##Lo script funziona solo ritorna sempre il valore None,
#inoltre vorrei implementarlo meglio, non sono del tutto soddisfatto,
#accetto volentieri ragguagli.

        



    

