import numpy as np
import mnist
from keras.models import Sequential, load_model

test_images = mnist.test_images()
test_labels = mnist.test_labels()

# Normalize and Reshape
test_images = (test_images / 255) - 0.5
test_images = np.expand_dims(test_images, axis=3)
model = load_model('cnn.h5')

predictions = model.predict(test_images[:25])

print("Predictions:  ", np.argmax(predictions, axis=1))
print("Actual Digits:", test_labels[:25])
