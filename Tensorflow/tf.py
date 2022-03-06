from tensorflow import keras
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import numpy as np
from cv2 import cv2
#from keras.preprocessing.image import img_to_array
import matplotlib.pyplot as plt
###=====Global variables=====###

batch_size = 32
img_height = 180
img_width = 180
AUTOTUNE = tf.data.experimental.AUTOTUNE
num_classes = 9

#======================================================#

###     Loading Data from PC     ###

ex_train = keras.utils.image_dataset_from_directory(
    'data', 
    labels='inferred', 
    label_mode='int',
    color_mode='rgb', 
    batch_size=batch_size, 
    image_size=(img_height, img_width), 
    shuffle=True, 
    seed=123, 
    validation_split=0.2, 
    subset='training',
    interpolation='bilinear', 
    follow_links=False,
    crop_to_aspect_ratio=True
)

ex_validation = keras.utils.image_dataset_from_directory(
    'data', 
    labels='inferred', 
    label_mode='int',
    color_mode='rgb', 
    batch_size=batch_size, 
    image_size=(img_height, img_width), 
    shuffle=True, 
    seed=123, 
    validation_split=0.2, 
    subset='validation',
    interpolation='bilinear', 
    follow_links=False,
    crop_to_aspect_ratio=True
)

#======================================================#

###     Visualising Random 9 photos     ###


plt.figure(figsize=(10, 10))
class_names = ex_train.class_names

for images, labels in ex_train.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(class_names[labels[i]])
    plt.axis("off")
    
#======================================================#
    
###     Configure the dataset for performance     #####

# cache() - keeps file on the disk during the proccess
# prefetch() -  overlaps data preprocessing and model execution while training.
    
ex_train = ex_train.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
ex_validation =ex_validation.cache().prefetch(buffer_size=AUTOTUNE)

#======================================================#

#####    Creating the Model(NN)     #####



model = Sequential([
  layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),     #normalizing
  layers.Conv2D(16, 3, padding='same', activation='relu'),              #conver 3 2d array in a single
  layers.MaxPooling2D(),
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(128, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(196, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(256, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(1024, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Flatten(),                                                     #and coverting 2d into single array
  layers.Dense(128, activation='relu'),
  layers.Dense(num_classes)
])

#======================================================#
    
#####     Compiling the Model(NN)     #####
    
model.compile(optimizer='nadam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

#======================================================#

#####    Model(NN) summary     #####
### To final report and presentation ###

model.summary()

#======================================================#

#####    Training the Model(NN)     #####

epochs = 30

history = model.fit(
  ex_train,
  validation_data=ex_validation,
  epochs=epochs
)

#======================================================#

#####     Visualize training results     #####
### To final report and presentation ###

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

#======================================================#

#####     PREDICTION     #####

raw_img = cv2.imread('predict/8.jpg')  #Choose a picture to predict
plt.imshow(raw_img)
img = cv2.resize(raw_img, [img_height, img_width])
    
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

predictions2 = model.predict(img_array)
score2 = tf.nn.softmax(predictions[0])

print("This is a prediction {} \n".format(predictions))
print("This is a score ")
for s in score:
    print(" {:.2f} ".format(100*s))
    
print(" \n")
print("These are classes {} \n".format(class_names))


print(
    "This image most likely belongs to {} with a {:.2f} percent confidence. \n"
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)

model.save('SecondTry.model')

