import os

# Directory where your label files are stored
label_dir = 'C:/Users/Hp/Downloads/motorwheel/test/labels'

# New class label (e.g., 1)
new_class_id = 3

# Function to update all classes in label files
def update_labels(label_dir, new_class_id):
    # Get all label files (typically .txt files)
    label_files = [f for f in os.listdir(label_dir) if f.endswith('.txt')]

    for label_file in label_files:
        # Full path to the label file
        label_path = os.path.join(label_dir, label_file)

        # Read the label file
        with open(label_path, 'r') as file:
            lines = file.readlines()

        # Process each line in the label file
        new_lines = []
        for line in lines:
            parts = line.strip().split()
            # Set the class ID to the new class ID (unconditionally)
            parts[0] = str(new_class_id)
            # Rebuild the line with the updated class ID
            new_lines.append(' '.join(parts))

        # Write back to the label file
        with open(label_path, 'w') as file:
            file.write('\n'.join(new_lines) + '\n')
        print(f"Updated {label_file} to class {new_class_id}")


# Call the function to update labels
update_labels(label_dir, new_class_id)
