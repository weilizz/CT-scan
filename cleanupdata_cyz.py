import os

# Path to the dataset folder (images and annotations)
image_folder = "C:/Users/Hp/Downloads/Arduino_Uno/train/images"
annotation_folder = "C:/Users/Hp/Downloads/Arduino_Uno/train/labels"

# Class ID for Arduino Uno (ensure you know which class ID is for Arduino Uno)
arduino_class_id = 0  # Update with the correct class ID for Arduino Uno

# Iterate over all annotation files
for annotation_file in os.listdir(annotation_folder):
    if annotation_file.endswith(".txt"):
        # Get the corresponding image file name
        image_file = annotation_file.replace(".txt", ".jpg")


        with open(os.path.join(annotation_folder, annotation_file), "r") as file:
            lines = file.readlines()

            # If no Arduino Uno class is found, delete both the image and annotation file
            if not any(line.startswith(str(arduino_class_id)) for line in lines):
                os.remove(os.path.join(image_folder, image_file))
                os.remove(os.path.join(annotation_folder, annotation_file))
                print(f"Deleted {image_file} and {annotation_file}")

            if not any(line.startswith(str(arduino_class_id)) for line in lines):
                print(f"Deleting {image_file} and {annotation_file}")
                os.remove(os.path.join(image_folder, image_file))
                os.remove(os.path.join(annotation_folder, annotation_file))

print("Cleanup complete!")

