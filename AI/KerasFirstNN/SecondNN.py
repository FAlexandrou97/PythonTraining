import numpy as np
import mnist
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from keras.utils import to_categorical

train_images = mnist.train_images()
train_labels = mnist.train_labels()
test_images = mnist.test_images()
test_labels = mnist.test_labels()

# Normalize
train_images = (train_images / 255) - 0.5
test_images = (test_images / 255) - 0.5

print(train_images.shape)
print(test_images.shape)


# Reshape
train_images = np.expand_dims(train_images, axis=3)
test_images = np.expand_dims(test_images, axis=3)

print("--Extracting the 3rd channel of the images--")

print(train_images.shape)
print(test_images.shape)

num_filters = 8
kernel_size = 3
pool_size = 2
model = Sequential([
    Conv2D(num_filters, kernel_size, input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=pool_size),
    Flatten(),
    Dense(10, activation='softmax')
])
model.compile('adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x=train_images,
          y=to_categorical(train_labels),  # makes labels binary (0001000000 = 3)
          epochs=5, verbose=1,  # Display training data analytically
          validation_data=(test_images, to_categorical(test_labels)))

model.save('cnn.h5')