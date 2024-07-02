import os
import pathlib
import cv2
import glob


xmlpath =""

filepath = __file__ 
parpath = pathlib.Path(filepath).parent.__str__()
absxmlpath =parpath+"/out4/"
files = os.listdir(absxmlpath)

framenumberlist = sorted([  name[:-4] for name in files])

in_folder ="/20240131_150344/"
out_folder = "/out4/"
filepath = __file__ 
parpath = pathlib.Path(filepath).parent.__str__()

for frame_no in framenumberlist:
    if frame_no.__contains__("."):
        continue
    file_name = str(frame_no).zfill(7)+".png"
    img = cv2.imread(parpath + in_folder + file_name)
    cv2.imwrite(parpath+out_folder+str(frame_no).zfill(7)+".jpg",img)


