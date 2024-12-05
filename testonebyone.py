from ultralytics import YOLO

# Load the trained model
model = YOLO('runs/detect/train3/weights/best.pt')

# Perform inference on an image
results = model('C:/Users/Hp/Downloads/raspi_testimageone.jpg')

# Visualize results
results[0].show()  # Access the first (and only) result and call 'show'
