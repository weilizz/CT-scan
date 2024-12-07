import cv2
import json
from ultralytics import YOLO
from collections import defaultdict
import time

# Load the trained model
model = YOLO('../runs/detect/train3/weights/best.pt')

# Ecosystem mapping for object classes
ecosystem_map = {
    "Arduino_Uno": "Arduino ecosystem",
    "Arduino_Nano": "Arduino ecosystem",
    "Raspberry_Pi": "ROS ecosystem",
    "Motorwheel": "ROS ecosystem"
}
# Path to the JSON file to save detections
json_file = "detection.json"

# Initialize dictionary to store detections
detections = {
    "Arduino ecosystem": {
        "Arduino_Uno": 0,
        "Arduino_Nano": 0
    },
    "ROS ecosystem": {
        "Raspberry_Pi": 0,
        "Motorwheel": 0
    }
}
# Open the webcam (use 0 for the default camera, or the appropriate camera index)
cap = cv2.VideoCapture(0)

# Set the desired width and height of the video frame (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Press 'q' to quit.")

# Refresh rate in seconds
refresh_interval = 10
last_refresh_time = time.time()

while True:
    # Reset inventory counts for each refresh cycle
    inventory_counts = defaultdict(int)

    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Perform inference on the frame
    results = model(frame)

    # Loop through the detected objects in the frame
    for result in results[0].boxes:
        # Extract class ID and bounding box
        class_id = int(result.cls)

        # Get the class name from the model's class labels
        class_name = model.names[class_id]

        # Get the ecosystem for the detected class
        ecosystem = ecosystem_map.get(class_name, "Unknown ecosystem")

        # Update inventory counts
        inventory_counts[class_name] += 1

        # Annotate the frame with detection details
        x_min, y_min, x_max, y_max = map(int, result.xyxy[0])  # Bounding box coordinates
        label = f"{class_name} - {ecosystem}"
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        cv2.putText(frame, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the annotated frame
    cv2.imshow("Real-Time Object Detection", frame)

    # Refresh inventory counts every interval
    current_time = time.time()
    if current_time - last_refresh_time >= refresh_interval:
        # Convert inventory counts to ecosystem-based structure
        ecosystem_counts = defaultdict(dict)

        # Loop through all items in the `detections` dictionary to include zeros
        for ecosystem, items in detections.items():
            for class_name in items:
                # Update the counts from the detected inventory or default to 0
                ecosystem_counts[ecosystem][class_name] = inventory_counts.get(class_name, 0)

        # Save the inventory counts as a JSON file
        json_filename = "../detections.json"
        with open("detection.json", "w") as json_file:
            json.dump(ecosystem_counts, json_file, indent=4)

        print(f"Inventory counts saved to {json_filename}:")
        print(json.dumps(ecosystem_counts, indent=4))

        # Update last refresh time
        last_refresh_time = current_time

        # Reset inventory counts for the next refresh cycle
        inventory_counts.clear()

    # Press 'q' to quit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
