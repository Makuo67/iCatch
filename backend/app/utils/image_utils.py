import numpy as np
import cv2
from PIL import Image


def save_image(uploaded_file):
    file_location = f"static/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
    return file_location


def load_image(image_path):
    image = Image.open(image_path)
    # Resize to match the input size of the model
    image = image.resize((224, 224))
    image = np.array(image) / 255.0   # Normalize image
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image


def normalize(heatmap):
    heatmap = np.maximum(heatmap, 0)
    heatmap = heatmap / heatmap.max()
    return heatmap
