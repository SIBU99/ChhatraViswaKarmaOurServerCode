from keras.models import load_model
from PIL import Image
import numpy as np
from skimage import transform
from django.conf import settings
from os.path import join

def load(filename):
    url = join(settings.BASE_DIR, "PlantDiseaseDetection")
    model=load_model(join(join(url,'paddy_ml_data'),"paddy.h5"))
    np_image = Image.open(filename) #Open the image
    np_image = np.array(np_image).astype('float32')/255 #Creates a numpy array as float and divides by 255.
    np_image = transform.resize(np_image, (150, 150, 3))
    np_image = np.expand_dims(np_image, axis=0)
    result = model.predict(np_image)
    result= np.around(result,decimals=3)
    result=result*100
    return result
