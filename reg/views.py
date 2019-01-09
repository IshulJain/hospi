from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
import requests
from django.views.decorators.csrf import csrf_exempt
import json
import os
import facebook
from Auth.models import *
#from payment.models import *
from django_mobile import get_flavour
from user_agents import parse
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from django.contrib.staticfiles.templatetags.staticfiles import static
import dropbox
from django.db.models import Sum,Max
import urllib2
import cookielib
from ast import literal_eval
from xlrd import open_workbook
from xlwt import Workbook
import random
from django.utils.crypto import get_random_string
import cStringIO
from PIL import Image
import urllib
import cloudinary
import cloudinary.uploader
import cloudinary.api
import base64
from io import BytesIO
from django.core import serializers
from Auth.views import send_sms_single

@csrf_exempt
def register(request):
    response = {}
    if 1:#try:
        data = request.POST
        #form = RegisterForm(data)
        email = data.get('email',None)
        try:
            techProfile = TechProfile.objects.get(email = email)
            #user = User.objects.get(email = email)
            #messages.warning(request,"Email Already Registered !")
            #return HttpResponse("Email Already Registered!") #redirect('/register')
            return False
        except:
            bugUsername = User.objects.latest('id').id
            user = User.objects.create_user(username=str(bugUsername+1))
            techprofile = TechProfile(user = user,email = email)
        user.first_name = data.get('name','')
        password = data.get('password',"techTeam")
        user.set_password(password)
        user.save()
        print 'code base 1'
        try:
            college = College.objects.get(collegeName = data.get('college').strip())
        except:
            college = College(collegeName = data.get('college').strip())
            college.save()
        try:
        	techprofile = TechProfile.objects.get(user = user)
        except:
			techprofile = TechProfile(user = user)
        techprofile.email = email
        techprofile.technexId = "TX"+str(100000+user.id)
        techprofile.college = college
        techprofile.mobileNumber = data.get('mobileNumber')
        techprofile.year = data.get('year')
        #techprofile.apploginStatus = True
		#print "codeBaes 2"
        pins = TechProfile.objects.all().values_list("pin")
        while True:
            stringR = get_random_string(3,allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
            if stringR not in pins:
                techprofile.pin = stringR
                techprofile.save()
                break
        print techprofile        
        return techprofile
    else:#except:
        return False

@login_required(login_url = '/login/')
def intro(request):
	techids = TechProfile.objects.all().values_list('technexId')
	emails = TechProfile.objects.all().values_list('email')
	totalHostels_ = Hostel.objects.all()
	workshops = Workshops.objects.all()
	facilities = Facility.objects.all()
	user = {}
	user['name'] = request.user.first_name
	print user
	datas = json.loads(serializers.serialize('json',totalHostels_,fields = ('name','capacity','bufferSize')))
	totalHostels = []
	for data in datas:
		count = Hostel.objects.get(name = data['fields']['name']).offlineprofile_set.all().count()
		data['fields']['currentCapacity'] = data['fields']['capacity'] - count - data['fields']['bufferSize']
		totalHostels.append(data['fields'])
	return render(request,'mainPage.html',{'emails': emails,"hostels":totalHostels,'facilities':facilities,'user':user,'workshops':workshops, 'techids':techids})

@csrf_exempt
def offLineRegister(request):
	response = {}
	post = request.POST
	# post['idCard']
	try:
		try:
			offLineProfile = OffLineProfile.objects.get(techProfile__email = post['email'])
			response['status'] = 2 # Already registered 
		except:
			offLineProfile = OffLineProfile.objects.get(techProfile__technexId = post['techids'])
			response['status'] = 2 # Already registered
		return JsonResponse(response)
	except:
		try:
			try:
				techprofile = TechProfile.objects.get(email = post['email'])
			except:
				techprofile = TechProfile.objects.get(technexId = post['techids'])
		except:
			techprofile = register(request)
		offLineProfile = OffLineProfile(techProfile = techprofile,gender = int(post['gender']))

		if int(post['hospiKit']) == 1:
			techprofile.botInfo = 'given'
			techprofile.save()
		if int(post['security']) == 1:
			response['security'] = 'Reached'
			security  = Facility.objects.get(name = 'Security')
			securityTransaction = Transaction(creditor = techprofile, amount = 200, facility  = security, reciever = request.user.deskteam)
			securityTransaction.save()
		if int(post['accom']) == 1:
			response['accom'] = "Reached"
			hostel = Hostel.objects.get(name = post['hostel'])
			count = hostel.offlineprofile_set.all().count()
			if hostel.capacity <= count:
				response['status'] = 0
				return JsonResponse(response)
			accomFacility = Facility.objects.get(name = 'Accomodation')
			accomtransaction = Transaction(creditor = techprofile, amount = 500, facility = accomFacility, reciever = request.user.deskteam)
			accomtransaction.save()
			offLineProfile.hostel = hostel
		transactions = Transaction.objects.filter(creditor = techprofile)
		transactionsData = json.loads(serializers.serialize('json',transactions, fields=('amount','timeStamp','facility')))
		for transactionData in transactionsData:
			transactionData['fields']['facility'] = Facility.objects.get(id=transactionData['fields']['facility']).name
		response['paymentData'] = transactionsData
		offLineProfile.save()
		response['status'] = 1
		return JsonResponse(response)

@csrf_exempt
def details(request):
	response = {}
	post = request.POST
	try:
		offLineProfile = OffLineProfile.objects.get(techProfile__email = post['email'])
		response['status'] = 2 # Already registered
		techprofile = offLineProfile.techProfile
		#response['IdCard'] = techprofile.apploginStatus
		print(response)
		total = 0
		transactions = Transaction.objects.filter(creditor = techprofile)
		transactionsData = json.loads(serializers.serialize('json',transactions, fields=('amount','timeStamp','facility')))
		for transactionData in transactionsData:
			transactionData['fields']['facility'] = Facility.objects.get(id=transactionData['fields']['facility']).name
			total += transactionData['fields']['amount']
		techProfile = [techprofile]
		data = json.loads(serializers.serialize('json', techProfile, fields=('technexId','city','year','mobileNumber')))		
		data[0]['fields']['name'] = techProfile[0].user.first_name
		data[0]['fields']['college'] = techProfile[0].college.collegeName
		try:
			response['hostel'] = offLineProfile.hostel.name
		except:
			response['hostel'] = 'Not Alloted'
		response['data'] = data[0]['fields']
		response['paymentData'] = transactionsData
		response['total'] = total 
		if techprofile.tshirtdata == True:
			response['tshirtdata'] = 1
			if techprofile.idcard.tshirtStatus == True:
				response['tshirtGiven'] = 1
			else:
				response['tshirtGiven'] = 0
			if techprofile.tshirtsize == "":
				response['tshirtdata'] = "N/A"
				response['color'] = "N/A"
			else:	
				response['tshirtsize'] = techprofile.tshirtsize
				response['color'] = techprofile.color
		else:
			response['tshirtdata'] = 0
			response['tshirtsize'] = "N/A"
			response['color'] = "N/A"	
		print response
		if accomFlag(techprofile):
			response['accommodation'] = 1
		else:
			response['accommodation'] = 0
		if techprofile.botInfo == 'given':
			response['hospiKit'] = 1
		else:
			response['hospiKit'] = 0
		
		return JsonResponse(response)
	except:
		try:
			techProfile = TechProfile.objects.filter(email = post['email'])
			# response['IdCard'] = techProfile.apploginStatus
			print(response)
			data = json.loads(serializers.serialize('json', techProfile, fields=('technexId','city','year','mobileNumber')))		
			data[0]['fields']['name'] = techProfile[0].user.first_name
			data[0]['fields']['college'] = techProfile[0].college.collegeName
			response['status'] = 1 #For Registered techprofile but not registered offlineProfile
			response['data'] = data[0]['fields']
			transactions = Transaction.objects.filter(creditor = techProfile)
			transactionsData = json.loads(serializers.serialize('json',transactions, fields=('amount','timeStamp','facility')))
			total = 0
			for transactionData in transactionsData:
				transactionData['fields']['facility'] = Facility.objects.get(id=transactionData['fields']['facility']).name
				total += transactionData['fields']['amount']
			response['paymentData'] = transactionsData
			response['total'] = total
			if accomFlag(techProfile[0]):
				response['accommodation'] = 1
			else:
				response['accommodation'] = 0
			
			return JsonResponse(response)
		except:
			response['status'] = 0 #Not registered TechProfile
			return JsonResponse(response)


@csrf_exempt
def details1(request):
	response = {}
	post = request.POST
	try:

		offLineProfile = OffLineProfile.objects.get(techProfile__technexId = post['techids'])
		response['status'] = 2 # Already registered
		techprofile = offLineProfile.techProfile
		total = 0
		transactions = Transaction.objects.filter(creditor = techprofile)
		transactionsData = json.loads(serializers.serialize('json',transactions, fields=('amount','timeStamp','facility')))
		for transactionData in transactionsData:
			transactionData['fields']['facility'] = Facility.objects.get(id=transactionData['fields']['facility']).name
			total += transactionData['fields']['amount']
		techProfile = [techprofile]
		data = json.loads(serializers.serialize('json', techProfile, fields=('technexId','city','year','mobileNumber')))		
		data[0]['fields']['name'] = techProfile[0].user.first_name
		data[0]['fields']['college'] = techProfile[0].college.collegeName
		try:
			response['hostel'] = offLineProfile.hostel.name
		except:
			response['hostel'] = 'Not Alloted'
		response['data'] = data[0]['fields']
		response['paymentData'] = transactionsData
		response['total'] = total 
		if techprofile.tshirtdata == True:
			response['tshirtdata'] = 1
			if techprofile.idcard.tshirtStatus == True:
				response['tshirtGiven'] = 1
			else:
				response['tshirtGiven'] = 0
			if techprofile.tshirtsize == "":
				response['tshirtdata'] = "N/A"
				response['color'] = "N/A"
			else:	
				response['tshirtsize'] = techprofile.tshirtsize
				response['color'] = techprofile.color
		else:
			response['tshirtdata'] = 0
			response['tshirtsize'] = "N/A"
			response['color'] = "N/A"	
		print response
		if accomFlag(techprofile):
			response['accommodation'] = 1
		else:
			response['accommodation'] = 0
		if techprofile.botInfo == 'given':
			response['hospiKit'] = 1
		else:
			response['hospiKit'] = 0
		# response['IdCard'] = techprofile.apploginStatus	
		return JsonResponse(response)
	except:
		try:
			techProfile = TechProfile.objects.filter(technexId = post['techids'])
			data = json.loads(serializers.serialize('json', techProfile, fields=('technexId','city','year','mobileNumber')))		
			data[0]['fields']['name'] = techProfile[0].user.first_name
			data[0]['fields']['college'] = techProfile[0].college.collegeName
			response['status'] = 1 #For Registered techprofile but not registered offlineProfile
			response['data'] = data[0]['fields']
			transactions = Transaction.objects.filter(creditor = techProfile)
			transactionsData = json.loads(serializers.serialize('json',transactions, fields=('amount','timeStamp','facility')))
			total = 0
			for transactionData in transactionsData:
				transactionData['fields']['facility'] = Facility.objects.get(id=transactionData['fields']['facility']).name
				total += transactionData['fields']['amount']
			response['paymentData'] = transactionsData
			response['total'] = total
			if accomFlag(techProfile[0]):
				response['accommodation'] = 1
			else:
				response['accommodation'] = 0
			# response['IdCard'] = techProfile.apploginStatus
			return JsonResponse(response)
		except:
			response['status'] = 0 #Not registered TechProfile
			return JsonResponse(response)			


def assignHostel(gender):
	hostels = Hostel.objects.filter(genderType=gender).order_by("order")
	print gender
	currentHostel = CurrentHostel.objects.get(hostel__genderType = int(gender))
	count = currentHostel.hostel.offlineprofile_set.all().count()
	if currentHostel.hostel.capacity - count > currentHostel.hostel.bufferSize:
		return currentHostel.hostel
	else:
		for hostel in hostels:
			count_ = hostel.offlineprofile_set.all().count()
			if hostel.capacity - count_ > hostel.bufferSize:
				currentHostel.hostel = hostel
				currentHostel.save()
				return hostel
	return False


@csrf_exempt
def hostelPortal(request):
	response = {}
	currentHostels = CurrentHostel.objects.all()
	totalHostels_ = Hostel.objects.all()
	datas = json.loads(serializers.serialize('json',totalHostels_,fields = ('name','capacity','bufferSize')))
	totalHostels = []
	for data in datas:
		count = Hostel.objects.get(name = data['fields']['name']).offlineprofile_set.all().count()
		data['fields']['currentCapacity'] = data['fields']['capacity'] - count - data['fields']['bufferSize']
		totalHostels.append(data['fields'])
	if request.method == 'POST':
		post = request.POST
		hostel = Hostel.objects.get(name = post['name'])
		count = hostel.offlineprofile_set.all().count()
		if hostel.capacity < count:
			return render(request,'hostel.html',{'error':"Hostel Already Filled","currentHostels":currentHostels,"hostels":totalHostels})
		currentHostel = CurrentHostel.objects.get(hostel__genderType = hostel.genderType)
		currentHostel.hostel = hostel
		currentHostel.save()

	return render(request,'hostel.html',{'error':"",'currentHostels':currentHostels,"hostels":totalHostels})

def generateCode(techprofile):
	try:
		id = IdCard.objects.get(techProfile = techprofile)
		print id
		return id.pin
	except:	
		position = random.randint(0,3)
		response = {}
		x = techprofile.pin
		y = ['X','X','X','X','X']
		y[4] = str(position)
		if 1:
			print position
			print techprofile
			offtech = OffLineProfile.objects.get(techProfile = techprofile)
			try:
				hostel = offtech.hostel.code
				
			except:
				hostel = 'Z'
			y[position] = hostel		
			l = 0	
			for ch in range(0,3):
				if l is position:
					l = l+1
				y[l] = x[ch]
				l = l+1
			print y
			z = "".join(y)
			idCard = IdCard(techProfile = techprofile,pin = z)
			print z			
			idCard.save()		
			return z
		else:

			return 0		





@csrf_exempt
def hostelAllot(request):
	response = {}
	post = request.POST
	hostel = Hostel.objects.get(name = post['hostelName'])
	print 'here'
	try:
		profile = OffLineProfile.objects.get(techProfile__email = post['email'])
	except:
		try:
			profile = OffLineProfile.objects.get(techProfile__technexId = post['techids'])
		except:
			try:
				email1 = post['email']
				techp = TechProfile.objects.get(email = email1)
				profile = OffLineProfile(techProfile = techp)
				profile.save()
			except:
				id1 = post['techids']
				techp = TechProfile.objects.get(technexId = id1)
				profile = OffLineProfile(techProfile = techp)
				profile.save()


	# except:
	# 	email1 = post['email']
	# 	techp = TechProfile.objects.get(email=email1)
	# 	profile = OffLineProfile(techProfile=techp)
	# 	profile.save()
	print profile
	# facility = Facility.objects.get(name = 'Accommodation')
	
	count = hostel.offlineprofile_set.all().count()
	if hostel.capacity <= count:
		response['status'] = 0
		return JsonResponse(response)
	else:
		transactions = Transaction.objects.filter(creditor = profile.techProfile)
		if transactions.count() == 0:
			response['status'] = 2
			return JsonResponse(response)	
		profile.hostel = hostel
		response['hostelName'] = hostel.name
		response['status'] = 1
	profile.save()
	#pin = generateCode(profile.techProfile)
	return JsonResponse(response)

@csrf_exempt
def createIdCard(request):
	response = {}
	# post = request.POST
	# try:
	# 	techProfile = TechProfile.objects.get(email = post['identifier'])
	# 	print "HI"
	# except:
	# 	techProfile = TechProfile.objects.get(technexId = post['identifier'])
	# 	print "BYR"
	# try:
	# 	idCard = IdCard.objects.get(techProfile = techProfile)
	# 	response["status"]=1
	# except:
	# 	response["status"]=0




	# pin = generateCode(techProfile)
	# print pin
	# response['status'] = 1
	# response['pin'] = pin
	# message = "your security pin is " + str(pin) + "\n#StayTechnexed" 
	# print message
	# number = str(techProfile.mobileNumber)
	# try:	
	# 	send_sms_single(message.encode("utf-8"),number)
	# except:
	# 	pass
	print response

	return JsonResponse(response)


@csrf_exempt
def submitId(request):
	response = {}
	post = request.POST
	try:
		techProfile = TechProfile.objects.get(email = post['identifier'])
	except:
		techProfile = TechProfile.objects.get(technexId = post['identifier'])
	if 1:#try:
		print post['pin']
		try:
			idCard = IdCard.objects.get(techProfile = techProfile)
		except:
			idCard = IdCard(techProfile = techProfile)
		idCard.pin = post['pin']
		idCard.save()
		response['status'] = 1
	else:#except:
		response['status'] = 0	
		# response['message'] = e
	return JsonResponse(response)



# def accomo():


def accomFlag(techprofile):
	payments = sheetpayment.objects.filter(tech = techprofile)
	basetime = datetime.datetime.strptime('Mon Feb 9 01:00:00 IST 2017','%a %b %d %X IST %Y')
	counter = 0
	for payment in payments:
		print "reached"
		time = datetime.datetime.strptime(payment.timeStamp,'%a %b %d %X IST %Y')
		if payment.ticketName == 'Innovians Technologies (Final Round) With Accomodation' or payment.ticketName == 'Innovians Technologies (Final Round)' or payment.ticketName == 'Registration - With Accomodation' or payment.ticketName == 'Startup Fair - Free Accomodation' or payment.ticketName == 'Startup Fair- Free Accomodation' or payment.ticketPrice == 1300 or payment.ticketName == 'Intellecx final round with accommodation' or payment.ticketName == 'Krackat Final Round with accommodation' or payment.ticketName == 'Krackat/Intellecx Final Round with accommodation':
		    return True
		elif basetime > time:
			print "reached"
			if payment.ticketName == '3D Printing' or payment.ticketName == 'Android App Development' or payment.ticketName == 'Bridge Design' or payment.ticketName == 'Data Mining' or payment.ticketName == 'Digital Marketing' or payment.ticketName == 'Ethical Hacking' or payment.ticketName == 'Industrial Automation - PLC & SCADA' or payment.ticketName == 'Internet of Things' or payment.ticketName == 'Swarm Robotics' or payment.ticketName =='Vision Botics (Sixth Sense Technology)' or payment.ticketName =='Automobile':
			    print "Reached"
			    g = sheetpayment.objects.filter(email = payment.email).values_list('ticketName')
			    if (u'Registration',) in g:
			    	return True
			        #send_email(payment.email,subject,body)	
	return False

@csrf_exempt
def IdCard(request):
	y = request.POST['identifier']
	response = {}
	try:
		try:
			t = TechProfile.objects.get(technexId = y)
		except:
			t = TechProfile.objects.get(email = y)
		t.apploginStatus = True
		t.save()
		response['status'] = 1
	except:
		response['status'] = 0
		
	return JsonResponse(response)

workshopsList =['E-Commerce', 'Digital Marketing', 'Sixthsense Robotics', 'Android Application Development', 'Ethical Hacking and Information Security', 'Internet of Things', 'Bridge Design', 'Cryptocurrency', 'Industrial Automation PLC and SCADA', 'Voice Controlled Automation Using Amazon Alexa', 'Autonomous Robotics (ArduBotics)', 'Artificial Intelligence and Machine Learning', 'Automobile Mechanics and IC Engines']
# @user_passes_test(lambda u: u.is_staff)
def dataA():
	t = Transaction.objects.all()
	d = DeskTeam.objects.get(user__username = 'Tech')
	pSecurity = t.filter(amount = 200)
	nSecurity = t.filter(amount = -200)
	wks = []
	others = []
	for k in t:
		if k.reciever != d:
			if k.facility.name in workshopsList:
				wks.append(k)
			elif k.amount != 200 and k.amount != -200:
				others.append(k)

	mPwks = 0
	mNwks = 0
	mNs = 0
	mPs = 0
	mPothers = 0
	mNothers = 0
	for k in pSecurity:
		mPs += k.amount
	for k in nSecurity:
		mNs += k.amount
	for k in wks:
		if k.amount > 0:
			mPwks += k.amount
		else:
			mNwks += k.amount
	for k in others:
		if k.amount > 0:
			mPothers += k.amount
		else:
			mNothers += k.amount
	response = {}
	response['pWks'] = mPwks
	response['nWks'] = mNwks
	response['Wks'] = mPwks+mNwks
	response['pS'] = mPs
	response['nS'] = mNs
	response['S'] = mPs+mNs
	response['POther'] = mPothers
	response['NOther'] = mNothers
	response['Other'] = mPothers+mNothers
	response['T'] = mPwks+mNwks+mPs+mNs+mPothers+mNothers
	print response
