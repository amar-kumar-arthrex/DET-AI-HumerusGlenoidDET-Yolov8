import cv2
import xml.etree.ElementTree as ET
import pathlib
import os
import glob
def read_voc_annotation(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    objects = []
    for obj in root.findall('object'):
        obj_struct = {}
        obj_struct['name'] = obj.find('name').text
        bbox = obj.find('bndbox')
        obj_struct['bbox'] = [
            int(float(bbox.find('xmin').text)),
            int(float(bbox.find('ymin').text)),
            int(float(bbox.find('xmax').text)),
            int(float(bbox.find('ymax').text))
        ]
        objects.append(obj_struct)
    return objects
def draw_annotations(image, annotations):
    for annotation in annotations:
        bbox = annotation['bbox']
        cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
        cv2.putText(image, annotation['name'], (bbox[0], bbox[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


in_folder ="/out/"
filepath = __file__ 
parpath = pathlib.Path(filepath).parent.__str__()

files = glob.glob(parpath+in_folder+"*.jpg")


for file in files:
    path,extension = file.split(".")
    xml_file = path +".xml"
    jpg_file = path +".jpg"
    image = cv2.imread(jpg_file)
    annotations = read_voc_annotation(xml_file)
    draw_annotations(image, annotations)
    cv2.imwrite(jpg_file,image)
