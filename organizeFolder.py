## Questo programma ha il compito di classificare ed organizzare il contenuto della
#  cartella FileOrganizer; fondamentale importare i seguenti moduli

import os
import shutil

#stabiliamo il percorso per accedere alla cartella 
path = "/Users/jacopocilibrasi/desktop/FileOrganizer/files"
#creiamo una lista con il contenuto della cartella del path
names = os.listdir(path)
#definiamo della stringe da aggiungere al momento della creazione di nuove cartelle
folder_name = ['_audio', '_image', '_txt']
#creiamo un loop per generare le cartelle necessarie al riordino della cartella file
#FileOrganizer
#for x in folder_name:
    #if not os.path.exists(path+'/files'+ x):
        #os.makedirs(path+'/files'+ x)
gen = [os.makedirs(path+'/files'+ x) for x in ('_audio', '_image', '_txt') if not os.path.exists(path+'/files'+ x)]

#creiamo un ciclo in cui classifichiamo ogni file presente
#(per classificare i file ho utilizzato una funzione)
#ne printiamo le caratteristiche e le scriviamo anche in un file csv

outfile = open("fileOrganizer.csv", "w")

from csv import writer
csvWriter = writer(outfile)
csvWriter.writerow(["Name", "fileType", "Byte"])

def fileType(file_ext):
    if file_ext == ".jpeg" or file_ext == ".png" or file_ext == ".jpg" :
        return "image"
    elif file_ext == ".mp3":
        return "audio"
    elif file_ext == ".odt" or file_ext == ".txt":
        return "doc" 
    else:
        return "folder"

for file in names:
    filename, file_ext = os.path.splitext(file)
    file_stats = os.stat(path)
    print(f"Name:{filename} Type:{fileType(file_ext)} Byte:{file_stats.st_size}")
    csvWriter.writerow([f"{filename}", f"{fileType(file_ext)}", f"{file_stats.st_size}"])

     
    try:
        if not file_ext:
            pass
        
        elif file_ext in (".mp3"):
            shutil.move(path+'/'+file, path+ '/files_audio/'+ file)
            
        elif file_ext in (".png", ".jpeg", ".jpg"):
            shutil.move(path+'/'+file, path+ '/files_image/'+ file)

        elif file_ext in ( ".txt", ".odt"):
            shutil.move(path+'/'+file, path+ '/files_txt/'+ file)



    except(FileNotFoundError, PermissionError):
        pass

shutil.move("/Users/jacopocilibrasi/desktop/fileOrganizer.csv","/Users/jacopocilibrasi/desktop/FileOrganizer/files")
    
outfile.close()
