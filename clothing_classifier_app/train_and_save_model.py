import numpy as np
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.models import load_model

# 🎯 Load the dataset
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# 🧼 Normalize the data
x_train = x_train / 255.0
x_test = x_test / 255.0

# 🧠 Define the model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dropout(0.2),
    Dense(10, activation='softmax')
])

# ⚙️ Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 🚂 Train the model
model.fit(x_train, y_train, epochs=10, validation_split=0.1)

# 💾 Save the model
model.save("model.h5")
print("✅ Model saved as model.h5")
