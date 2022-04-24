import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

Categories = ["Ak Orda","Asia Park","Astana Opera", "Baiterek", "ENU", "Expo","Hazrat Sultan Mosque", "KAZGUU", "Keruen", "Keruen City", "Khan Shatyr", "Mega SilkWay",
              "National Museum of Kazakhstan", "Nazarbayev University", "Bottle", "container", "Cup"]

score = None


def photoPrep(filepath):
    IMG_SIZE = 180
    raw_img = cv2.imread(filepath)
# =============================================================================
#     raw_img = cv2.imread('Desktop/LoveThis/predict/0.jpg')
# =============================================================================
    print("This is {}".format(filepath))
    plt.imshow(raw_img)
    img = cv2.resize(raw_img, [IMG_SIZE, IMG_SIZE])
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    return img_array


def predicts( imgy):
    model = tf.keras.models.load_model("test2.model")
    prediction = model.predict([photoPrep(imgy)])
    score = tf.nn.softmax(prediction[0])
    return Categories[np.argmax(score)], score, Categories

def get_score():
    
    scores ={}
    for it in range(len(Categories)):
        scores[Categories[it]] = score[it] 
        print("it = {}".format(it))
        
    return scores

### Test ###

# =============================================================================
# result, res, Categories = predicts("images/Expo.jpg")
# 
# 
# print("Received image belongs to {} with {} chance".format(result,res[Categories.index(result)]*100))
# =============================================================================
