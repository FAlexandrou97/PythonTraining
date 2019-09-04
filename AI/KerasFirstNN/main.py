import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(1)
from keras.models import Sequential
from keras.layers import Dense

# Read training data
train = pd.read_csv('train.csv')
x = train.loc[:, 'pixel0':'pixel783']
y = train.loc[:,'label']
x_test = pd.read_csv('test.csv')

# Training data set
x_train = x[:40000]
y_train = y[:40000]
y_train = pd.get_dummies(y_train)

# Cross-validation set
x_dev = x[40000:42000]
y_dev = y[40000:42000]
y_dev = pd.get_dummies(y_dev)

print ("number of training examples = " + str(x_train.shape[0]))
print ("number of cross-validation examples = " + str(x_dev.shape[0]))
print ("X_train shape: " + str(x_train.shape))
print ("Y_train shape: " + str(y_train.shape))
print ("X_dev shape: " + str(x_dev.shape))
print ("Y_dev shape: " + str(y_dev.shape))

# Create model
model = Sequential()
model.add(Dense(32, activation='relu', input_dim=784))
model.add(Dense(16, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(x_train.values, y_train.values, epochs=20, batch_size=64, verbose=2,
          validation_data=(x_dev.values, y_dev.values))

predictions = model.predict_classes(x_test.values, verbose=0)
predictions_df = pd.DataFrame(predictions, columns= ['label'])
predictions_df['ImageID'] = predictions_df.index + 1
submission_df = predictions_df[predictions_df.columns[::-1]]
submission_df.to_csv("submission.csv", index=False, header=True)
submission_df.head()

# Display the 10 Digits
for n in range(1,10):
    plt.subplot(1,10,n)
    plt.imshow(x.iloc[n].values.reshape((28, 28)), cmap='gray')
    plt.title(y.iloc[n])

plt.show()