import os
from PIL import Image
import random

def generate_dummy_annotations(image):
    # Generate random bounding box coordinates
    width, height = image.size
    x_min = random.randint(0, width - 50)
    y_min = random.randint(0, height - 50)
    x_max = x_min + random.randint(10, 50)
    y_max = y_min + random.randint(10, 50)
    return [(x_min, y_min, x_max, y_max)]

def create_text_file(image_path, output_directory):
    try:
        filename = os.path.splitext(os.path.basename(image_path))[0]
        txt_path = os.path.join(output_directory, filename + ".txt")
        print(f"Creating text file for image: {image_path}")  # Add debug print statement
        print(f"Text file path: {txt_path}")  # Add debug print statement

        with open(txt_path, "w") as txt_file:
            image = Image.open(image_path)
            bounding_boxes = generate_dummy_annotations(image)
            for box in bounding_boxes:
                x_center = (box[0] + box[2]) / (2 * image.width)
                y_center = (box[1] + box[3]) / (2 * image.height)
                width = (box[2] - box[0]) / image.width
                height = (box[3] - box[1]) / image.height
                txt_file.write(f"0 {x_center} {y_center} {width} {height}\n")
        print("Text file created successfully.")  # Add debug print statement
    except Exception as e:
        print(f"Error creating text file: {e}")

# Load the dataset
dataset_path = "/home/shima/Dataset"
output_directory = "/home/shima/YOLOv5-Hand-Gesture/dataset"

# Iterate through each gesture class directory
for gesture_class in os.listdir(dataset_path):
    gesture_class_path = os.path.join(dataset_path, gesture_class)
    if os.path.isdir(gesture_class_path):
        print(f"Processing gesture class: {gesture_class}")
        # Iterate through each image in the gesture class directory
        for filename in os.listdir(gesture_class_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_path = os.path.join(gesture_class_path, filename)
                print(f"Processing image: {image_path}")
                create_text_file(image_path, output_directory)
        print("Gesture class processing finished.")


