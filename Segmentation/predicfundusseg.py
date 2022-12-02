

import os
import numpy as np
import cv2
from glob import glob
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import load_model
from keras.preprocessing.image import array_to_img, img_to_array, load_img

model= load_model('opticdiscseg_model.h5')
model.load_weights('model-optic-disk.h5')

test_images='/.../'

output_path= '/.../'
if not(os.path.isdir(output_path)):
  os.mkdir(output_path)


files= os.listdir(test_images)

for f in files:
  temp = load_img(os.path.join(test_images,f))
  temp = img_to_array(temp)
  temp = resize(temp, (256, 256, 3), mode = 'constant', preserve_range = True)/255.
  temp= np.expand_dims(temp, axis=0)
  y_pred_test= model.predict(temp)
  y_pred_test= np.squeeze(y_pred_test, axis=0)
  y_pred_test= np.squeeze(y_pred_test, axis=2)
  #pred = (pred> 0.5).astype(np.uint8)*255
  y_pred_test= y_pred_test*255
  cv2.imwrite(os.path.join(output_path,f), y_pred_test)
  print(f)