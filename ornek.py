import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Veri setini yükle
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Veriyi normalleştir (0-255 aralığını 0-1 arasına getir)
x_train, x_test = x_train / 255.0, x_test / 255.0

# Yapay sinir ağı modeli oluştur
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# Modeli derle
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Modeli eğit
model.fit
(x_train, y_train, epochs=5)

# Modeli test et
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test doğruluk oranı: {test_acc:.2f}")

# Örnek bir tahmin yap
predictions = model.predict(x_test)
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.title(f"Tahmin: {np.argmax(predictions[0])}")
plt.show
()
