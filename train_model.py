from ultralytics import YOLO

# Load a YOLOv8 pre-trained model
model = YOLO('yolov8n.pt')  # 'yolov8n.pt' is the smallest model; use 'yolov8m.pt' or larger if resources allow

# Train the model
model.train(data='dataset.yaml', epochs=30, imgsz=6140, batch=16)
