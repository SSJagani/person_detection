from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from .models import User
from django.core.files.storage import FileSystemStorage
from .static import trainner as tr
from .static import detector as dc
import cv2
import numpy as np

# Create your views here.
@api_view(["GET","POST"])
def userRegiter(request):
	try:
		print("########",request.__dict__)
		if request.method == "POST":
			user_ID = request.POST.get('User_id', False)
			user_name = request.POST.get('User_name', False)
			#Store data in database
			user=User(user_id=user_ID,user_name=user_name)
			user.save()
			return JsonResponse("Successfully Registration Your Id And Name..",safe=False)
		else:
			return HttpResponse("Not Get Methods Uesd")
	except ValueError as e:
		return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(["GET","POST"])
def imageDataset(request):
	try:
		fs = FileSystemStorage()
		if request.method == "POST":
			user_ID = request.data['user_id']
			if 'image1' in request.FILES:
				image1 = request.FILES['image1']
				filename = fs.save(user_ID+"/"+image1.name, image1)
				uploaded_file_url = fs.url(filename)
			if 'image2' in request.FILES:
				image2 = request.FILES['image2']
				filename = fs.save(user_ID+"/"+image2.name, image2)
				uploaded_file_url = fs.url(filename)
			if 'image3' in request.FILES:
				image3 = request.FILES['image3']
				filename = fs.save(user_ID+"/"+image3.name, image3)
				uploaded_file_url = fs.url(filename)
			if 'image4' in request.FILES:
				image4 = request.FILES['image4']
				filename = fs.save(user_ID+"/"+image4.name, image4)
				uploaded_file_url = fs.url(filename)
			if 'image5' in request.FILES:
				image5 = request.FILES['image5']
				filename = fs.save(user_ID+"/"+image5.name, image5)
				uploaded_file_url = fs.url(filename)
			if 'image6' in request.FILES:
				image6 = request.FILES['image6']
				filename = fs.save(user_ID+"/"+image6.name, image6)
				uploaded_file_url = fs.url(filename)
			if 'image7' in request.FILES:
				image7 = request.FILES['image7']
				filename = fs.save(user_ID+"/"+image7.name, image7)
				uploaded_file_url = fs.url(filename)
			if 'image8' in request.FILES:
				image8 = request.FILES['image8']
				filename = fs.save(user_ID+"/"+image8.name, image8)
				uploaded_file_url = fs.url(filename)
			if 'image9' in request.FILES:
				image9 = request.FILES['image9']
				filename = fs.save(user_ID+"/"+image9.name, image9)
				uploaded_file_url = fs.url(filename)
			if 'image10' in request.FILES:
				image10 = request.FILES['image10']
				filename = fs.save(user_ID+"/"+image10.name, image10)
				uploaded_file_url = fs.url(filename)
			if 'image11' in request.FILES:
				image11 = request.FILES['image11']
				filename = fs.save(user_ID+"/"+image11.name, image11)
				uploaded_file_url = fs.url(filename)
			if 'image12' in request.FILES:
				image12 = request.FILES['image12']
				filename = fs.save(user_ID+"/"+image12.name, image12)
			if 'image13' in request.FILES:
				image13 = request.FILES['image13']
				filename = fs.save(user_ID+"/"+image13.name, image13)
				uploaded_file_url = fs.url(filename)
			if 'image14' in request.FILES:
				image14 = request.FILES['image14']
				filename = fs.save(user_ID+"/"+image14.name, image14)
				uploaded_file_url = fs.url(filename)
			if 'image15' in request.FILES:
				image15 = request.FILES['image15']
				filename = fs.save(user_ID+"/"+image15.name, image15)
				uploaded_file_url = fs.url(filename)
			else:
				pass		
			l=tr.trainingImage()
			print(l)
			return HttpResponse("Successfully Uploaded ...")		
		else:
			return HttpResponse("Some Error In Uploading Image....")
	except Exception as e:
		return Response(e.args[0],status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def detector(request):
	try:
		if request.method == "POST":
			img = cv2.imdecode(np.fromstring(request.FILES['image'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
			image_id=dc.image_detect(img)
			print(image_id)
			if image_id != "Unknown" and image_id != "Face Not Detection...":
				use_name = User.objects.filter(user_id=image_id)
				name = use_name[0]
			else:
				name = image_id
			return HttpResponse("Detect Face Is "+ str(name)+" ..... ")
		else:
			return HttpResponse("Some Error In Detect Image....")
	except Exception as e:
		return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
	