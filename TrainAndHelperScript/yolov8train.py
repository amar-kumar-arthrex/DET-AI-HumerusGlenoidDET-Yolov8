import torch
from ultralytics import YOLO
model = YOLO("yolov8s.pt")
data_yaml_path ='/Users/amarkumar/DevEnv/PythonProjects/data.yaml'
model.train(data = data_yaml_path,
            epochs=30,
            imgsz=640,
            device=torch.device("mps"),
           )

