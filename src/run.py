import gesture_dataset
from PIL import Image
import os

# Load the dataset
dataset_path = "/home/shima/Dataset"
output_directory = "dataset"

gesture_dataset.load_dataset(dataset_path, output_directory)
