
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


def check_d_folders():
    for folder in folder_list:
        if not folder.exists():
            print(f"error, missing {folder} folder")
            sys.exit()

    


def check_d_files():

    file_list = list(downloads.iterdir())

    for file in file_list:
        if file.is_file():
            match file.suffix:
                case ".exe":
                    shutil.move(file, executables)
                case ".mp4":
                    shutil.move(file, videos)
                case ".pdf" | ".csv":
                    shutil.move(file, docs)
                case ".msi" | ".msix":
                    shutil.move(file, installers)
                case ".jpeg"| ".png"|".jpg":
                    shutil.move(file, photos)
                case _:
                    shutil.move(file, misc)
        
        else: pass


check_d_folders()
check_d_files()

    


        