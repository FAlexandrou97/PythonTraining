from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
import numpy as np

base_path = 'garbageIMG/'

model = load_model('Submachine.h5')

batch_size = 32
pic_size = 48

datagen_train = ImageDataGenerator()
train_generator = datagen_train.flow_from_directory(base_path + "train",
                                                    target_size=(pic_size,pic_size),
                                                    color_mode="grayscale",
                                                    batch_size=batch_size,
                                                    class_mode='categorical',
                                                    shuffle=True)


test_datagen = ImageDataGenerator()

test_generator = test_datagen.flow_from_directory(
    directory=base_path+'/predict',
    target_size=(48, 48),
    color_mode="grayscale",
    batch_size=128,
    class_mode='categorical',
    shuffle=False
)


test_generator.reset()

pred = model.predict_generator(test_generator, verbose=1, steps=1)

# Number of the classes : 0 = cardboard ...
predicted_class_indices=np.argmax(pred,axis=1)

# Name of the classes : metal, plastic ...
labels = (train_generator.class_indices)
labels = dict((v,k) for k,v in labels.items())
predictions = [labels[k] for k in predicted_class_indices]
print(labels)

print(predictions)