import tensorflow as tf
print("tf. version = ", tf.__version__)
import tensorflow.keras
print("keras version=", tensorflow.keras.__version__)
from keras.applications import resnet50

from tensorflow.keras.applications.resnet50 import ResNet50
#from tensorflow.keras.preprocessing import image
#from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
#import numpy as np

model = ResNet50(weights='imagenet')
