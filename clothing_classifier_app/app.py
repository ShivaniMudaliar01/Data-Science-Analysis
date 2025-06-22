import streamlit as st
import numpy as np
from PIL import Image, ImageOps
import tensorflow as tf

# 👚 Class labels
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# 🧠 Load the model
model = tf.keras.models.load_model("model.h5")

st.title("👕 Clothing Item Classifier")

st.info("""
🔍 **Disclaimer:**  
This model is trained on the Fashion MNIST dataset and supports only 10 categories:  
T-shirt/top, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, and Ankle boot.

🧵 Clothing items like **skirts, hats, jeans, or accessories** are **not recognized** by this model.
""")

st.write("Upload a clothing image (even in color), and the model will classify it.")

# 📤 Upload image
uploaded_file = st.file_uploader("Choose a clothing image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # 🖼️ Load and preprocess
    image = Image.open(uploaded_file).convert('L')        # Grayscale
    image = ImageOps.invert(image)                        # Invert for white-on-black style
    image = ImageOps.autocontrast(image)                  # Boost contrast
    image = image.resize((28, 28))                        # Resize

    st.image(image, caption="Processed Image", width=150)

    # 📊 Prepare input
    img_array = np.array(image) / 255.0
    img_array = img_array.reshape(1, 28, 28)

    # 🔮 Predict
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]

    st.markdown(f"### 🧠 AI Thinks It’s a: `{predicted_class}`")

    # 🧠 Show Top 3 Predictions
    st.subheader("🔍 Top 3 Predictions:")
    top_3 = np.argsort(prediction[0])[::-1][:3]
    for i in top_3:
        st.write(f"{class_names[i]}: {prediction[0][i]:.2%}")
