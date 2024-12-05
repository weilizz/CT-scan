import cv2
from ultralytics import YOLO

# Load the trained model
model = YOLO('runs/detect/train3/weights/best.pt')

# Open the webcam (use 0 for the default camera, or the appropriate camera index)
cap = cv2.VideoCapture(0)

# Set the desired width and height of the video frame (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Press 'q' to quit.")

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Perform inference on the frame
    results = model(frame)

    # Get the annotated frame with detections
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("Real-Time Object Detection", annotated_frame)

    # Press 'q' to quit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

