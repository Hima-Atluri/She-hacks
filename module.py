from msilib import sequence
from string import printable
from keras.models import model_from_json, model_from_config
import cv2
import numpy as np
from PIL import Image, ImageTk, ImageDraw, ImageFont
import PIL
import keras
# import imquality.brisque as brisque

# from keras.preprocessing.image import img_to_array
from keras.utils import img_to_array
# import matplotlib.pyplot as plt
model = model_from_config(open("weights.json", "r").read())
# load weights
model.load_weights('weights.h5')
# file_path1 = "C:/Users/HP/OneDrive/Desktop/signature.jpg"
# file_path2 = "C:/Users/HP/OneDrive/Desktop/photo.jpg"

# image quality checking
'''def imageQuality(file_path1):
    img = PIL.Image.open(file_path1)
    return brisque.score(img)'''


def check(link):

    preds = model.predict(link)
    output1 = np.argmax(preds)
    return output1
    '''
    test_url_mal = "naureen.net/etisalat.ae/index2.php"
    test_url_benign = "sixt.com/php/reservation?language=en_US"
    max_len = 75
    url = test_url_benign
    url_int_tokens = [[printable.index(x) + 1 for x in url if x in printable]]
    X = keras.utils.data_utils.pad_sequences(url_int_tokens, maxlen=max_len)

    target_proba = model.predict(X, batch_size=1)
    print(target_proba)'''
    # return target_proba


check("https://www.google.com/")
