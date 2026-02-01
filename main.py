
from pathlib import Path
import shutil
import sys



downloads = Path.home()/"Downloads"
executables = downloads/ "executables"
photos = downloads/ "photos"
videos = downloads/ "videos"
installers = downloads/ "installers"
docs = downloads/ "docs"
misc = downloads/ "misc"




folder_list = [executables, photos, videos, installers, docs, misc]

#remember to write the similar longer hexes first
magic_dict = {


    #images and gif
    "89504E470D0A1A0A" : ".png",
    "FFD8FF"           : ".jpeg",
    "474946383761"     : ".gif",
    #------------------------------
    
    "4D5A" : ".exe",

    #------------------------------
    #audio
    "494433" : ".mp3",
    "FFFB" :".mp3",
    "FFF3": ".mp3",
    "FFF2": ".mp3",
    #------------------------------
    #docs
    "255044462D" : ".pdf",

}

#check if folder exists else create
def check_d_folders():
    for folder in folder_list:
        folder.mkdir(exist_ok=True)

#get hex
def get_file_hex(file_path, i):
    with open(file_path, "rb" ) as f:
            #read first i bytes and translate to hex
            file_bytes = f.read(i) 
            file_magic =file_bytes.hex().upper()
    return file_magic

#handle renaming and moving files
def check_rename_move(file, path, i:int =0):
    name = file.name
    destination = path/name
    if destination.exists():
        i += 1
        name = f"{file.stem}({i}){file.suffix}"
        check_rename_move(file, path, i)
    else:
        shutil.move(file, destination)
    


def check_d_files():

    file_list = list(downloads.iterdir())
    for file in file_list:
        if not file.is_file():
            continue
        
        try:

            file_magic = get_file_hex(file, 4)

            #loop and get file type from dict
            file_type = None
            for key in magic_dict :
                if file_magic.startswith(key):
                    file_type = magic_dict[key]
                    break
            #handle other cases
            else:
                file_magic = get_file_hex(file, 12)
                if "66747970" in file_magic:
                    file_type = ".mp4"
                #read suffix in case no hex number matches
                else:
                    file_type = file.suffix

            match file_type:
                case ".exe":
                    check_rename_move(file, executables)
                case ".mp4":
                    check_rename_move(file, videos)
                case ".pdf" | ".csv":
                    check_rename_move(file, docs)
                case ".msi" | ".msix":
                    check_rename_move(file, installers)
                case ".jpeg"| ".png"|".jpg"|".gif":
                    check_rename_move(file, photos)
                case _:
                    check_rename_move(file, misc)


        except PermissionError:
            print(f"Permission error for {file}")
            continue
        except:
            print(f"failed to read or move {file}")
            continue
        

check_d_folders()
check_d_files()

    


        