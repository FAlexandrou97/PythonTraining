import os # used for navigating to image path
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense, Flatten, BatchNormalization, Dropout, GaussianNoise
from keras.models import Sequential, load_model
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from keras import applications
from matplotlib import pyplot as plt


numClasses = 5
base_path = 'garbageIMG/'
pic_size = 96
batch_size = 128

datagen_train = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    rescale=1/255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest',
    validation_split=0.2
)

datagen_validation = ImageDataGenerator(
    rescale=1/255
)

train_generator = datagen_train.flow_from_directory(base_path + "train",
                                                    target_size=(pic_size,pic_size),
                                                    color_mode="rgb",
                                                    batch_size=batch_size,
                                                    class_mode='categorical',
                                                    shuffle=True)

validation_generator = datagen_validation.flow_from_directory(base_path + "validation",
                                                    target_size=(pic_size,pic_size),
                                                    color_mode="rgb",
                                                    batch_size=batch_size,
                                                    class_mode='categorical',
                                                    shuffle=False)

# vgg16 model
conv_base = applications.vgg19.VGG19(include_top=False, weights='imagenet',
                                           input_shape=(pic_size, pic_size, 3), pooling=None, classes=numClasses)

# InceptionResNetV2 model
# conv_base = applications.inception_resnet_v2.InceptionResNetV2(include_top=False, weights='imagenet',
#                                           input_shape=(pic_size, pic_size, 3), pooling=None, classes=numClasses)

# MobileNetV2 model
# conv_base = applications.mobilenet_v2.MobileNetV2(include_top=False, weights='imagenet',
#                                    input_shape=(pic_size, pic_size, 3), pooling=None, classes=numClasses)

# resnet50 model
# conv_base = applications.resnet50.ResNet50(include_top=False, weights='imagenet',
#                                            input_shape=(pic_size, pic_size, 3), pooling=None, classes=numClasses)

# Xception model
# conv_base = applications.xception.Xception(include_top=False, weights='imagenet',
#                                            input_shape=(pic_size, pic_size, 3), pooling=None, classes=numClasses)

conv_base.trainable = False

# Newly added layers
model = Sequential()
model.add(conv_base)

model.add(Flatten())

# Fully connected 1st layer
model.add(Dense(512,activation='relu'))
model.add(BatchNormalization())
model.add(GaussianNoise(0.5))
model.add(Dropout(0.05))

# Fully connected 2nd layer
model.add(Dense(256,activation='relu'))
model.add(BatchNormalization())
model.add(GaussianNoise(0.5))
model.add(Dropout(0.05))

# Output layer
model.add(Dense(numClasses, activation='softmax'))

opt = Adam(lr=0.0001)
#model.load_weights("weights-rmsprop-05-0.88.hdf5")

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

filepath = "weights-pretrained-{epoch:02d}-{val_acc:.2f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]


training = model.fit_generator(generator=train_generator,
                    steps_per_epoch=train_generator.n//train_generator.batch_size,
                    epochs=250,
                    validation_data=validation_generator,
                    validation_steps=validation_generator.n//validation_generator.batch_size,
                    callbacks=callbacks_list,
                    verbose=2)

acc = training.history['acc']
val_acc = training.history['val_acc']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()
plt.show()

# model.save('pretrainedSub.h5')
