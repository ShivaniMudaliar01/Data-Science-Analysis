from tensorflow.keras.datasets import fashion_mnist
from PIL import Image
import os

# Load dataset
(_, _), (x_test, y_test) = fashion_mnist.load_data()

# Create folder
os.makedirs("sample_images", exist_ok=True)

# Save 10 sample test images
for i in range(20):
    img = Image.fromarray(x_test[i])  # Already grayscale 28x28
    img.save(f"sample_images/sample_{i}_label_{y_test[i]}.png")
