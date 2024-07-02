
import os
import shutil
import time
import pathlib
import glob
def merge_folders(source_folders, destination_folder):

    filepath = __file__ 
    parpath = pathlib.Path(filepath).parent.__str__()
    counter = 0
    destination_folder =os.path.join(parpath,destination_folder)
    for source_folder in source_folders:
        folder_path = os.path.join(parpath,source_folder,"*.jpg")
        files = glob.glob(folder_path)
        for file in files:
            path,extension = file.split(".")
            xml_file = path +".xml"
            jpg_file = path +".jpg"
            image_name = str(counter).zfill(7) +".jpg"
            xml_filename = str(counter).zfill(7) +".xml"
            xml_file_destination = os.path.join(destination_folder,xml_filename)
            image_file_destination = os.path.join(destination_folder,image_name)
            
            shutil.copy(xml_file, xml_file_destination)
            shutil.copy(jpg_file, image_file_destination)
            counter = counter + 1

# Example usage:
source_folders = ["out1","out2","out3","out4"] # List of folders to merge files from
destination_folder = "out"  # Folder where files will be merged

merge_folders(source_folders, destination_folder)