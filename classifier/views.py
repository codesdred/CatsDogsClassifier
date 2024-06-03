from django.shortcuts import render
from django.core.files.storage import default_storage

import tensorflow as tf
import numpy as np
from keras.preprocessing import image

import os

cnn = tf.keras.models.load_model('classifier/ai_models/cnn.keras')

# Create your views here.
def home(request):
	if request.method == "POST":
		files = os.listdir('C:/Users/Administrator/Desktop/Projects/catsdogs/media')
		for file in files:
			file_path = default_storage.path(file)
			os.remove(file_path)
		if 'imginput' in request.FILES:
			file = request.FILES['imginput']
			file_name = default_storage.save(file.name, file)
			file_url = default_storage.path(file_name)
			img = image.load_img(file_url, target_size = (64, 64))
			img = image.img_to_array(img)
			img = np.expand_dims(img , axis = 0)

			res = cnn.predict(img)
			# if res[0][0] > 0.5:
			# 	pred = 'dog'
			# else:
			# 	pred = 'cat'
			val = res[0][0]*100
			dog = round(val,2)
			cat = round(100-val,2)

			filepath = '../media/'+file_name
			return render(request, 'home.html', {'image':filepath, 'dog':dog, 'cat':cat})
		else:
			return render(request, 'home.html', {'image': '../static/images/white.png', 'dog': 0.00,'cat': 0.00})
	else:
		return render(request, 'home.html', {'image': '../static/images/white.png', 'dog': 0.00,'cat': 0.00})
	

	
