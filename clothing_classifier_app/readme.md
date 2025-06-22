# 👗 Clothing Item Classifier Web App

This is a simple Streamlit web application that classifies uploaded clothing images into one of 10 predefined categories using a deep learning model trained on the Fashion MNIST dataset.

---

## 🚀 Features

- Upload clothing images (even in color).
- Auto-converts to grayscale and resizes for model compatibility.
- Predicts one of 10 categories from the Fashion MNIST dataset.
- Displays prediction with confidence visualization.
- Built with TensorFlow and Streamlit — runs locally or on the web.

---

## 🏷️ Supported Classes

> Note: This app is limited to the 10 classes from the Fashion MNIST dataset:

- T-shirt/top
- Trouser
- Pullover
- Dress
- Coat
- Sandal
- Shirt
- Sneaker
- Bag
- Ankle boot

🧵 **Skirts, jeans, hats, or accessories are not recognized by this model.**

---

## 🛠️ Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/ShivaniMudaliar01/Data-Science-Analysis/tree/35fd4345f3250d49c3495f45b4894534ffb8813c/clothing_classifier_app
   cd clothing-classifier-app
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the model and save it:**
   ```bash
   python train_and_save_model.py
   ```

5. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
6. **Generate image samples (optional):**
   ```bash
   python image_generator.py
   ```

---

## 📁 Project Structure

```
.
├── app.py                   # Streamlit app
├── model.h5                 # Trained model (generated automatically after running training script)
├── train_and_save_model.py # Script to train and save model
├── image_generator.py      # Script to generate sample images (optional)
├── sample_images/           # Optional test images
└── requirements.txt         # Python dependencies

```

---

## 📸 Sample Images and Output Screeshots

![ Link](clothing_classifier_app/sample_images)

---

## 📌 Disclaimer

> ⚠️ This model is trained only on Fashion MNIST classes.  
> It may not perform well on real-world fashion items or clothing types not included in the dataset.

---

## 📚 Future Improvements

- Use real-world fashion datasets like DeepFashion or Fashion Product Images.
- Train on RGB images and add support for skirts, jeans, etc.
- Add confidence chart and top-3 predictions.
- Deploy on Streamlit Cloud or Hugging Face Spaces.

---

## 🙌 Acknowledgements

- [Fashion MNIST Dataset](https://github.com/zalandoresearch/fashion-mnist)
- [Streamlit](https://streamlit.io/)
- [TensorFlow](https://www.tensorflow.org/)

---

## 💻 Author

**Shivani Mudaliar**  
_Data Scientist | Python Developer_
