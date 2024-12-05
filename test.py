from ultralytics import YOLO
import os
import cv2

# Load the trained model
model = YOLO(r"C:/Users/Hp/AI Inventory Management/AI_Inventory_Management/runs/detect/train3/weights/best.pt")

# Path to the test images folder
test_image_folder = r"C:/Users/Hp/Downloads/Arduino_Ros/test/image"

# Output folder for saving results
output_folder = r"C:\Users\Hp\AI Inventory Management\AI_Inventory_Management\output"
os.makedirs(output_folder, exist_ok=True)

# Iterate through all test images and run inference
for image_file in os.listdir(test_image_folder):
    if image_file.lower().endswith(('.jpg', '.png', '.jpeg')):  # Adjust for image formats
        image_path = os.path.join(test_image_folder, image_file)

        # Run inference on the image
        results = model(image_path)

        # Process and save the annotated image
        for result in results:
            annotated_image = result.plot()  # Get the annotated image

            # Ensure OpenCV saves the image correctly
            output_image_path = os.path.join(output_folder, f"output_{image_file}")
            success = cv2.imwrite(output_image_path, annotated_image)

            if success:
                print(f"Saved output to {output_image_path}")
            else:
                print(f"Failed to save output for {image_file}")
