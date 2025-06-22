import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

# 👚 Class labels
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# 🧠 Load the trained model (or retrain in a notebook and save as model.h5)
model = tf.keras.models.load_model("model.h5")

st.title("👕 Clothing Item Classifier")

st.info("""
🔍 **Disclaimer:**  
This model is trained on the Fashion MNIST dataset and supports only 10 categories:  
T-shirt/top, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, and Ankle boot.

🧵 Clothing items like **skirts, hats, jeans, or accessories** are **not recognized** by this model.
""")

st.write("Upload a clothing image (even in color), and the model will classify it.")

# 📤 File uploader
uploaded_file = st.file_uploader("Choose a clothing image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('L').resize((28, 28))
    st.image(image, caption="Uploaded Image", width=150)

    # 🧪 Preprocess the image
    img_array = np.array(image) / 255.0
    img_array = img_array.reshape(1, 28, 28)

    # 🧠 Make prediction
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]

    st.markdown(f"### 🧠 AI Thinks It’s a: `{predicted_class}`")
