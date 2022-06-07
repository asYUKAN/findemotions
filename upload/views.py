from django.shortcuts import render

from django.http import HttpResponse

from django.core.files.storage import FileSystemStorage
import os
from . models import Audios

from . model_test import livePredictions
aud1_path=""
def uploaded(request):

	s = Audios()

	text=''


	

	if request.method == 'POST':
		
		

		os.system("rm -r media/")

		uploaded_file=request.FILES['image']


		fs = FileSystemStorage()

		
		fs.save(uploaded_file.name,uploaded_file)



		
		
		
		s.aud_name=uploaded_file.name

		s.aud_path='media/'+uploaded_file.name 

		global aud1_path

		aud1_path=s.aud_path



			
	return render(request,'../templates/ser/index.html',{'img1':aud1_path})
		
def predict(request):
    pred = livePredictions(path='/home/yukan/MyWorkSpace/Python/Django/SRP-Voice Emotion Recognition/ser/upload/SER_model.h5',file=aud1_path)

    pred.load_model()
    res=pred.makepredictions()
    return render(request,'../templates/ser/index.html',{'predicted':res})
