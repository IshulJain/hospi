# coding=utf-8
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
from django_mobile import get_flavour
from user_agents import parse
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from django.contrib.staticfiles.templatetags.staticfiles import static
import dropbox
from django.db.models import Sum,Max
import urllib2
from django.utils import timezone
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
import operator
from io import BytesIO
import pandas as pd
import csv
#from Auth.forms import *
# Create your views here.
citrixpe= static('citrix.png')
server = 'http://www.technex.in/'
app_key = 'rrevl3xuwa073fd'
app_secret = 'v51fzo5r8or1bkl'
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
sheetUrls = {

    "Digital Marketing":"https://script.google.com/a/technex.in/macros/s/AKfycbz5Ymy5Vg7oSpmilfaRQ_rdTpROQ6U2ohivsMP7-e79OHvrgS6K/exec",
    "Autonomous Robotics (ArduBotics)":"https://script.google.com/a/technex.in/macros/s/AKfycbxXvylH4qpA0HFSIc-CMy-zY8GtTuYM94YqFiDGuJwzn3K0xS_u/exec",
    "Android Application Development":"https://script.google.com/a/technex.in/macros/s/AKfycbxqf1VqKo7uk2GCtG0LNgs2Z6_-Lv3VFYxS1iGWLfdXPqWaWbmJ/exec",
    "Industrial Automation PLC and SCADA":"https://script.google.com/a/technex.in/macros/s/AKfycbylymIu146g0KDABKUt6VOKsFETrIAZPDreO5nG0Ig9aZJpRF4O/exec",
    "Ethical Hacking and Information Security":"https://script.google.com/a/technex.in/macros/s/AKfycbyMMx4BCyx0XkkxWq9VvqZWCZAfSxK1b_h9ZQnLCAFVFLbRwi8/exec",
    "Internet Of Things":"https://script.google.com/a/technex.in/macros/s/AKfycbwLN1H5lzqjNwKO3X0dRKkTsf6m7CFt78OMKIwYky2vY6NM_A4T/exec",
    "Artificial Intelligence and Machine Learning":"https://script.google.com/a/technex.in/macros/s/AKfycbznhBK3NJOPSkxpD_clpzPzWLG-3Fi72UFwcyBNp74rHXxsf0cv/exec",
    "Sixthsense Robotics":"https://script.google.com/a/technex.in/macros/s/AKfycbxcx3sEqeKGQZBV4zdvjwDzKJbYojStKWBEitw7SVOyBj8EQiQ/exec",
    "Bridge Design":"https://script.google.com/a/technex.in/macros/s/AKfycbxjqVDylXCZMV8pKjW9-vj3r4y5V-nPYe2HD5domg7db14NHhjF/exec",
    "Cryptocurrency":"https://script.google.com/a/technex.in/macros/s/AKfycbwiQhOAdl4ZcRYlLCfz_GwiEtfRWqROXLAJI9c--zSFho6tFK0/exec",
    "Augmented Reality":"https://script.google.com/a/technex.in/macros/s/AKfycbxWp0CzQOmx0NPv9XZc7AirbN_7qglzPtaQzWkGLaAd2JlkwGM/exec",
    "Voice Controlled Automation Using Amazon Alexa":"https://script.google.com/a/technex.in/macros/s/AKfycbzvXYV3fMtaSjZAqbN4kpKklGEEG9J1JM_W5kTAdIjklI-PVdm9/exec",
    "Automobile Mechanics and IC Engines":"https://script.google.com/a/technex.in/macros/s/AKfycbxJi5yTzScJ_rJwXlZ8MZ5QUB_t_oASeNkUueBhtddnz34ai_t2/exec",
    "E-Commerce":"https://script.google.com/a/technex.in/macros/s/AKfycbxgBa9H0QtAUot7m1y9BFzHOU58WbByfGIrKPy5HwI7vYbl030R/exec",

    "bridge-design": "https://script.google.com/a/technex.in/macros/s/AKfycbwlDd9WTEzkNwrRQTaqKZMXMyp8UW9Z7ckqB1HSrT01wWDZHXIe/exec", #Updated
    "e-commerce": "https://script.google.com/a/technex.in/macros/s/AKfycbxZXFxH1B7RmOEsQ0N5LGMMMg4aaiEjcrV_WJSR-kO9UpMqqeI/exec", #Updated
    "digital-marketing": "https://script.google.com/a/technex.in/macros/s/AKfycbwVAyI4IFMKG-PJ0FclvXS0IXFtLOUVEZZ2vIorY-UrjQ3z3yk/exec", #Updated
    "augmented-reality": "https://script.google.com/a/technex.in/macros/s/AKfycbydF9ZrXW7p1a6CXQlMRTsSeDVzqfYL1-tgNRAHfozgIUk360v-/exec", #Updated
    "sixthsense-robotics": "https://script.google.com/a/technex.in/macros/s/AKfycbzI-0_8PDnS0LYo2QUJ53zcSpPhajV9V38s06V0yWwQOJ-h_uuJ/exec", #Updated
    "android-application-development": "https://script.google.com/a/technex.in/macros/s/AKfycbwmuFO28O6lYFVLsClOVTMnCROVrS-vUTEmKdRq2-WpU0EdWfr_/exec", #Updated
    "ethical-hacking-information-security": "https://script.google.com/a/technex.in/macros/s/AKfycbw-H8EBmdgeVWE05UcuL4CKmI67d-kLeWlGHW2zOEQod9SriA/exec", #Updated
    "automobile-mechanics-ic-engines": "https://script.google.com/a/technex.in/macros/s/AKfycbw7eOBWS_BCbHpO5rdpcggBOjB-cb03lk2QLrykEXAGSPkBxn0K/exec", #Updated
    "autonomous-robotics-ardubotics": "https://script.google.com/a/technex.in/macros/s/AKfycbx5DtU6OQQ3536xLdGuj6rbHRBcdE9evOwa0nBkcga8UAv_mVHX/exec", #Updated
    "cryptocurrency": "https://script.google.com/a/technex.in/macros/s/AKfycbxoPSwLXi4X-6kxIdC4Dloow65s0QuMN56VfcSjosSYA0kExdFB/exec", #Updated
    "industrial-automation-plc-scada": "https://script.google.com/a/technex.in/macros/s/AKfycbw9bviaV03HbJGLAIRpYDAOmCDI5-T0qBnEqAL-uOGNGpRFVE4K/exec", #Updated
    "internet-of-things": "https://script.google.com/a/technex.in/macros/s/AKfycbwrkWl-IJRK5ujypg0HjKFhZEL05Unkdl5pWehNHxwUqmsx22cx/exec", #Updated
    "artificial-intelligence-machine-learning": "https://script.google.com/a/technex.in/macros/s/AKfycbwHuRypXQrZvrv5mphBSDVN-7isE609xoPKA0qHSJUw3z2nHIU/exec", #Updated
    "voice-controlled-automation-using-amazon-alexa": "https://script.google.com/a/technex.in/macros/s/AKfycbzn0dDn6WCY6He2srW0BL9QhixBUBS5xcZmxLoFc6tsg7ktJIs/exec", #Updated
    # "internet-of-things": "https://script.google.com/macros/s/AKfycbwLtFRKGpWk9ZxvvAoq409JqHMiykh2wWYHte6k6DUd94q7zLak/exec",
    # "data-mining" : "https://script.google.com/macros/s/AKfycbzLegitbfINZp8Ygu2aGBwLHMXaB-aQOW__B-lr6ZCD34NfliqM/exec",
    # "digital-marketing" : "https://script.google.com/macros/s/AKfycby1EOzmNiEpW5ddEbTwTIugmCidIf5H05GmMdDSxTZn15PD60c/exec",
    # "3-d-printing" : "https://script.google.com/macros/s/AKfycbz3LcIF1VOg-EJsDueeKU6Ncpl3velEbiu4D7dwCDzuVtLhGmKJ/exec",
    # "swarm-robotics" : "https://script.google.com/macros/s/AKfycbxEATq42TerLuSWCpA_mGf7meRLU5I_vNCz6HedPcsA70zTapw/exec",
    "bridge-design" : "https://script.google.com/macros/u/1/s/AKfycbxjqVDylXCZMV8pKjW9-vj3r4y5V-nPYe2HD5domg7db14NHhjF/exec",
    # "android-app-development" : "https://script.google.com/macros/s/AKfycbyUauzei8mhLXoxTtGI7_8sfIVP_7RuIeRCbV9jMjiJiA6rYdg/exec",
    # "vision-botics" : "https://script.google.com/macros/s/AKfycbwqOaFMVHeePAC_gYSCvXLSjqEhn5KcnbLkCOUQx-gHs3wgVFfp/exec",
    # "automobile" : "https://script.google.com/macros/s/AKfycbxJVGyMPPT1Aa9DjPDqqcaw0ZbWC8dYqTuZPc50iwaMISf8MNg-/exec",
    # "ethical-hacking" : "https://script.google.com/macros/s/AKfycbw_oQ_7Mxc-NpPeipvTlGYIt5Jau5PzVCYqcgMpuelCs37cVRuA/exec",
    # "industrial-automation-plc-scada" : "https://script.google.com/macros/s/AKfycbxRDIbRTg4Y9lSoPnuorqv0Q3GujmdBR-j50vyYuVlg3BMjtog/exec",

    "startup-fair-ventura" : "https://script.google.com/a/technex.in/macros/s/AKfycby7bB2SOyJz-Lj0UvjzaymFyKKoM_mwCWXkvW2Q_xGUiUZmci0/exec", #Updated
    "startup-fair-battle" : "https://script.google.com/a/technex.in/macros/s/AKfycbxklC9f27wTX4pMpnDO8VD4midp7Ygt_VfoFd4Lyh_Kiln6nuCp/exec", #Updated

    "quiz-registartion" : "https://script.google.com/macros/s/AKfycbz7irBHUHPRt7E3RE9yhGUgnRN3Cy8XKZ4ux0tbjmd6J2_vuAhN/exec",
    "dhokebaaj" : "https://script.google.com/macros/s/AKfycbwcAYUhZMqjz2qudkp6m523HOaSdWMY1pzijYHMOP5ccdL0_TkJ/exec",
    "krackatdata" : "https://script.google.com/macros/s/AKfycbzP0aInZDkeoa2JWF4eWfLzuilGmJ2hWdFYWlmbyuaio3FuB2pH/exec",
    "astroquizdata" : "https://script.google.com/macros/s/AKfycbyYzMh3r2jyG-pMI1eSeTljE6EDXmAcOqHGpfBaehV6EcfMBpzn/exec",
    "payments" : "https://script.google.com/macros/s/AKfycbzyki6cw6DkVBwpVW63pZ32X2C8K2ajaf90f4e4zB8SHrNVbloh/exec",
    "intellecxresult" : "https://script.google.com/macros/s/AKfycbysKSJ7spHDO5YMCVu82sDftLjhDTjom3r55b5tl3723_Slwsk/exec",
    "tshirt" : "https://script.google.com/macros/s/AKfycbydgOTlQjdiBzHd_10hh_zGZ372uaeNGtFIFNdw3Cbl6gKIf-8/exec",
    "innoviansfinal": "https://script.google.com/macros/s/AKfycbxs1WH83WjKaF24_6IeogV_ZOJdKw1fWRKt5ANACRTT-skzzKGN/exec"
    }
    
@csrf_exempt
def profileValidation(request):
    response = {}
    response['status'] = 0
    if request.method == 'POST':
        post = request.POST
        try:
            techprofile = TechProfile.objects.get(email = post['email'])
            response['status'] = 1
            return JsonResponse(response)
        except:
            return JsonResponse(response)
    else:
        return JsonResponse(response)

@csrf_exempt
@login_required(login_url='/register/')
def profileData(request):
    response =  {}
    print "hi"
    if request.method == 'POST':
        post = json.loads(request.body)#request.POST
        print post
        user = request.user
        techProfile = user.techprofile
        user.first_name = post['name']
        user.save()
        techProfile.mobileNumber = post['mobile']
        collegeName = post['college'].strip()
        try:
            college = College.objects.get(collegeName = collegeName)
        except:
            college = College(collegeName = collegeName)
            college.save()
        techProfile.college = college
        techProfile.city = post['city']
        techProfile.year = post['year']
        techProfile.save()
        response['status'] = 1
        return JsonResponse(response)
    else:
        response['status'] = 0
        response['error'] = 'Invalid Request!!'
        return JsonResponse(response)

@login_required(login_url='/register/')
def genetella(request):
    response = contextCall(request)
    return render(request, 'index.html',response)


def ca(request):
    return redirect("http://ca.technex.in")

def sponsors(request):
    response = {}
    sponsorTypes = SponsorshipType.objects.all().order_by('order')
    sponsorTypeArray = []
    for sponsorType in sponsorTypes:
        sponsorTypeObject = {}
        sponsors = Sponsors.objects.filter(sponsorType = sponsorType).order_by('order')
        sponsorArray = []
        for sponsor in sponsors:
            sponsorObject = {}
            # sponsorObject['category']
            sponsorObject['name'] = sponsor.name
            sponsorObject['imageLink'] = sponsor.imageLink
            sponsorObject['websiteLink'] =  sponsor.websiteLink
            sponsorArray.append(sponsorObject)
        sponsorTypeObject['type'] = sponsorType.title
        sponsorTypeObject['sponsors'] = sponsorArray
        sponsorTypeArray.append(sponsorTypeObject)
    response['data'] = sponsorTypeArray
    print response
    if(get_flavour(request) == 'full'):
        return render(request,"sponsor18d.html",{'response':response})
    else:
        return render(request,"sponsor18m.html",{'response':response}) 

def team(request):
    teams = TeamList.objects.all()
    print teams
    if(get_flavour(request)=='full'):
        return render(request,"contactsnew.html",{"teams":teams})
    else:    
        return render(request,"contactsmobilenew.html",{"teams":teams})

@csrf_exempt
def IndexView(request):
    if request.method == 'POST':
        return render(request, "indexmobilenew.html")
    agent = parse(request.META['HTTP_USER_AGENT'])
    print "hi"
    if(get_flavour(request) == 'full'):
        return render(request,"indexnew.html",{'browser':agent.browser.family})
    else:
        return render(request,"indexmobilenew.html")
def contextCall(request):
    response = {}
    try:
        user = request.user
        techprofile = user.techprofile
        response['user'] = user
        response['techProfile'] = techprofile
        teams = Team.objects.filter(Q(members = techprofile) | Q(teamLeader = techprofile)).distinct()
        print teams
        teamsData = []
        for team in teams:
            teamData = {}

            teamData['teamName'] = team.teamName
            teamData['event'] = team.event.eventName
            teamData['parentEvent'] = team.event.parentEvent.categoryName
            teamData['parentEventLink'] = team.event.parentEvent.nameSlug
            teamData['teamId'] = team.technexTeamId
            teamData['leader'] = team.teamLeader.user.first_name
            teamData['leaderEmail'] = team.teamLeader.email
            teamMemberUrl = []
            teamMemberNames = []
            for member in team.members.all():
                teamMemberNames.append(member.user.first_name.encode("utf-8"))
                try:
                    teamMemberUrl.append(member.fb.profileImage.encode("utf-8"))
                except:
                    url = "/static/profile.png"
                    teamMemberUrl.append(url)
            teamData['memberNames'] = teamMemberNames
            teamData['memberUrls'] = teamMemberUrl
            teamsData.append(teamData)

        print teamsData

        # response['notificationArray'] = notificationData(request)
        try:
            workshops = WorkshopTeam.objects.filter(Q(members = techprofile) | Q(teamLeader = techprofile)).distinct()
            workshopsData = []
            for workshop in workshops:
                workshopData = {}
                workshopData['workshop'] = workshop.workshop.title
                workshopData['teamId'] = workshop.teamId
                workshopsData.append(workshopData)
            response['workshops'] = workshopsData
            print workshopsData
        except:
            pass
        try:
            qteams = quizTeam.objects.filter(Q(members = techprofile))
            teamData = {}
            for qteam in qteams:
                teamData['teamName'] = qteam.quizTeamId
                teamData['event'] = ""
                teamData['parentEvent'] = "Intellecx"
                teamData['parentEventLink'] = "/intellecx"
                teamData['teamId'] = qteam.quizTeamId
                teamData['leaderEmail'] = ""
                teamMemberNames = []
                teamMemberUrl = []
                for member in qteam.members.all():
                    teamMemberNames.append(member.user.first_name.encode("utf-8"))
                    print teamMemberNames
                    try:
                        teamMemberUrl.append(member.fb.profileImage.encode("utf-8"))
                    except:
                        url = "/static/profile.png"
                        print url
                        teamMemberUrl.append(url)
                print teamData
                teamData['memberNames'] = teamMemberNames
                teamData['memberUrls'] = teamMemberUrl
                print teamData
                teamsData.append(teamData)
                print teamsData
        except:
            pass

        try:
            startupteams = StartUpFair.objects.filter(teamLeader = techprofile)
            for startupteam in startupteams:
                teamdata = {}
                teamdata['event'] = ""
                teamdata['teamName'] = startupteam.teamName
                teamdata['parentEvent'] = "StartupFair"
                teamdata['parentEventLink'] = "/startupfair"
                teamdata['teamId'] = ""
                teamdata['leader'] = techprofile.user.first_name
                teamdata['teamLeaderEmail'] = startupteam.teamLeader.email
                teamMemberUrl = []
                teamMemberNames = []
                startupMails = StartUpMails.objects.filter(team = startupteams)
                for startupmail in startupMails:
                    teamMemberNames.append(startupmail.email.encode("utf-8"))
                    url = "/static/profile.png"
                    teamMemberUrl.append(url)
                teamdata['memberNames'] = teamMemberNames
                teamdata['memberUrls'] = teamMemberUrl
                print teamdata
                teamsData.append(teamdata)

            response['teams'] = teamsData
        except:
            pass
        response['notifications'] =  notificationData(request)
        print response
    except:
        pass
    return response

@login_required(login_url = '/register')
def dummyDashboard(request):
    context = contextCall(request)

    context['teamsAsMember'] = Team.objects.filter(members = context['techProfile'])
    context['teamsAsLeader'] = Team.objects.filter(teamLeader = context['techProfile'])
    print context
    return redirect('/events/register')#render(request, 'eventRegistration.html',context)

@csrf_exempt
def emailUnique(request):
    response = {}
    post = request.POST #json.loads(request.body)
    try:
        techProfile = TechProfile.objects.get(email = post['email'])
        #user = User.objects.get(email = post['email'])
        response = '0'
    except:
        response = '1'
    return HttpResponse(response)

def spreadsheetfill_register(techprofile):
    timeFormat = '%d / %m / %Y'
    dic = {
        "name" : techprofile.user.first_name,
        "email" : techprofile.email,
        "college" : techprofile.college.collegeName,
        "technexId" : techprofile.technexId,
        "year" : techprofile.year,
        "mobileNumber" : techprofile.mobileNumber,
        "city" : techprofile.city,
        "date" : techprofile.user.date_joined.strftime(timeFormat)
    }
    # print(dic)
    url = "https://script.google.com/a/technex.in/macros/s/AKfycbwIXDuKjAipVNAWj8cjVAQrurLg7nWLU1s7nDCZD41yhSucG4I/exec" #tech@technex.in
    #url='https://script.google.com/a/technex.in/macros/s/AKfycbykHL9khnVUO0cM_pQ8W7MJ-avy_K8Go8d0K21HRlLFsgR1CrI/exec' #events@technex.in
    requests.post(url,data=dic)

@csrf_exempt
def register(request):
    if request.user.is_authenticated():
        return redirect('/dashboard')
    if request.method == 'POST':
        data = request.POST
        email = data.get('email',None)
        # print 'code base 0111'
        email=email.lower()
        print email
        try:
            # print "code base 01"  
            techProfile = TechProfile.objects.get(email__iexact = email)
            user = User.objects.get(email = email)
            return HttpResponse("Email Already Registered!")
        except:
            bugUsername = User.objects.latest('id').id
            user = User.objects.create_user(username=str(bugUsername+15), email=email)
            techprofile = TechProfile(user = user,email = email)

        user.first_name = data.get('name',None)
        password = data.get('password',None)
        user.set_password(password)
        user.save()
        print 'code base 1'
        try:
            college = College.objects.filter(collegeName = str(data.get('college')).strip())[0]
        except:
            college = College(collegeName = str(data.get('college')).strip())
            college.save()
        techprofile.technexId = "TX"+str(10000+user.id)
        techprofile.college = college
        techprofile.mobileNumber = data.get('mobileNumber')
        techprofile.city = data.get('city')
        techprofile.year = data.get('year')
        pins = TechProfile.objects.all().values_list("pin")
        while True:
            stringR = get_random_string(3,allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
            if stringR not in pins:
                techprofile.pin = stringR
                techprofile.save()
                break
        if 'referral' in data:
            techprofile.referral = data['referral']
            print 'code base 1.5'
        print data.get('uid')
        try:
            fb_connect = FbConnect.objects.get(uid = data.get('uid'))
            techprofile.fb = fb_connect
            print data.get('uid')
            print 'code base1'
            techprofile.save()
        except:
            techprofile.save()
        print "codeBaes 2"
        techprofile =TechProfile.objects.get(email=email)
        spreadsheetfill_register(techprofile)
        print "codeBase 3"
        subject = "[Technex'18] Confirmation of Registration"
        body = "Dear "+ user.first_name +''',

You have successfully registered for Technex 2018 with Technex Id %s . Team Technex welcomes you aboard!

An important note to ensure that the team can contact you further:  If you find this email in Spam folder, please right click on the email and click on 'NOT SPAM'.

       Our team will be at the task of updating you from time to time, the  information regarding the festival. Please keep visiting the website and the facebook page of Technex '18 to stay up-to-date with the latest happenings at Technex '18.


Note : As this is an automatically generated email, please don't  reply to this mail. Please feel free to contact us either through mail or by phone incase of any further queries. The contact details are clearly mentioned on the website www.technex.in.


Looking forward to seeing you soon at Technex 2018.

All the best!


Regards

Team Technex.'''%(techprofile.technexId)
        send_email(email,subject,body)
        print "codeBaes 4"

        message="Registration successful. Your registration ID is "+ str(techprofile.technexId) + " . Visit www.fb.com/technex for updates. \nRegards\nTeam Technex"
        # send_sms_single(message,str(techprofile.mobileNumber))
        #newUser = authenticate(username=email, password=password)
        #print 'code base 3'
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        print "codeBaes 5"
        login(request, user)
        return HttpResponse('1')
    else:
        context= {}
        context['all_colleges'] = College.objects.filter(status = True).values_list('collegeName',flat=True).distinct()
        try:
            get = request.GET
            context['name'] = get['name']
            context['uid'] = get['uid']
            if 'email' in get:
                context['email'] = get['email']

            context['status'] = 1;
            if(get_flavour(request)=='full'):
                return render(request,'index_login.html',context)
            else:    
                return render(request,'index_login_mobile.html',context)
        except:
            context['status'] = 0;
            if(get_flavour(request)=='full'):
                return render(request,'index_login.html',context)
            else:    
                return render(request,'index_login_mobile.html',context)



# def loginView(request):
#     response = {}
#     if request.user.is_authenticated():
#         response['status'] = 0
#         response['error'] = 'Already logged In'
#         return JsonResponse(response)
#     if request.method == 'POST':

#         post = request.POST
#         try:
#             try:
#                 techProfile = TechProfile.objects.get(email = post['email'])
#             except:
#                 techProfile = TechProfile.objects.get(technexId = post['email'])
#         except:
#             response['status'] = 0
#             response['error'] = "No User registered with the email!"
#             return JsonResponse(response)
#         #user = authenticate(username = post['email'], email= post['email'], password = post['password'])
#         kUser = techProfile.user
#         user = authenticate(username = kUser.username, password = post['password'])

#         if user is not None:
#             login(request, user)
#             response['status'] = 1
#             return JsonResponse(response)
#         else:
#             response['status'] = 0
#             response['error'] = "Invalid Credentials !"
#             return JsonResponse(response)
#     else:
#         response['status'] = 0
#         response['error'] = "Invalid Request!!"
#         return JsonResponse(response)

def loginView(request):
    # if(request.method=='GET'):
    #     print("bbo")

    response = {}
    
    if request.user.is_authenticated():
        response['status'] = 0
        response['error'] = 'Already logged In'
        return JsonResponse(response)
        print (request.method)
    if request.method == 'POST':

        post = request.POST
        print post['email']
        try:
            try:
                techProfile = TechProfile.objects.get(email = post['email'].lower())
            except:
                print post['email']
                techProfile = TechProfile.objects.get(technexId = post['email'])
        except:
            response['status'] = 0
            response['error'] = "No User registered with the email!"
            return JsonResponse(response)
        #user = authenticate(username = post['email'], email= post['email'], password = post['password'])
        kUser = techProfile.user
        user = authenticate(username = kUser.username, password = post['password'])

        if user is not None:
            login(request, user)
            response['status'] = 1
            return JsonResponse(response)
        else:
            response['status'] = 0
            response['error'] = "Invalid Credentials !"
            return JsonResponse(response)
    else:
        response['status'] = 0
        response['error'] = "Invalid Request!!"
        return JsonResponse(response)


@login_required(login_url='/register')
def dashboardView(request):
    context = contextCall(request)
    return render(request,'thankyou.html',context)

@csrf_exempt
@login_required(login_url='/register') #not /login/
def logoutView(request):
    logout(request)
    return redirect('/register')


def fbConnect(request):
    response = {}
    if request.method == 'POST':
        post = request.POST
        accessToken = post['accessToken']
        uid = post['uid']
        graph = facebook.GraphAPI(accessToken)
        args = {'fields':'name,email,picture'}
        profile = graph.get_object('me',**args)
        print profile
        try:
            fb_connect = FbConnect.objects.get(uid = uid)
            fb_connect.accessToken = accessToken
        except:
            fb_connect = FbConnect( accessToken = accessToken, uid = uid,profileImage = profile['picture']['data']['url'])
        fb_connect.save()
        try:
            techProfile = fb_connect.techprofile#TechProfile.objects.get(fb = fb_connect)
            user = techProfile.user #User.objects.get(username = profile['email'])
            #if  techProfile.fb is None:
            #   techProfile.fb = fb_connect
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request,user)
            response['status'] = 1 #status for logged IN
        except:
            context = {}
            if 'name' in profile:
                context['name'] = profile['name']
            if 'email' in profile:
                context['email'] = profile['email']
            context['uid'] =  uid
            print context
            response['context'] = context
            response['status'] = 0 #status signup prepopulation of data
        return JsonResponse(response)






'''

def get_fb_token(app_id, app_secret):
    try:
        webbrowser.open('https://graph.facebook.com/oauth/authorize?'+urllib.urlencode({'client_id':'461359507257085','redirect_uri':'http://localhost:8000/','scope':'publish_actions'}))
    except:
        pass
    #secret_code = raw_input("Secret Code: ")
    payload = {'grant_type': 'client_credentials', 'scope':'user_likes,publish_actions', 'client_id': app_id, 'client_secret': app_secret,'redirect_uri':'http://localhost:8000/'}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)

    print file.text #to test what the FB api responded with
    #result = file.text.split("=")[1]
    #print file.text #to test the TOKEN
    return file.text

def demofb_id(request):
    print str(request)
    app_id = '461359507257085'
    app_secret = '7be92fe7ee2c2d12cd2351d2a2c0dbb8'
    token = get_fb_token(app_id, app_secret)
    response = {}
    response['data'] = token
    #facebook.auth_url(app_id,'http://locahost:8000/ca/demofb_id',)
    return JsonResponse(response)
'''

@csrf_exempt
def resetPass(request,key):
    if request.method == 'GET':

        try:
            forgotPass = ForgotPass.objects.get(key = int(key))

            return render(request,"reset.html")
        except:
            messages.warning(request,'Invalid Url !')
            return redirect('/register')

    elif request.method == "POST":
        post = request.POST
        try:
            forgotPass = ForgotPass.objects.get(key=key)
            user = forgotPass.user
            password1 = post.get('form-password')
            password2 = post.get('form-repeat-password')
            if password1 == password2:
                forgotPass.delete()
                user.set_password(password1)
                user.save()
                messages.success(request,'password set successfully!',fail_silently=True)
                return redirect('/register')
            else:
                messages.warning(request,"passwords didn't match!")
                url = server+"/resetPass/"+key
                return redirect(request,url)
        except:
            raise Http404('Not allowed')


        return redirect('/resetPass/'+key)


@csrf_exempt
def eventApi(request):
    response = {}
    try:
        parentEvents = ParentEvent.objects.all()
        response['data'] = []
        for parentEvent in parentEvents:
            pEventData = {}
            pEventData['name'] = parentEvent.categoryName
            pEventData['description'] = parentEvent.description
            pEventData['order'] = parentEvent.order
            pEventData['events'] = []
            events = Event.objects.filter(parentEvent = parentEvent)
            for event in events:
                eventData = {}
                eventData['eventName'] = event.eventName
                eventData['description'] = event.description
                eventData['deadLine'] = event.deadLine
                eventData['prizeMoney'] = event.prizeMoney
                eventData['maxMembers'] = event.maxMembers
                eventData['eventOrder'] = event.eventOrder
                eventData['eventOptions'] = []
                eventOptions = EventOption.objects.filter(event = event)
                for eventOption in eventOptions:
                    eventOptionData = {}
                    eventOptionData['optionName'] = eventOption.optionName
                    eventOptionData['optionDescription'] = eventOption.optionDescription
                    eventOptionData['eventOptionOrder'] = eventOption.eventOptionOrder
                    eventData['eventOptions'].append(eventOptionData)
                pEventData['events'].append(eventData)
            response['data'].append(pEventData)
            response['status'] = 1
        return JsonResponse(response)
    except:
        response['error'] = True
        response['status'] = 'Error in finding events'
        return JsonResponse(response)

@csrf_exempt
def events(request):
    response = {}
    if request.method == 'GET':
        response['status'] = 1
        # response['type'] = 0
        data = []
        parentEvents = ParentEvent.objects.all()
        for parentEvent in parentEvents:
            dataObject = {}
            dataObject['parentEventId'] = parentEvent.nameSlug
            dataObject['events'] = []
            dataObject['parentEventName'] = parentEvent.categoryName
            events = Event.objects.filter(parentEvent = parentEvent)
            for event in events:
                eventData = {}
                eventData['event_name'] = event.eventName
                eventData['event_content'] = event.description
                if event.eventName == "Hackathon":
                    eventData['event_register'] = "Registrations are Closed"
                else:
                    eventData['event_register'] = "Register Team"

                if event.nameSlug=="krackat":
                    eventData['register_link'] = "http://krackat.technex.in/"
                elif event.nameSlug=="hackathon":
                    eventData['register_link'] = "#"
                else:
                    eventData['register_link'] = "/dashboard/#/eventreg/"+parentEvent.nameSlug+"/"+event.nameSlug+"/"


                # eventData['register_link'] = "/dashboard/#/eventreg/"+parentEvent.nameSlug+"/"+event.nameSlug+"/"
                # eventData['deadLine'] = event.deadLine
                eventData['prizeMoney'] = event.prizeMoney
                eventData['maxMembers'] = event.maxMembers
                eventData['eventOrder'] = event.eventOrder
                eventData['eventSlug']=event.nameSlug
                eventData['eventOptions'] = []
                eventData['eventId'] = event.nameSlug
                eventOptions = EventOption.objects.filter(event = event)
                for eventOption in eventOptions:
                    eventOptionData = {}
                    eventOptionData['optionName'] = eventOption.optionName
                    eventOptionData['optionDescription'] = eventOption.optionDescription
                    eventOptionData['eventOptionOrder'] = eventOption.eventOptionOrder
                    eventData['eventOptions'].append(eventOptionData)
                eventData['eventOptions'].sort(key=lambda x: x['eventOptionOrder'])
                dataObject['events'].append(eventData)
            data.append(dataObject)
            response['data'] = data 
            # print response   
    else:
        response['error'] = True
        response['status'] = 'Invalid Request'
        return JsonResponse(response)    
    if(get_flavour(request)=='full'):      
        return render(request,'eventnew.html',{'response':json.dumps(response),'eventdata':response})
    else:
        return render(request,'eventmobilenew.html',{'response':json.dumps(response),'eventdata':response})

def event2api(request):
    return JsonResponse(response)


# def event(request, key):
#     response = {}
#     if request.method == 'GET':


#         try:
#             parentEvent = ParentEvent.objects.get(nameSlug = key)
#             parentEventname = parentEvent.categoryName
#         except:
#             response['error'] = True
#             response['status'] = 'Invalid Slug for Parent Event'
#             return JsonResponse(response)
#         response['name'] = parentEvent.categoryName
#         response['description'] = parentEvent.description
#         response['order'] = parentEvent.order
#         response['slug'] = parentEvent.nameSlug
#         response['sponimage']=parentEvent.sponimage
#         response['assosponimage']=parentEvent.assosponimage
#         response['assosponlink']= parentEvent.assosponlink
#         response['sponlink']=parentEvent.sponlink
#         print parentEvent.sponimage
#         response['events'] = []
#         events = Event.objects.filter(parentEvent = parentEvent)
#         for event in events:
#             eventData = {}
#             eventData['eventName'] = event.eventName
#             eventData['description'] = event.description
#             # eventData['deadLine'] = event.deadLine
#             eventData['prizeMoney'] = event.prizeMoney
#             eventData['maxMembers'] = event.maxMembers
#             eventData['eventOrder'] = event.eventOrder
#             eventData['eventSlug']=event.nameSlug
#             eventData['eventOptions'] = []
#             eventOptions = EventOption.objects.filter(event = event)
#             for eventOption in eventOptions:
#                 eventOptionData = {}
#                 eventOptionData['optionName'] = eventOption.optionName
#                 eventOptionData['optionDescription'] = eventOption.optionDescription
#                 eventOptionData['eventOptionOrder'] = eventOption.eventOptionOrder
#                 eventData['eventOptions'].append(eventOptionData)
#             eventData['eventOptions'].sort(key=lambda x: x['eventOptionOrder'])
#             response['events'].append(eventData)
#         response['events'].sort(key= lambda x: x['eventOrder'])
#         metaTags = MetaTags.objects.filter(event = parentEvent)
#         #print json.dumps(response)
#         return render(request,'index3.html',{'parentEvent':json.dumps(response), 'metaTags': metaTags,'parentEventname':parentEventname})
#     else:
#         response['error'] = True
#         response['status'] = 'Invalid Request'
#         return JsonResponse(response)

def guestLecture(request):
    response = {}
    resp = {}
    try:
        lectures = GuestLecture.objects.all()
        response['lectures'] = []
        for lecture in lectures:
            lectureData = {}
            lectureData['title'] = lecture.title.encode('ascii','ignore')
            lectureData['description'] = lecture.description.encode('ascii','ignore')
            lectureData['lecturerName'] = lecture.lecturerName.encode('ascii','ignore')
            lectureData['lecturerBio'] = lecture.lecturerBio.encode('ascii','ignore')
            lectureData['designation'] = lecture.designation.encode('ascii','ignore')
            lectureData['lectureType'] = lecture.lectureType.encode('ascii','ignore')
            lectureData['photo'] = lecture.photo.encode('ascii','ignore')
            response['lectures'].append(lectureData)
        # print response
    except:
        response['status'] = 0
    if(get_flavour(request)=='full'):
        return render(request, 'guestlecturenew.html', {'lectures':response})
    else:
        return render(request, 'guestmobilenew.html', {'lectures':response})

def error404(request):
    return render(request, '404.html')

def error500(request):
    return render(request, '500.html')

def send_email(recipient, subject, body):

    return requests.post(
        "https://api.mailgun.net/v3/mgun.technex.in/messages",
        auth=("api", "key-716da2426e77cc5296dacd1e4768672d"),
        data={"from": "Technex<tech@technex.in>",
              "to": recipient,
              "subject": subject,
              "text": body})

@csrf_exempt
@user_passes_test(lambda u: u.is_staff)
def send_publicity_mail(request):
    response = {}
    if request.method == 'POST':
        post = request.POST
        recipient = post['recipient']
        subject = post['subject']
        body = post['body']

        response['status'] = str(requests.post(
        "https://api.mailgun.net/v3/mgun.technex.in/messages",
        auth=("api", "key-716da2426e77cc5296dacd1e4768672d"),
        data={"from": "Technex<events@technex.in>",
              "to": recipient,
              "subject": subject,
              "text": body}))

        return JsonResponse(response)
    else:
        return render(request,"publicitymail.html")



def send_email2(r,s,b):
    return requests.post("https://api.mailgun.net/v3/mg32.technex.in/messages",auth=("api", "key-817973280a90a2a4c81a917cfe9a8503"),data={"from":"Technex 2018 IIT(BHU) Varanasi India <technex@iitbhu.ac.in>","to":r,"subject":s,"text":b})

@csrf_exempt
def botApi(request):
    response = {}
    post = request.POST
    if post['passkey'] == 'Xs6vvZdLhsYHAEK':
        try:
            techProfile = TechProfile.objects.get(id = post['email'])
            response['status'] = 1
        except:
            response['status'] = 0
        techProfile.botInfo = post['uid']
        techProfile.save()

        return JsonResponse(response)
    return HttpResponse("Invalid Request!")

@csrf_exempt
def forgotPassword(request):
    response = {}
    if request.method == 'POST':
        email = request.POST.get("email")

        try:
            user = TechProfile.objects.get(email = email).user
        except:
            response['status'] = 0
            response['error'] = 'Email not Registered!!'
            return JsonResponse(response)
        subject = "Reset Password"
        forgotPassKey = 'Technex' + email + "caportal"
        forgotPassKey = str(hash(forgotPassKey))

        try:
            key = ForgotPass.objects.get(user = user)
            key.key = forgotPassKey
            key.save()
        except:
            key = ForgotPass(user = user,key = forgotPassKey)
            key.save()

        body = "Please Cick on the following link to reset your Technex Acount Password.\n\n"
        body += server + "resetPass/" + forgotPassKey

        if send_email(email, subject, body):
            response['status'] = 1
            return JsonResponse(response)
        else:
            response['status'] = 0
            response['error'] = 'Connection Problem..Please Try Again'
            return JsonResponse(response)
    else:
        return render(request,'login.html')
        response['status'] = 0
        response['error'] = 'Invalid Request'
        return JsonResponse(response)


'''
@csrf_exempt
def resetPass(request,forgotPassKey):
    if request.method == 'GET':
        try:
            key = Key.objects.get(forgotPassKey = int(forgotPassKey))
            return render(request,"ca/reset.html")
        except:
            messages.warning(request,'Invalid Url !')
            return redirect('/login')

    elif request.method == "POST":
        post = request.POST
        try:
            key = Key.objects.get(forgotPassKey=forgotPassKey)
            caprofile = key.ca
            password1 = post.get('form-password')
            password2 = post.get('form-repeat-password')
            if password1 == password2:
                caprofile.user.set_password(password1)
                caprofile.user.save()
                messages.success(request,'password set successfully!',fail_silently=True)
                return redirect('/login')
            else:
                messages.warning(request,"passwords didn't match!")
                url = server + "/resetPass/" + key
                return redirect(request, url)
        except:
            raise Http404('Not allowed')
'''

def cdncheck(request):
    return render(request, 'cdn_check.html', {})

def startupFair(request):
    print "coodod"
    if(get_flavour(request)=='full'):
        return render(request, 'startupnew.html', {})
    else:
        return render(request, 'startupmobilenew.html', {})        
def hospitality(request):
    return render(request, 'hospitality.html', {})
def airshow(request):
    if(get_flavour(request)=='full'):
        return render(request, 'airshownew.html',{})
    else:
        return render(request, 'airshowmobilenew.html',{})
    

@csrf_exempt
def read(request):
    response = {}
    if request.method == 'POST':
        post = request.POST
        try:
            readerStatus = ReaderStatus.objects.get(reader = request.user.techprofile, notification__notificationId = post['notificationId'])
        except:
            notificationR = Notification.objects.get(notificationId = post['notificationId'])
            readerStatus = ReaderStatus(reader = request.user.techprofile, notification = notificationR)
            readerStatus.save()
        response['status'] = 1

        response['unread'] = Notification.objects.all().count() - ReaderStatus.objects.filter(reader = request.user.techprofile).count()
        return JsonResponse(response)
    else:
        response['status'] = 0
        return JsonResponse(response)

@csrf_exempt
def notificationData(request):
    notifications = Notification.objects.all()
    notificationWrapper = {}
    notificationArray = []
    count = 0
    for notification in notifications:
        notificationObject = {}

        notificationObject['title'] = notification.title
        notificationObject['notificationId'] = notification.notificationId
        notificationObject['description'] = notification.description
        notificationObject['time'] = notification.time
        notificationObject['photo'] = notification.photo
        try:

            ReaderStatus.objects.get(notification = notification,reader = request.user.techprofile)
            status = 1
        except:
            count = count + 1
            status = 0

        notificationObject['status'] = status
        notificationArray.append(notificationObject)
    notificationWrapper['unread'] = count
    notificationWrapper['notifications'] = notificationArray
    return notificationWrapper


@csrf_exempt
@login_required(login_url='/register')
def startUpRegistration(request):
    response = {}
    print request
    if request.method == 'POST':
        post = json.loads(request.body)
        print post
        try:
            StartUpFair.objects.get(teamLeader = request.user.techprofile)
            response['status'] = 0
            response['error'] = 'Already registered !!'
            return JsonResponse(response)
        except:
            startUpFair = StartUpFair(startuptype= post['startuptype'],description= post['description'],year=post['year'],teamLeader = request.user.techprofile, teamName = post['teamName'],linkUrl = post['link'],funding = post['funding'])
            startUpFair.save()
            memberEmails = ""
            # pindustry = []
            btypes = []
            # print post['pindustry']
            # for industry in post['pindustry']:
            #     try:
            #         pind = PrimaryIndustry.objects.get(name = industry)
            #         pindustry.append(pind)
            #     except:
            #         response['status'] = 0
            #         response['error'] = 'Some Error Occured'

            for btype in post['btype']:
                bty = BusinessType.objects.get(name = btype)
                btypes.append(bty)
            for email in post['memberMails']:
                if checkunique(email):
                    s=StartUpMails(email=email,team=startUpFair,)
                    memberEmails += email+'  '
                    s.save()
            # pindustry = list(set(pindustry))
            btypes = list(set(btypes))
            # for pind in pindustry:
            #     startUpFair.pindusry.add(pind)
            for bty in btypes:
                startUpFair.bType.add(bty)
            sf=StartUpFair.objects.get(teamLeader=request.user.techprofile)
            subject = "[Technex'18] Successful Registration"
            body = '''
Dear %s,

Thanks for registering for %s Technex'18.

Your Team Details Are
Team Name- %s
Team Leader- %s
Team Members- %s


An important note to ensure that the team can contact you further:  If you find this email in Spam folder, please right click on the email and click on 'NOT SPAM'.


Note : As this is an automatically generated email, please don't  reply to this mail. Please feel free to contact us either through mail or by phone incase of any further queries. The contact details are clearly mentioned on the website www.technex.in/startupfair.


Looking forward to seeing you soon at Technex 2018.

All the best!


Regards

Team Technex
Regards
            '''
            send_email(sf.teamLeader.email,subject,body%(sf.teamLeader.user.first_name,"Startup Fair".capitalize(),sf.teamName,sf.teamLeader.email,memberEmails))
            response['status'] = 1
            techprofile = request.user.techprofile
            # message = "Registration successful for StartupFair.\n TeamName:"+str(post['teamName'])+"\nVisit www.fb.com/technex for regular updates!  All the best, Team Technex"
            # send_sms_single(message,str(techprofile.mobileNumber))
            
            startupfair_spreadsheet(sf)
           
            return JsonResponse(response)
    else:
        response['status'] = 0
        response['error'] = 'Invalid Request!!'
        return JsonResponse(response)


#@login_required(login_url = '/register')
def startUpData(request):
    response = {}
    try:
        startUp = StartUpFair.objects.get(teamLeader = request.user.techprofile)
    except:
        response['status'] = 0
        response['error'] = 'Not registered for Start Up Fair !'
    response['teamName'] = startUp.teamName
    memberMails = StartUpMails.objects.filter(team = startUp)
    response['memberMails'] = []
    for memberMail in memberMails:
        response['memberMails'].append(memberMail)
    response['status'] = 1
    return JsonResponse(response)


@login_required(login_url = '/register')
def startUpDelete(request):
    response = {}
    try:
        startUp = StartUpFair.objects.get(teamLeader = request.user.techprofile)
    except:
        response['status'] = 0
        response['error'] = 'Not registered for Start Up Fair !'
    startUp.delete()
    response['status'] = 1
    return JsonResponse(response)

@csrf_exempt
@login_required(login_url = '/register')
def changePass(request):
    response = {}
    print request
    if request.method == 'POST':
        post = json.loads(request.body)
        user = authenticate(username=request.user.username,password=post['oldPass'])
        if user is not None:
            request.user.set_password(post['newPass'])
            request.user.save()
            user = authenticate(username=request.user.username,password=post['newPass'])
            login(request,user)
            response['status'] = 1
            return JsonResponse(response)
        else:
            response['status'] = 0
            response['error'] = 'Password Entered is Incorrect !!'
            return JsonResponse(response)
    else:
        response['status'] = 0
        response['error'] = 'Invalid Request!!'
        return JsonResponse(response)

def checkunique(request):
    try:
        StartUpMails.objects.get(email = request)
        return False
    except:
        return True
@csrf_exempt
def innoviansRegister(request):    
    response = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        print data 
        techProfile = TechProfile.objects.get(email = data['email'])
        dic = {
        "name" : techProfile.user.first_name.encode("utf-8"),
        "email" : techProfile.email.encode("utf-8"),
        "mobileNumber" : str(techProfile.mobileNumber),
        "college" : techProfile.college.collegeName.encode("utf-8"),
        "technexId" : techProfile.technexId.encode("utf-8")
        }
        url = sheetUrls['innoviansfinal']
        print url
        print dic
        requests.post(url,data = dic)
        return JsonResponse(response)
        



@csrf_exempt
def workshopRegister(request):
    response = {}

    if request.method == 'POST':
        data = json.loads(request.body)
        print data
        workshop = Workshops.objects.get(slug = data['workshopSlug'])

        # try:
        #     # print "here"
        #     if data['teamName'] == '':
        #         raise Exception('This is the exception you expect to handle')
        #     else:
        #         team = WorkshopTeam.objects.get(teamName = data['teamName'], workshop = workshop)
        #         response['status'] = 0
        #         response['error'] = "TeamName Already exists"
        #         return JsonResponse(response)
        # except:
        try:
            teamLeader = TechProfile.objects.get(technexId = data['teamLeaderEmail'])
            print teamLeader.college.collegeWebsite
            print type(teamLeader.college.collegeWebsite)
            if teamLeader.college.collegeWebsite == "190":
                response['status'] = 0
                response['error'] = "Registration not Successfull!!"
                return JsonResponse(response)
        except:
            teamLeader = TechProfile.objects.get(email = data['teamLeaderEmail'])
            print teamLeader.college.collegeWebsite
            print type(teamLeader.college.collegeWebsite)
            if teamLeader.college.collegeWebsite == "190":
                response['status'] = 0
                response['error'] = "Registration not Successfull!!"
                return JsonResponse(response)
        users = []
        # print "here"
        for member in data['members']:
            try:
                try:
                    user = TechProfile.objects.get(email = member)
                    if user.college.collegeWebsite == "190":
                        response['status'] = 0
                        response['error'] = "Registration not Successfull!!"
                        return JsonResponse(response)
                    users.append(user)
                except:
                    user = TechProfile.objects.get(technexId = member)
                    if user.college.collegeWebsite == "190":
                        response['status'] = 0
                        response['error'] = "Registration not Successfull!!"
                        return JsonResponse(response)
                    users.append(user)
            except:
                response['status'] = 0
                response['error'] = 'Member not Registered('+str(member)+')'
                return JsonResponse(response)

        users = list(set(users))
        try:
            try:
                team = WorkshopTeam.objects.get(teamLeader = teamLeader,workshop = workshop)
                response['status'] = 0
                response['error'] = 'You have Already registered for this event!!'
                return JsonResponse(response)
            except:
                team = Team.objects.get(workshop = workshop, members = teamLeader)
                response['status'] = 0
                response['error'] = 'You have Already registered for this event !!'
        except:
            for u in users:
                try:
                    try:
                        team = WorkshopTeam.objects.get(workshop = workshop, members = u)
                        response['status'] = 0
                        response['error'] = u.email+' Already registered for this workshop !!!'
                        return JsonResponse(response)
                    except:
                        team = WorkshopTeam.objects.get(workshop = workshop, teamLeader = u)
                        response['status'] = 0
                        response['error'] = u.email+' Already registered for this workshop !!!'
                        return JsonResponse(response)
                except:
                    try:
                        if teamLeader == u:
                            users.remove(u)
                    except:
                        pass
            team = WorkshopTeam(teamLeader = teamLeader,workshop = workshop, teamName = data['teamName'])
            team.save()
        subject = "[Technex'18] Successful Registration"
        body = '''
Dear %s,

Thanks for registering for %s Technex'18.

An important note to ensure that the team can contact you further:  If you find this email in Spam folder, please right click on the email and click on 'NOT SPAM'.


Note : As this is an automatically generated email, please don't  reply to this mail. Please feel free to contact us either through mail or by phone incase of any further queries. The contact details are clearly mentioned on the website www.technex.in.


Looking forward to seeing you soon at Technex 2018.

All the best!


Regards

Team Technex
Regards
        '''
        # memberEmails = ""
        # for user in users:
        #     memberEmails += user.email+'  '
        #     team.members.add(user)
        # send_email(teamLeader.email,subject,body%(teamLeader.user.first_name,workshop.title.capitalize(),team.teamName,teamLeader.email,memberEmails))
        send_email(teamLeader.email,subject,body%(teamLeader.user.first_name,workshop.title.capitalize()))
        # for user in users:
        #    send_email(user.email,subject,body%(user.user.first_name,workshop.title.capitalize(),team.teamName,teamLeader.email,memberEmails))
        response['status'] = 1
    
        workshop_spreadsheet(team)
        return JsonResponse(response)
    else:
        response['status'] = 0
        return render(request, 'eventRegistration.html',contextCall(request))
        #return JsonResponse(response)

def botTest(request):
    email = request.user.techprofile.id
    return render(request,'thankyou.html',{'id':email})

def gverify(request):
    return render(request,'googlec0c9e6f96a842b6d.html',{})

# def workshop(request):
#     response={}
#     # print "HH"
#     try:
#         workshops=Workshops.objects.all()
#         # # print workshops
#         response['workshops']=[]
#         for workshop in workshops:
#             workshopData={}
#             workshopData['title']=workshop.title.encode('ascii','ignore')
#             workshopData['description']=workshop.description.encode('ascii','ignore')
#             workshopData['workshopfees']=workshop.workshopFees
#             workshopData['maxMembers']=workshop.maxMembers
#             workshopData['image']=workshop.image.encode('ascii','ignore')
#             workshopData['order']=workshop.order
#             response['workshops'].append(workshopData)
#             # print workshop.title
#             # print "HH"
#     except:
#         response['status']=0
#     print response
#     if(get_flavour(request) == 'full'):
#         return render(request,"workshopnew.html",{'workshops':response})
#     else:
#         return render(request,"workshopmobilenew.html",{'workshops':response}) 

@csrf_exempt
def workshop(request):
    response = {}
    if True:#try:
        workshops = Workshops.objects.all()
        response = {}
        response['status'] = 1
        response['type'] = 0
        # response['data'] = []
        # data = []
        response['parentEventId'] = "workshops"
        response['events'] = []
        response['parentEventName'] = "Workshops"
        WorkshopData = []
        for workshop in workshops:
            workshopData = {}
            workshopData['event_name'] = workshop.title
            workshopData['image'] = workshop.image
            workshopData['event_content'] = workshop.description
            workshopData['event_register'] = "Register"
            workshopData['register_link'] = "#"
            workshopData['workshopFees'] = workshop.workshopFees
            workshopData['eventOrder'] = workshop.order
            # workshopData['']
            workshopData['eventSlug'] = workshop.slug
            workshopData['eventId'] = workshop.slug
            workshopData['sponlink'] = workshop.sponlink
            workshopData['sponimage'] = workshop.sponimage
            # workshopData['workshopId'] = workshop.slug
            workshopData['eventOptions'] = []
            workshopOptions = WorkshopOptions.objects.filter(workshop = workshop)
            for workshopOption in workshopOptions:
                workshopOptionData = {}
                workshopOptionData['optionName'] = workshopOption.optionName
                workshopOptionData['optionDescription'] = workshopOption.optionDescription
                workshopOptionData['eventOptionOrder'] = workshopOption.optionOrder
                workshopData['eventOptions'].append(workshopOptionData)
            workshopData['eventOptions'].sort(key=lambda x: x['eventOptionOrder'])
            response['events'].append(workshopData)
        # data.append(dataObject)
        # WorkshopData.sort(key=lambda x: x['order'])
        # data.append(WorkshopData)
        # response['data'] = dataObject
    else:#except:
        response['status'] = 0
    print json.dumps(response)    
    if(get_flavour(request) == 'full'):
        return render(request,"workshopnew.html",response)
    else:
       return render(request,"workshopmobilenew.html",response)



# @csrf_exempt
# def workshop(request):
#     response = {}
#     if True:#try:
#         workshops = Workshops.objects.all()
#         response['status'] = 1
#         response['type'] = 0
#         # response['data'] = []
#         data = []
#         dataObject = {}
#         dataObject['parentEventId'] = "workshops"
#         dataObject['events'] = []
#         dataObject['parentEventName'] = "Workshops"
#         WorkshopData = []
#         for workshop in workshops:
#             workshopData = {}
#             workshopData['event_name'] = workshop.title
#             workshopData['image'] = workshop.image
#             workshopData['event_content'] = workshop.description
#             workshopData['event_register'] = "Register"
#             workshopData['register_link'] = "#"
#             workshopData['workshopFees'] = workshop.workshopFees
#             workshopData['eventOrder'] = workshop.order
#             # workshopData['']
#             workshopData['eventSlug'] = workshop.slug
#             workshopData['eventId'] = workshop.slug
#             workshopData['sponlink'] = workshop.sponlink
#             workshopData['sponimage'] = workshop.sponimage
#             # workshopData['workshopId'] = workshop.slug
#             workshopData['eventOptions'] = []
#             workshopOptions = WorkshopOptions.objects.filter(workshop = workshop)
#             for workshopOption in workshopOptions:
#                 workshopOptionData = {}
#                 workshopOptionData['optionName'] = workshopOption.optionName
#                 workshopOptionData['optionDescription'] = workshopOption.optionDescription
#                 workshopOptionData['eventOptionOrder'] = workshopOption.optionOrder
#                 workshopData['eventOptions'].append(workshopOptionData)
#             workshopData['eventOptions'].sort(key=lambda x: x['eventOptionOrder'])
#             dataObject['events'].append(workshopData)
#         data.append(dataObject)
#         # WorkshopData.sort(key=lambda x: x['order'])
#         # data.append(WorkshopData)
#         response['data'] = data
#     else:#except:
#         response['status'] = 0
#     print json.dumps(response)    
#     return render(request,'workshopnew.html',{"eventdata":response,"response":json.dumps(response)})

    # 

'''
@csrf_exempt
def workshop(request):
    response = {}
    if True:#try:
        workshops = Workshops.objects.all()
        response['status'] = 1
        response['type'] = 0
        # response['data'] = []
        data = []
        dataObject = {}
        dataObject['parentEventId'] = "workshops"
        dataObject['events'] = []
        dataObject['parentEventName'] = "Workshops"
        WorkshopData = []
        for workshop in workshops:
            workshopData = {}
            workshopData['event_name'] = workshop.title
            workshopData['image'] = workshop.image
            workshopData['event_content'] = workshop.description
            workshopData['event_register'] = "Register"
            workshopData['register_link'] = "#"
            workshopData['workshopFees'] = workshop.workshopFees
            workshopData['eventOrder'] = workshop.order
            # workshopData['']
            workshopData['eventSlug'] = workshop.slug
            workshopData['eventId'] = workshop.slug
            workshopData['sponlink'] = workshop.sponlink
            workshopData['sponimage'] = workshop.sponimage
            # workshopData['workshopId'] = workshop.slug
            workshopData['eventOptions'] = []
            workshopOptions = WorkshopOptions.objects.filter(workshop = workshop)
            for workshopOption in workshopOptions:
                workshopOptionData = {}
                workshopOptionData['optionName'] = workshopOption.optionName
                workshopOptionData['optionDescription'] = workshopOption.optionDescription
                workshopOptionData['eventOptionOrder'] = workshopOption.optionOrder
                workshopData['eventOptions'].append(workshopOptionData)
            workshopData['eventOptions'].sort(key=lambda x: x['eventOptionOrder'])
            dataObject['events'].append(workshopData)
        data.append(dataObject)
        # WorkshopData.sort(key=lambda x: x['order'])
        # data.append(WorkshopData)
        response['data'] = data
    else:#except:
        response['status'] = 0
    print json.dumps(response)    
    return render(request,'workshopnew.html',{"eventdata":response,"response":json.dumps(response)})

''
def event(request, key):
    response = {}
    if request.method == 'GET':
        events = Event.objects.filter(parentEvent = parentEvent)
        for event in events:
            eventData = {}
            eventData['eventName'] = event.eventName
            eventData['description'] = event.description
            # eventData['deadLine'] = event.deadLine
            eventData['prizeMoney'] = event.prizeMoney
            eventData['maxMembers'] = event.maxMembers
            eventData['eventOrder'] = event.eventOrder
            eventData['eventSlug']=event.nameSlug
            eventData['eventOptions'] = []
            eventOptions = EventOption.objects.filter(event = event)
            for eventOption in eventOptions:
                eventOptionData = {}
                eventOptionData['optionName'] = eventOption.optionName
                eventOptionData['optionDescription'] = eventOption.optionDescription
                eventOptionData['eventOptionOrder'] = eventOption.eventOptionOrder
                eventData['eventOptions'].append(eventOptionData)
            eventData['eventOptions'].sort(key=lambda x: x['eventOptionOrder'])
            response['events'].append(eventData)
        response['events'].sort(key= lambda x: x['eventOrder'])
        metaTags = MetaTags.objects.filter(event = parentEvent)
        #print json.dumps(response)
        return render(request,'index3.html',{'parentEvent':json.dumps(response), 'metaTags': metaTags,'parentEventname':parentEventname})
    else:
        response['error'] = True
        response['status'] = 'Invalid Request'
        return JsonResponse(response)
'''
@user_passes_test(lambda u: u.is_staff)
def registrationData(request):
    eventcount = {}
    # eventcount['eventdata'] = []
    workshopcount = {}
    workshopcount['workshopdata'] = []
    iitBHUs = College.objects.filter(collegeWebsite = "190")
    totalRegistrations = TechProfile.objects.all().count()
    localRegistrations = 0
    localTeams = 0
    for iitBHU in iitBHUs:
        localRegistrations += TechProfile.objects.filter(college = iitBHU).count()
        localTeams += Team.objects.filter(teamLeader__college = iitBHU).count()
    totalTeams = Team.objects.all().count()
    workshopTeamsTotal = WorkshopTeam.objects.filter(~Q(teamLeader__college__collegeWebsite = "190")).count()
    pevents = ParentEvent.objects.all()
    eventtypeArray = []
    for pevent in pevents:
        eventtypeobj = {}
        events = Event.objects.filter(parentEvent = pevent)
        eventArray = []
        for event in events:
            eventobj = {}
            eventobj['event'] = event.eventName
            counts = Team.objects.filter(event = event)
            countmen = counts.filter(~Q(teamLeader__college__collegeWebsite = "190"))
            f = 0
            for coun in countmen:
                 f = f + 1 + coun.members.count()
            eventobj['count'] = Team.objects.filter(event = event).count()
            eventobj['participantCount'] = f
            eventobj['localcount'] = 0
            for iitBHU in iitBHUs:
                eventobj['localcount'] += Team.objects.filter(teamLeader__college = iitBHU , event = event).count()
            eventArray.append(eventobj)
        eventtypeobj['parentEvent'] = pevent.categoryName
        eventtypeobj['events'] = eventArray
        eventtypeArray.append(eventtypeobj)
    eventcount['data'] =  eventtypeArray

    print eventcount

    # pevents = ParentEvent.objects.all()

    workshops = Workshops.objects.all()
    # print events
    # for event in events:
    #     eventcountobj = {}
    #     eventcountobj['event'] = event.eventName
    #     eventcountobj['count'] = Team.objects.filter(event = event).count()
    #     eventcountobj['localcount'] = Team.objects.filter(teamLeader__college = iitBHU , event = event).count()
    #     eventcount['eventdata'].append(eventcountobj)
    #     print eventcount
    for workshop in workshops:
        workshopcountobj = {}
        workshopcountobj['workshop'] = workshop.title

        workshopteams = WorkshopTeam.objects.filter(workshop = workshop)
        workshopteams = workshopteams.filter(~Q(teamLeader__college__collegeWebsite = "190"))
        number = 0
        for workshopteam in workshopteams:
            number += workshopteam.members.count() + 1
        workshopcountobj['count'] = workshopteams.count()
        if workshopcountobj['count'] is 0:


            number = 0
        workshopcountobj['participantcount'] = number
        workshopcount['workshopdata'].append(workshopcountobj)
        print workshopcount
    return render(request,'data.html',{'externalTeams':totalTeams-localTeams,'externalParticipation':totalRegistrations-localRegistrations,'totalTeams':totalTeams,'totalRegistrations':totalRegistrations,'localRegistrations':localRegistrations,'localTeams':localTeams,'workshopTeamsTotal':workshopTeamsTotal,'eventcount': eventcount, 'workshopcount':workshopcount})

@user_passes_test(lambda u: u.is_staff)
def collegewise(request):
    colleges = College.objects.all().order_by('collegeName')
    if request.method == 'POST':
        college = College.objects.filter(collegeName = request.POST['college'])
        college = College.objects.filter(collegeWebsite = college[0].collegeWebsite).exclude(collegeWebsite = '0')
        if college.count() == 0:
            college = College.objects.filter(collegeName = request.POST['college'])
        collegeWale = []
        for col in college:
            collegeWale.extend(TechProfile.objects.filter(college = col))
        eventsData = []
        workshopsData = []
        collegeWaleCount = len(collegeWale)
        referral = []
        for collegeWala in collegeWale:
            teams = Team.objects.filter(Q(members = collegeWala) | Q(teamLeader = collegeWala)).distinct()
            workshopTeams = WorkshopTeam.objects.filter(Q(members = collegeWala) | Q(teamLeader = collegeWala)).distinct()
            referral.append(collegeWala.referral)
            events = []
            workshops = []
            for workshopteam in workshopTeams:
                workshops.append(workshopteam.workshop.title)
            workshopsData.append(workshops)
            for team in teams:
                events.append(team.event.eventName)
            eventsData.append(events)
            print eventsData
            print workshopsData
        referral = list(set(referral))
        try:
            referral.remove(None)
            referral.remove('')
        except:
            pass
        return render(request,'publicity.html',{'colleges':colleges,'collegeWaleCount':collegeWaleCount,'collegeWale':zip(collegeWale,eventsData,workshopsData),'referral':referral})
    else:
        return render(request,'publicity.html',{'colleges':colleges})

@csrf_exempt
def regtrack(request):
    print request.POST

    if request.POST['passkey']!="njoefvoafjoadfjodcjocsjo":
        print "error in passkey"
        return render(request, '404.html')
    response={}
    iitBHUs = College.objects.filter(Q(collegeName = 'IIT (BHU) Varanasi') | Q(collegeName = 'IITBHU') | Q(collegeName = 'IIT-BHU') | Q(collegeName = 'IIT BHU') | Q(collegeName = 'IIT Varanasi') | Q(collegeName = 'Indian Institute Of Technology BHU') | Q(collegeName = 'Indian Institute Of Technology Varanasi') | Q(collegeName = 'Indian Institute of Technology BHU Varanasi') | Q(collegeName = 'Indian Institute of Technology (BHU) Varanasi') | Q(collegeName = 'IIT(BHU)') | Q(collegeName = 'IIT Indian Institute of Technology BHU'))
    totalRegistrations = TechProfile.objects.all().count()
    localRegistrations = 0
    localTeams = 0
    for iitBHU in iitBHUs:
        localRegistrations += TechProfile.objects.filter(college = iitBHU).count()
        localTeams += Team.objects.filter(teamLeader__college = iitBHU).count()
    totalTeams = Team.objects.all().count()
    workshopTeamsTotal = WorkshopTeam.objects.all().count()
    response['totalTeams']=totalTeams
    response['totalRegistrations']=totalRegistrations
    response['localRegistrations']=localRegistrations
    response['localTeams']=localTeams
    response['workshopTeamsTotal']=workshopTeamsTotal
    return JsonResponse(response)



@csrf_exempt
def uploadtry(request):
    return render(request, 'uploadtry.html')

@csrf_exempt
@login_required(login_url='/register/')
def dropboxtest(request):
    post = request.POST
    username = ""
    response = {}
    eventa =  post['event'].split(':')[1]
    event = Event.objects.get(nameSlug = eventa)
    status = event.abstract
    # print (Event.objects.get(nameSlug = eventa))
    # event
    if status is 1:
        username = request.user.username
        tech = TechProfile.objects.get(user = username)
        print tech.user
        try:
            team = Team.objects.get(teamLeader = tech, event = event)
            print team.teamName
        except:
            try:
                team = Team.objects.get(members = tech, event = event)
                print team.teamName
            except:
                response['status'] = 0;
                response['error'] = "No such team exists"
                print response
                return
                # return render(request,'dash.html',{'response':response})
        if team.abstractstatus is 0:
            filename = "/"+str(post['event'].split(':')[1])+'/'+ str(team.technexTeamId) + '.png'
            code = 'Jfu-UCbHKFAAAAAAAAAADg2rnPqxU34KZq5hcmosIIxjsO8H4LNNjm4P6JJa16hF'
            access_token = 'Jfu-UCbHKFAAAAAAAAAADg2rnPqxU34KZq5hcmosIIxjsO8H4LNNjm4P6JJa16hF'
            client = dropbox.client.DropboxClient(access_token)
            resp = client.put_file(filename,request.FILES['abstract'])
            print resp
            response['status'] = 1
            response['error'] = "Abstract successfully submitted"
            team.abstractstatus = 1
            team.save()
        else:
            response['status'] = 0
            response['error'] = "Abstract already submitted"
    else:
        response['status'] = 0
        response['error'] = "Abstract submission not required for this event"
    print response
    # return render(request,'dash.html',{'response':response})

def fbReach(request):
    response = {}
    if request.method == 'POST':
        post = request.POST
        accessToken = post['accessToken']
        uid = post['uid']
        graph = facebook.GraphAPI(accessToken)
        args = {'fields':'name,email,picture'}
        profile = graph.get_object('me',**args)
        print profile
        print profile['name']
        try:
            fb_connect = FbReach.objects.get(uid = uid)
            fb_connect.accessToken = accessToken
            fb_connect.name = profile['name']
        except:
            fb_connect = FbReach( accessToken = accessToken, uid = uid,profileImage = profile['picture']['data']['url'])
        fb_connect.save()
        extendToken(uid)
        response['status'] = 1
        return JsonResponse(response)
    else:
        return render(request, 'fbReach.html')

def extendToken(uid):
    fb = FbReach.objects.get(uid = uid)
    app_id = '461359507257085'
    app_secret = '7be92fe7ee2c2d12cd2351d2a2c0dbb8'
    graph = facebook.GraphAPI(fb.accessToken)
    extendedToken = graph.extend_access_token(app_id,app_secret)

    fb.accessToken = extendedToken['access_token']
    fb.save()


def autoshare(token,message,link):
    message.replace(' ', '+')
    requests.post("https://graph.facebook.com/me/feed/?message=" + message + "&access_token=" + token + "&link=" + link)

def auto(message,link,last):
    message.replace(' ', '+')
    tokens = FbReach.objects.all()
    response = {}
    response["status"] = 1
    for token in tokens:
        if (int(token.uid) % 5 == int(last)) or (int(last) == 9) :
            try:
                requests.post("https://graph.facebook.com/me/feed/?message=" + message + "&access_token=" + token.accessToken + "&link=" + link)
            except:
                response["status"] = 0
    return response

@csrf_exempt
@user_passes_test(lambda u: u.is_staff)
def autoshare_call(request):
    response = {}
    if request.method == 'POST':
        post = request.POST
        print post
        try:
            response['res'] = auto(post['message'],post['link'],post['last'])
            response['status'] = 1
        except:
            response['status'] = 0
        return JsonResponse(response)
    else:
        return render(request, 'autoshare.html')

def auto_share_like(token,limit = 1,caption="",):
    try:
        graph = facebook.GraphAPI(access_token = token, version= '2.2')
        profile = graph.get_object(id ='225615937462895')
        posts = graph.get_connections(profile['id'],"posts",limit = limit)
        #userPosts = graph.get_object("me/feed")
        #print(userPosts['data'])
        '''
        links = []
        for userPost in userPosts['data']:
            links.append(userPost['link'])
        '''
        #postIds = []
        linksPosted = []
        for post in posts['data']:
            try:
                #graph.put_object(post['id'],"likes")
                #postIds.append(post['link'])
                attachment = {
                'link':post['link'],
                'name': '',
                'caption':'',
                'description':'',
                'picture':''
                }
                print post['link']
                #if post['link'] not in links:
                linksPosted.append(post['link'])
                graph.put_wall_post(message=caption,attachment = attachment)
                #graph.put_comment(post['id'],message="(Y)")
            except:
                continue
        return linksPosted
    except:
        return "gand PHat gayi"


def projectChutiyaKatta(limit = 1,caption=""):
    promoters = FbReach.objects.all()
    for promoter in promoters:
        print auto_share_like(promoter.accessToken,limit,caption)

@csrf_exempt
def paymentApi(request):
    post = request.POST#json.loads(request.body)#request.POST
    response = {}
    if 1:#try:


        try:
            consumer = TechProfile.objects.get(email =post['email'])
            payment = PaymentStatusa(tech = consumer, status = post['status'], ticketId = post['ticketId'],email = post['email'])


        except:
            payment = PaymentStatusa(email = post['email'], status = post['status'], ticketId = post['ticketId'])

        payment.contact = str(post.get("contact",""))
        payment.ticketPrice = str(post.get("ticketPrice",""))
        payment.timeStamp = str(post.get("timeStamp",""))
        payment.ticketName = str(post.get("ticketName",""))
        payment.save()
        response['status'] = 1
    else:#except:
        response['status'] = 0
    return JsonResponse(response)

def phoneNumberSepartion(request):
    number = request.GET['number']
    lengthNumber = len(str(number))
    print number
    numberS = str(number)
    h = []
    for i in range(0,lengthNumber-9,10):
        no = int(numberS[i:i+10])
        h.append(no)

    return HttpResponse(str(h))

def phoneSep(request):
    return render(request, 'numberS.html')


def eventRegistrationView(request):
    response = {}
    events = Events.objects.all();
    print events

#def exhibitions(request):
  #  return render(request,'exhibitions.html')

def liteversion(request):
    return redirect('/')

def workshop_spreadsheet(team):
    members = team.members.all()
    dic = {
    # "teamName": team.teamName.encode("utf-8"),
    "leaderName" : team.teamLeader.user.first_name.encode("utf-8"),
    "leaderEmail" : team.teamLeader.email.encode("utf-8"),
    "leaderMobile":str(team.teamLeader.mobileNumber),
    "leaderCollege":team.teamLeader.college.collegeName.encode("utf-8"),
    # "teamId":team.teamId
    }
    # try:
    #     dic['name1'] = members[0].user.first_name.encode("utf-8")
    #     dic['member1'] = members[0].email.encode("utf-8")
    #     dic['college1'] = members[0].college.collegeName.encode("utf-8")
    #     dic['mobile1'] = members[0].mobileNumber
    # except:
    #     dic['name1'] = 0
    #     dic['member1'] = 0
    #     dic['college1'] = 0
    #     dic['mobile1'] = 0
    # try:
    #     dic['name2'] = members[0].user.first_name.encode("utf-8")
    #     dic['member2'] = members[1].email.encode("utf-8")
    #     dic['college2'] = members[1].college.collegeName.encode("utf-8")
    #     dic['mobile2'] = members[1].mobileNumber
    # except:
    #     dic['name2'] = 0
    #     dic['member2'] = 0
    #     dic['college2'] = 0
    #     dic['mobile2'] = 0
    # try:
    #     dic['name3'] = members[0].user.first_name.encode("utf-8")
    #     dic['member3'] = members[2].email.encode("utf-8")
    #     dic['college3'] = members[2].college.collegeName.encode("utf-8")
    #     dic['mobile3'] = members[2].mobileNumber
    # except:
    #     dic['name3'] = 0
    #     dic['member3'] = 0
    #     dic['college3'] = 0
    #     dic['mobile3'] = 0
    # try:
    #     dic['name4'] = members[0].user.first_name.encode("utf-8")
    #     dic['member4'] = members[3].email.encode("utf-8")
    #     dic['college4'] = members[3].college.collegeName.encode("utf-8")
    #     dic['mobile4'] = members[3].mobileNumber
    # except:
    #     dic['name4'] = 0
    #     dic['member4'] = 0
    #     dic['college4'] = 0
    #     dic['mobile4'] = 0
    # print dic
    url = sheetUrls[team.workshop.slug.encode("utf-8")]
    requests.post(url, data = dic)


def workshopdataFill():
    teams = WorkshopTeam.objects.all()
    for team in teams:
        workshop_spreadsheet(team)


def corporateConclave(request):
    print request
    return render(request,'corporateConclave.html')

def kaleidoscope(request):
    return render(request,'kaleidoscope.html')


def test(request):
    response = {}
    try:
        user = request.user
        techprofile = user.techprofile
        response['name'] = techprofile.user.first_name
        response['email'] = techprofile.email
        response['phone'] = techprofile.mobileNumber
    except:
        response['name'] = ""
        response['email'] = ""
        response['phone'] = ""


    return render(request,'intellecx.html', {'response': response})



def send_sms(username,passwd,message,number):
    url = 'http://site24.way2sms.com/Login1.action?'
    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
    print url
    #For Cookies:
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    # Adding Header detail:
    opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]

    try:
        usock = opener.open(url, data)
    except IOError:
        return 0


    jession_id = str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]

    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
        return 0
    return 1

def send_sms_single(message,number):
    ups=Way2smsAccount_Premium.objects.all()
    for up in ups:
        if up.messages_left ==0:
            continue
        print up    
        send_sms(up.username,up.password,message,number)
        up.messages_left-=1
        up.save()
    return 1

# @user_passes_test(lambda u: u.has_perm('Auth.permission_code'))
@user_passes_test(lambda u: u.is_staff)
def sendSms(request):
    if request.method=="POST":
        messages_left=Way2smsAccount.objects.all().aggregate(Sum('messages_left'))['messages_left__sum']
        print messages_left
        if(messages_left==0):
            return render(request, 'send_sms.html',{'messages_left':messages_left,'error_msg':"Limit up man, bring some more accounts :D"})
        data = request.POST
        mobile_data = data.get('data',None)
        message=data.get('message',None)
        mobile_list=mobile_data.splitlines()
        print len(mobile_list)
        if len(mobile_list)>messages_left:
            return render(request, 'send_sms.html',{'messages_left':messages_left,'error_msg':"Sorry! I can send "+messages_left+" mesaages only!"})

        current_possible=0
        username=None
        password=None
        sent_numbers=[]
        count=0

        for m in mobile_list:
            number = m
            count+=1
            print m,count
            if current_possible==0:
                up_max=Way2smsAccount.objects.all().aggregate(Max('messages_left'))['messages_left__max']
                up=Way2smsAccount.objects.filter(messages_left=up_max)[0]
                current_possible=up_max
                username=up.username
                password=up.password
            sent=send_sms(username,password,message,number)
            # print number+username
            if sent:
                sent_numbers.append(number)
                current_possible-=1
                up.messages_left-=1
                up.save()
        messages_left=Way2smsAccount.objects.all().aggregate(Sum('messages_left'))['messages_left__sum']
        return render(request, 'send_sms_successful.html',{'messages_left':messages_left,'sent_numbers':sent_numbers,'count':len(sent_numbers)})
    else:
        messages_left=Way2smsAccount.objects.all().aggregate(Sum('messages_left'))['messages_left__sum']
        # print messages_left
        return render(request, 'send_sms.html',{'messages_left':messages_left})


def quizI(request):
    response = {}
    event = event.objects.get(eventName = 'Krackat')
    if user.is_authenticated:
        user = request.user
        try:
            team = Team.objects.filter(teamLeader = user, event = event)
            optionresp = optionResponse.objects.filter(team = team)
            if optionresp.attemptStatus is 1:
                response['status'] = 0
                response['message'] = "You have already finished you quiz"
                return render(request, 'dash.html' , response)
            else:
                quiz = optionresp.quiz
                if quiz.activeStatus is 0:
                    response['status'] = 0
                    response['message'] = "Your quiz has already ended"
                    return render(request , 'dash.html' , response)
                elif quiz.activeStatus is 2:
                    response['status'] = 0
                    response['message'] = "Your quiz has not yet started"
                else:
                    response['status'] = 1
                    questions = questions.objects.filter(quiz = quiz)
                    questionArrayObject = []
                    for question in questions:
                        questionArray = {}
                        questionArray['question'] = question.question
                        questionArray['option1'] = question.option1
                        questionArray['option1'] = question.option2
                        questionArray['option1'] = question.option3
                        questionArray['option1'] = question.option4
                        questionArrayObject.append(questionArray)
                    response['questions'] = questionArrayObject
                    finalResponse['data'] = response
                    return render(request , 'quiz.html', finalResponse)
        except:
            response['status'] = 0
            response['message'] = "You have not registered for this event"
            return render(request, 'dash.html', response)
    else:
        return redirect('/register')



def startupfair_spreadsheet(team):
    dic = {
    "startuptype" : team.startuptype.encode("utf-8"),
    "description" : team.description.encode("utf-8"),
    "year" : team.year,
    "linkUrl" : team.linkUrl,
    "funding" : team.funding,
    "leaderName" :  team.teamLeader.user.first_name.encode("utf-8"),
    "leaderEmail" : team.teamLeader.email.encode("utf-8"),
    "leaderMobile" : str(team.teamLeader.mobileNumber),
    "leaderCollege" : team.teamLeader.college.collegeName.encode("utf-8")
    }
    # primaryindustry = team.pindusry.all()
    businesstype = team.bType.all()
    # pindustry = ""
    btypes = ""
    # for p in primaryindustry:
    #     pindustry = pindustry + str(p.name) + ","
    for p in businesstype:
        btypes = btypes + str(p.name) + ","
    # dic['pindustry'] = pindustry
    dic['btypes'] = btypes
    if team.startuptype=="Ventura":
        url = sheetUrls["startup-fair-ventura"]
    else:
        url = sheetUrls["startup-fair-battle"]
    print dic
    requests.post(url,data=dic)


def startup_spreadsheet_delete(team):
    dic = {
    "leaderName" :  team.teamLeader.user.first_name.encode("utf-8"),
    "leaderEmail" : team.teamLeader.email.encode("utf-8"),
    "leaderMobile" : str(team.teamLeader.mobileNumber),
    "leaderCollege" : team.teamLeader.college.collegeName.encode("utf-8"),
    "startupDelete" : 1
    }
    if team.startuptype=="Ventura":
        url = sheetUrls["startup-fair-ventura"]
    else:
        url = sheetUrls["startup-fair-battle"]
    print dic
    requests.post(url,data=dic)


def startupdatafill():
    teams = StartUpFair.objects.all()
    for team in teams:
        startupfair_spreadsheet(team)



@csrf_exempt
def quizRegister2(request):
    response = {}
    if request.method == 'POST':
        data = request.POST#json.loads(request.body)
        users = []
        print data
        '''
        for user in data['members']:
            try:
                try:
                    member = TechProfile.objects.get(email = user)
                    users.append(member)
                except:
                    member = TechProfile.objects.get(technexId = user)
                    users.append(member)
            except:
                response['status'] = 0
                response['error'] = 'Member not Registered('+user+')'
                return JsonResponse(response)
        users = list(set(users))
        for u in users:
            try:
                quizteam = quizTeam.objects.get(members = u )
                response['status'] = 0
                response['error'] = u.email+' Already registered for this event !!!'
                return JsonResponse(response)
            except:
                pass
        '''


        try:
            quizteam = quizTeam2.objects.get(Q(member1Email = data['member1Email']) | Q(member2Email = data['member1Email']))
            messages.warning(request,"Member with this Email already Registered %s !"%(data['member1Email']))
            return render(request,"intellecx.html")
        except:
            try:
                quizteam = quizTeam2.objects.get(Q(member1Phone = data['member1Phone']) | Q(member2Phone = data['member1Phone']))
                messages.warning(request,"Member with this Phone Number already Registered %s !"%(data['member1Phone']))
                return render(request,"intellecx.html")
            except:
                Quiz = quiz.objects.get(quizId = data['quizId'])
                quizteam = quizTeam2(quiz = Quiz, member1Email = data['member1Email'], name1 = data['name1'], member1Phone = data['member1Phone'])
                try:
                    t = TechProfile.objects.get(email = data['member1Email'])
                    quizteam.status = True
                except:
                    quizteam.status = False
        try:
            quizteam = quizTeam2.objects.get(Q(member2Email = data['member2Email']) | Q(member2Email = data['member2Email']))
            messages.warning(request,"Member with this Email already Registered %s !"%(data['member2Email']))
            return render(request,"intellecx.html")
        except:
            try:
                quizteam = quizTeam2.objects.get(Q(member2Phone = data['member2Phone']) | Q(member1Phone = data['member2Phone']))
                messages.warning(request,"Member with this Phone Number already Registered %s !"%(data['member2Phone']))
                return render(request,"intellecx.html")
            except:
                quizteam.member2Email = data.get('member2Email')
                quizteam.member2Phone = data.get('member2Phone')
                quizteam.name2 = data.get('name2')
        quizteam.save()
        quizteam.quizTeamId = "INX" + str(1000+quizteam.teamId)

        subject = "INTELLECX | FINAL SLOT @10PM TODAY"
        body = '''
Hello,
Greetings from Team Technex,

The time has come to test your aptitude skills in one of the highly celebrated national level puzzle solving and logical reasoning contest. So, get ready to exercise all your wits as you battle it out to reach the top of the grid at INTELLECX.

%s

This is the link to the final slot of INTELLECX online round. Don't share the link. Visit this link at the slot timing to get redirected to the test page.
Timing of the final slot : Today, 10:00 - 10:40 pm.

Following are the general rules of the online round :
The online round consists of 10 logical reasoning questions
Duration of the test is 40 minutes.
There is NO provision for negative marking in the test.
Contact the coordinators for any further queries.
1. Kumar Anunay
    +91-9935009220
2. Kuljeet Keshav
    +91-8009596212

Regards,
Team Technex
            '''
        memberEmails = data.get('member2Email',None)
        key = str(hash("technex"+str(quizteam.teamId)+"livelong" + str(quizteam.member1Email)))
        quizteam.key = key
        quizteam.save()
        #for user in users:
            #memberEmails += user.email+'  '
            #quizteam.members.add(user)
        #for user in users:
        send_email(data['member1Email'],subject,body%("http://technex.in/playQuiz/"+str(quizteam.key)))

        quiz_spreadsheetfill(quizteam)
        return render(request,'intellecx.html',{"success":1})
    else:

        try:
            user = request.user
            techprofile = user.techprofile
            response['name'] = techprofile.user.first_name
            response['email'] = techprofile.email
            response['phone'] = techprofile.mobileNumber
        except:
            response['name'] = ""
            response['email'] = ""
            response['phone'] = ""
        return render(request,'intellecx.html',{'response':response})

def quiz_spreadsheetfill(team):
    # members = team.members.all()
    dic = {
    "quizTeamId" : team.quizTeamId

    }

    dic['member1Name'] = team.name1.encode("utf-8")
    dic['member1Email'] = team.member1Email.encode("utf-8")
    dic['member1Mobile'] = team.member1Phone
    try:
        dic['member2Name'] = team.name2.encode("utf-8")
        dic['member2Email'] = team.member2Email.encode("utf-8")
        dic['member2Mobile'] = team.member2Phone
    except:
        dic['member2Name'] = 0
        dic['member2Email'] = 0
        dic['member2Mobile'] = 0
    url = sheetUrls["quiz-registartion"]
    print dic
    requests.post(url,data=dic)

def collegesClassification():
    rb = open_workbook('technex-regisstration.xlsx')
    s = rb.sheet_by_index(0)
    # colleges = College.objects.all()
    # for college in colleges:
    #     print college.collegeName

    for i in range(1,3437):
        collegeName = literal_eval(str(s.cell(i,6)).split(':')[1])
        # print collegeName
        try:
            colleges = College.objects.filter(collegeName = collegeName)
            # print colleges
            for college in colleges:
                print college.collegeName
                college.collegeWebsite = int(str(str(s.cell(i,7)).split(':')[1]).split(".")[0])
                college.save()
                print i
        except:
            print collegeName
def collegesStateCity():
    rb = open_workbook('college-list.xlsx')
    s = rb.sheet_by_index(0)
    colleges = College.objects.all()
    for college in colleges:
        college.status = False

    for i in range(0,543):
        collegeid = str(int(str(str(s.cell(i,2)).split(':')[1]).split(".")[0]))
        # print collegeName
        try:
            colleges = College.objects.filter(collegeWebsite = collegeid)
            college = colleges[0]
            college.status = True
            college.collegeName = literal_eval(str(s.cell(i,1)).split(':')[1])
            college.save()
            # print colleges
            for college in colleges:
                print college.collegeName
                college.state = literal_eval(str(s.cell(i,5)).split(':')[1])
                college.city = literal_eval(str(s.cell(i,4)).split(':')[1])
                # college.collegeWebsite = int(str(str(s.cell(i,7)).split(':')[1]).split(".")[0])
                college.save()
                print i
        except:
            print collegeid

@user_passes_test(lambda u: u.is_staff)
def statewise(request):
    if request.method == 'POST':
        # print request.POST['state']
        response = {}
        colleges = College.objects.filter(state = request.POST['state']).order_by('city')
        citylist = []
        for college in colleges:
            citylist.append(college.city)
        citylist = list(set(citylist))
        citydataArray =  []
        statetotal = 0
        for city in citylist:
            citydata = {}
            citydata['city'] = city
            collegesincity = colleges.filter(city = city)
            users = 0
            citydata['colleges'] = []
            collegeCityArray = []
            for collegeincity in collegesincity:
                collegeCityArrayObject = {}
                collegeCityArrayObject['count'] = 0
                if collegeincity.status is True:
                    collegeswithId = colleges.filter(collegeWebsite = collegeincity.collegeWebsite)
                    for collegewithId in collegeswithId:
                        # collegeCityArrayObject['collegeName'] = collegeincity.collegeName
                        try:
                            collegeCityArrayObject['count'] += TechProfile.objects.filter(college = collegewithId).count()
                        except:
                            pass
                    collegeCityArrayObject['collegeName'] = collegeincity.collegeName
                    users += collegeCityArrayObject['count']
                    collegeCityArray.append(collegeCityArrayObject)

            citydata['count'] = users
            citydata['colleges'] = collegeCityArray
            citydataArray.append(citydata)
            statetotal += citydata['count']

        # for x in citydataArray:
        #     statetotal += citydata['count']
        response['state'] = request.POST['state']
        response['data'] = citydataArray
        response['statetotal'] = statetotal
        states = [
               "Andhra Pradesh",
               "Arunachal Pradesh",
               "Assam",
               "Bihar",
               "Chattisgarh",
               "Chandigarh",
               "Dadra and Nagar Haveli",
               "Daman and Diu",
               "Delhi",
               "Goa",
               "Gujarat",
               "Haryana",
               "Himachal Pradesh",
               "Hyderabad",
               "Telangana",
               "Jammu and Kashmir",
               "Jharkhand",
               "Karnataka",
               "Kerala",
               "Madhya Pradesh",
               "Maharashtra",
               "Manipur",
               "Meghalaya",
               "Mizoram",
               "Nagaland",
               "Orissa",
               "Punjab",
               "Pondicherry",
               "Rajasthan",
               "Sikkim",
               "Tamil Nadu",
               "Tripura",
               "Uttar Pradesh",
               "Uttarakhand",
               "West Bengal"
        ]
        response['states'] = states
        print response
        return render(request,'statewise.html',{'response':response})

    else:
        states = [
               "Andhra Pradesh",
               "Arunachal Pradesh",
               "Assam",
               "Bihar",
               "Chattisgarh",
               "Chandigarh",
               "Dadra and Nagar Haveli",
               "Daman and Diu",
               "Delhi",
               "Goa",
               "Gujarat",
               "Haryana",
               "Himachal Pradesh",
               "Hyderabad",
               "Jammu and Kashmir",
               "Jharkhand",
               "Karnataka",
               "Kerala",
               "Madhya Pradesh",
               "Maharashtra",
               "Manipur",
               "Meghalaya",
               "Mizoram",
               "Nagaland",
               "Orissa",
               "Punjab",
               "Pondicherry",
               "Rajasthan",
               "Sikkim",
               "Tamil Nadu",
               "Telangana",
               "Tripura",
               "Uttar Pradesh",
               "Uttarakhand",
               "West Bengal"
        ]
        response = {}
        response['states'] = states
        # print response

        return render(request,'statewise.html',{'response':response})

def collegestatus():
    colleges = College.objects.all()
    for college in colleges:
        college.status = False
        college.save()
        print college.collegeName

def quizteamdata():
    rb = open_workbook('QUIZ REGISTRATION.xlsx')
    s = rb.sheet_by_index(0)
    for i in range(0,93):
        quizteam = quizTeam(slot = 0)
        # quizteam.quizTeamId = literal_eval(str(s.cell(i,0)).split(':')[1])
        member1Email = literal_eval(str(s.cell(i,1)).split(':')[1])
        try:
            user1 = TechProfile.objects.get(email = member1Email)
            member2Email = literal_eval(str(s.cell(i,2)).split(':')[1])
            quizteam.quizTeamId = literal_eval(str(s.cell(i,0)).split(':')[1])
            quizteam.save()
            quizteam.members.add(user1)
            print member2Email
            try:
                user2 = TechProfile.objects.get(email= member2Email)
                quizteam.members.add(user2)
            except Exception as e:
                print e
        except:
            pass
        print member1Email
        # print i

def dhokebaaj():
    response = {}
    count = 0
    response['dhokewale'] = []
    users = TechProfile.objects.all()
    url = sheetUrls["dhokebaaj"]
    for user in users:
        try:
            print user.user.first_name
            print "TEAM CHECK"
            teams = Team.objects.filter(Q(members = user) | Q(teamLeader = user))
            print teams[0]
        except:
            try:
                print "WORKSHOP CHECK"
                workshops = WorkshopTeam.objects.filter(Q(members = user) | Q(teamLeader = user))
                print workshops[0]
            except:
                try:
                    print "Quiz teams"
                    qteams = quizTeam.objects.filter(Q(members = user))
                    print qteams[0]
                except:
                    try:
                        print "Startup check"
                        startupteams = StartUpFair.objects.filter(teamLeader = user)
                        print startupteams[0]
                    except:
                        dhokewala = {}
                        count +=1
                        dic = {}
                        dic = {
                        "name" : user.user.first_name,
                        "technexId" : user.technexId,
                        "college" : user.college.collegeName,
                        "mobileNumber" : user.mobileNumber,
                        "email" : user.email
                        }
                        print dic
                        if str(user.college.collegeWebsite) != "190" :
                            requests.post(url,data=dic)


                        # dhokewala['name'] = user.user.first_name
                        # dhokewala['technexId'] = user.technexId
                        # dhokewala['college'] = user.college.collegeName
                        # dhokewala['mobileNumber'] = user.mobileNumber
                        # response['dhokewale'].append(dhokewala)
    # print response
    # response['count'] = count
    print count
    # return render(request , 'dhokewale.html' , {'response' : response})



TimeInMinutesForQuiz = 42

@csrf_exempt
def startQuiz(request):
    response = {}
    if request.method == 'POST':
        post = request.POST
        Quiz = quiz.objects.get(quizId = post['quizId'])
        QuizTeam = quizTeam2.objects.get(quizTeamId = post['teamId'])
        if Quiz.activeStatus == 1:
            try:
                QuizResponse = quizResponses.objects.get(quiz = Quiz, quizTeam = QuizTeam)
                response['status'] = 4 # Quiz Already Started
            except:
                QuestionIds = questions.objects.filter(quiz = Quiz).values_list('questionId', flat=True)

                QuestionsForTeam = random.sample(QuestionIds,5)
                Questions = questions.objects.filter(questionId__in = QuestionsForTeam)
                QuizResponse = quizResponses(quiz = Quiz,quizTeam = QuizTeam)
                QuizResponse.save()
                print Questions.count()
                for Question in Questions:
                    QuizResponse.questions.add(Question)
                response['status'] = 1 # Successfully Quiz started
        else:
            if Quiz.activeStatus == 0:
                response['status'] = 2 # Quiz is not active right now
            else:
                response['status'] = 3 # Quiz closed
    else:
        response['status'] = 0 # Invalid Request
    return JsonResponse(response)

@csrf_exempt
def registerResponse(request):
    response = {}
    if request.method == 'POST':
        post = request.POST
        quizResponse = quizResponses.objects.get(responseId = post['responseId'])
        question = questions.o
        bjects.get(questionId = post['questionId'])
        if quizResponse.quiz.activeStatus is not 1:
            response['status'] = 4 # Quiz Not Active Right Now
            return HttpResponse("Quiz not active right now!!")
            # return JsonResponse(response)
        elif not quizResponse.validForSubmission(TimeInMinutesForQuiz):
            response['status'] = 2 # Quiz Already Submitted
            return HttpResponse("Quiz has already been Submitted")
            # return JsonResponse(response)
        elif quizResponse.status == 2:
            response['status'] = 3 # Quiz Finished by the User
            return JsonResponse(response)
            # return HttpResponse("Quiz already finished by the user")
            # return JsonResponse(response)
        try:
            questionResponse = chutiyapa.objects.get(quiz = quizResponse, question = question)
            questionResponse.fieldChutiyap = post['integerAnswer']
        except:
            questionResponse = chutiyapa(quiz = quizResponse, question = question, fieldChutiyap = post['integerAnswer'])
        questionResponse.save()
        response['answer'] = post['integerAnswer']
        print request.POST
        response['status'] = 1 # Successfully registered
    else:
        response['status'] = 0 # Invalid Request
    return JsonResponse(response)


@csrf_exempt
def finishQuiz(request,responseKey):
    response = {}
    if request.method == 'GET':
        post = request.GET
        quizResponse = quizResponses.objects.get(responseId = responseKey)
        if quizResponse.status == 2:
            response['status'] = 2 # Quiz Already Finished
            return render(request,'startquiz.html',{'response':"Quiz has already been finished by the user!"})
            #return HttpResponse("Quiz has already been finished by the user!")
        quizResponse.status = 2
        quizResponse.save()
        response['status'] = 1
        return render(request,'startquiz.html',{'response':"Quiz finished successfully!"})
        #return HttpResponse("Quiz finished successfully!")
    else:
        response['status'] = 0
        return HttpResponse("Some error occurred! Please report at tech@technex.in")
    # return JsonResponse(response)

@csrf_exempt
def quizPlay(request,quizKey):
    # return HttpResponse("Quiz Postponed for tommorrow due to overload on server, new quiz links will be sent soon. Stay tuned on https://www.facebook.com/events/365382803833825/ for further information.")

    response = {}
    if request.method == 'GET':
        if 1:#try#kkfkfk:
            try:
                team = quizTeam2.objects.get(key = str(quizKey))
            except:
                return render(request,'startquiz.html',{'response':'Invalid Link, please check your mail for the latest Link !!'})
            try:
                if team.quiz.activeStatus == 2:
                    return render(request,'startquiz.html',{'response':"You have already Submitted the Quiz!!"})
                elif team.quiz.activeStatus == 0:
                    return render(request,'startquiz.html',{'response':"Quiz will start soon ...!!!"})
                '''
                elif QuizResponse.quiz.activeStatus is not 1:
                    response['status'] = 4 # Quiz Not Active Right Now
                    return render(request , 'startquiz.html',{'response':"Quiz Will Start Soon..!"})
                    # return JsonResponse(response)
                elif not QuizResponse.validForSubmission(TimeInMinutesForQuiz):
                    response['status'] = 2 # Quiz Submitted due to timeout
                    # return JsonResponse(response)
                    #return HttpResponse("Time over. Quiz Submitted!")
                    return render(request,'startquiz.html',{'response':"Time Over..Quiz Automatically Submitted!"})
                elif QuizResponse.status == 2:
                    return render(request,'startquiz.html',{'response':'Quiz Already Submitted by You!!'}) # Quiz Finished by the User
            '''
            except:
                return render(request,'startquiz.html',{'response':'Quiz will Start Soon ..!!'})
            try:
                Questions = team.quizresponses.questions.all()
                QuizResponse = team.quizresponses
                if QuizResponse.status == 2:
                    response['status'] = 4 # Quiz Not Active Right Now
                    return render(request , 'startquiz.html',{'response':"Quiz Submitted !!!"})
            except:

                QuestionIds = questions.objects.filter(quiz = team.quiz).values_list('questionId', flat=True)
                QuestionsForTeam = random.sample(QuestionIds, 10)
                Questions = questions.objects.filter(questionId__in = QuestionsForTeam)
                QuizResponse = quizResponses(quiz = team.quiz,quizTeam = team)
                QuizResponse.save()
                for Question in Questions:
                        QuizResponse.questions.add(Question)

                #return JsonResponse(response)
                #return render(request,'startquiz.html',{'response':"Quiz Responses have been submitted by the user"})
                # return JsonResponse(response)
                #return HttpResponse("Quiz Responses have been submitted by the user")
            questionArray = []
            for Question in Questions:
                questionobject = {}
                try:
                    k = chutiyapa.objects.get(question = Question, quiz = QuizResponse)
                    print "yaha"
                    questionobject['responseOfUser'] = k.fieldChutiyap

                except:
                    questionobject['responseOfUser'] = ""
                questionobject['question'] = Question.question
                questionobject['questionId'] = Question.questionId
                questionArray.append(questionobject)
            response['questions'] = questionArray
            response['responseId'] = QuizResponse.responseId
            response['timer'] = TimeInMinutesForQuiz*60 - QuizResponse.timer()
            print QuizResponse.timer()
            print response
        return render(request,'quiz.html',response)

SubjectM = "Intellecx Online Round | Internship Opportunities | Prizes worth ₹ 90,000"
bodyM = '''
Hello,

Greetings from Team Technex,

“Wisdom is not to a gift to be received, but a prize to be earned through experience and toils.”

TECHNEX '18 gives you an opportunity to test your aptitude and reasoning skills in INTELLECX, an event where you push your intellectual limits to the fullest. With prizes of ₹ 90,000 and Internship opportunities up for grabs, INTELLECX is a two-stage event, the first round of which is an online round. Following are the rules for the first round:-

1. The online round consists of 10 aptitude questions to be answered in 40 minutes.

2. You can participate individually or, in a team of two members.

3. The timings for the event slots are

        Ø  6:00 pm-6:40 pm, Sat 4 Feb, 2018

        Ø  10:00 pm -10:40 pm, Sun 5 Feb, 2018

You can register in either of the slots for the event as per your convenience.

4. The winners of the online round get prizes worth ₹ 15000 and will be called for the next (GD/PI) round of INTELLECX in TECHNEX '18

Register for the event http://www.technex.in/intellecx .
You can also find the Registration link on dashboard.

For more information and latest updates follow the https://www.facebook.com/events/365382803833825/

For any queries contact:
Kuljeet Keshav +918009596212
Kumar Anunay +919935009220

So, this spring, be prepared for a brainstorming ride into the mental domain at TECHNEX '18


--
Regards
Team Technex '18

Visit our website: www.technex.in
Follow us on Facebook: www.facebook.com/technex
Follow us on Instagram: www.instagram.com/technexiitbhu

'''

def keyCreator():
    quizes = quizTeam2.objects.all()
    for quizz in quizes:
        key = hash("technex"+quizz.quizTeamId+"livelong")
        quizz.key = key

        print key
        quizz.save()


def shift():
    quizd = quiz.objects.get(quizId = 3)
    event = Event.objects.get(nameSlug = 'astroquiz')
    teams = Team.objects.filter(event = event)
    print teams.count()
    counter=0;
    for team in teams:
        counter = counter +1
        quizteama = quizTeam2(quiz = quizd,quizTeamId = 'ABS'+str(1000+counter),member1Email = team.teamLeader.email,member1Phone=team.teamLeader.mobileNumber,name1=team.teamLeader.user.first_name)
        try:
            quizteama.member2Email = team.members.all()[0].email
            quizteama.member2Phone = team.members.all()[0].mobileNumber
            quizteama.name2 = team.members.all()[0].user.first_name
        except:
            print "###############################"
        quizteama.save()

@csrf_exempt
@login_required(login_url='/register/')
def quizRegister(request):
    response = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        users = []
        print data
        for user in data['members']:
            try:
                try:
                    member = TechProfile.objects.get(email = user)
                    users.append(member)
                except:
                    member = TechProfile.objects.get(technexId = user)
                    users.append(member)
            except:
                response['status'] = 0
                response['error'] = 'Member not Registered('+user+')'
                return JsonResponse(response)
        users = list(set(users))
        for u in users:
            try:
                quizteam = quizTeam.objects.get(members = u )
                response['status'] = 0
                response['error'] = u.email+' Already registered for this event !!!'
                return JsonResponse(response)
            except:
                pass

        quizteam = quizTeam(slot = data['slot'])
        quizteam.save()
        slot = ""
        if data['slot'] is 1:
            slot =  "SATURDAY 4/02/2018 18:00 - 18:40"
        else:
            slot = "SUNDAY 5/02/2018 22:00 - 22:40"
        quizteam.quizTeamId = "INX" + str(1000+quizteam.teamId)
        quizteam.save()
        subject = "[Technex'18] Successful Registration for Intellecx"
        body = '''
Dear %s,

Thanks for registering for Intellecx Technex'18.

Your Team Details Are
TeamId- %s
Team Members- %s
Time Slot- %s

For any queries, Contact -
Kuljeet Keshav +918009596212
Kumar Anunay +919935009220

An important note to ensure that the team can contact you further:  If you find this email in Spam folder, please right click on the email and click on 'NOT SPAM'.


Note : As this is an automatically generated email, please don't  reply to this mail. Please feel free to contact us either through mail or by phone incase of any further queries. The contact details are clearly mentioned on the website www.technex.in.


Looking forward to seeing you soon at Technex 2018.

All the best!


Regards

Team Technex
Regards
            '''
        memberEmails = ""
        for user in users:
            memberEmails += user.email+'  '
            quizteam.members.add(user)
        for user in users:
            send_email(user.email,subject,body%(user.user.first_name,quizteam.quizTeamId,memberEmails,slot))

        quiz_spreadsheetfill(quizteam)

        response['status'] = 1
        return JsonResponse(response)
    else:
        response['status'] = 0
        return render(request, '500.html',contextCall(request))

# def test(request):
#     return render(request,'intellecx.html')

@csrf_exempt
def watermark(request):
    response = {}
    if request.method == 'POST':
        post = request.POST
        id_ = post['uid']
        accessToken = post['accessToken']
        url = "http://graph.facebook.com/" + id_ + "/picture?width=9999&height=9999"
        file1 = cStringIO.StringIO(urllib.urlopen(url).read())
        background = Image.open(file1)
        file2 = cStringIO.StringIO(urllib.urlopen("http://res.cloudinary.com/dlvrwjxot/image/upload/v1517846133/Tekk_Overlay.png").read())
        overlay = Image.open(file2)
        width = background.getbbox()[2]
        height = background.getbbox()[3]

        overlay = overlay.resize((width,height))
        background.paste(overlay,(0,0),overlay)

        background.save(id_ + ".png","PNG")
        cloudinary.config(
          cloud_name = "dlvrwjxot",
          api_key = "682868955162224",
          api_secret = "e92MJYvYL6nt9II31rPr-grjvrc"
        )
        x = cloudinary.uploader.upload(id_+".png")

        os.remove(id_+".png")
        response['status'] = 1
        response['url'] = x['secure_url']
        response['accessToken'] = accessToken
        response['uid'] = id_
        return JsonResponse(response)

@csrf_exempt
def finalImage(request):
    response = {}
    if request.method == 'POST':
        post = request.POST
        graph = facebook.GraphAPI(access_token = post['accessToken'], version= '2.2')
        fh = open(post['accessToken']+".png", "wb")
        fh.write(post['base64'].decode('base64'))
        fh.close()
        tags = [{"tag_uid": "225615937462895", "x": 1, "y": 1}]
        r =graph.put_photo(image=open(post['accessToken']+".png",'rb'), album_path="me/photos", message='', **{'tags[0]': tags})
        print r
        os.remove(post['accessToken']+".png")
        response['albumId'] = r['id']
        response['uid'] = post['uid']
        response['status'] = 1
        return JsonResponse(response)
    else:
        response['status'] = 0
        return JsonResponse(response)

def slowConnection(request):
    response = {}
    if request.method == 'POST':
        post = request.POST
        id_ = post['uid']
        accessToken = post['accessToken']
        url = "http://graph.facebook.com/" + id_ + "/picture?width=9999&height=9999"
        file1 = cStringIO.StringIO(urllib.urlopen(url).read())
        background = Image.open(file1)
        file2 = cStringIO.StringIO(urllib.urlopen("http://res.cloudinary.com/dlvrwjxot/image/upload/v1517846133/Tekk_Overlay.png").read())
        overlay = Image.open(file2)
        width = background.getbbox()[2]
        height = background.getbbox()[3]

        overlay = overlay.resize((width,height))
        background.paste(overlay,(0,0),overlay)

        background.save(id_ + ".png","PNG")
        cloudinary.config(
          cloud_name = "dlvrwjxot",
          api_key = "682868955162224",
          api_secret = "e92MJYvYL6nt9II31rPr-grjvrc"
        )
        x = cloudinary.uploader.upload(id_+".png")
        graph = facebook.GraphAPI(access_token = post['accessToken'], version= '2.2')
        tags = [{"tag_uid": "225615937462895", "x": 1, "y": 1}]
        r =graph.put_photo(image=open(id_+".png",'rb'), album_path="me/photos", message='', **{'tags[0]': tags})
        response['status'] = 1
        response['albumId'] = r['id']
        response['uid'] = id_
        os.remove(id_+".png")
        return JsonResponse(response)


def stayTechnexed(request):
    return render(request,'stayTechnexed.html')

@csrf_exempt
def posts(request):
    limit = 5
    response = {}
    if 1:#try:
        token = request.POST['token']
        graph = facebook.GraphAPI(access_token = token, version= '2.2')
        profile = graph.get_object(id ='225615937462895')
        posts = graph.get_connections(profile['id'],"posts",limit = limit)

        postsList = []
        for post in posts['data']:
            postObject = {}
            postObject['link'] = post['link']
            postObject['text'] = post['message']
            postsList.append(postObject)
        response['status'] = 1
        response['posts'] = posts
        return JsonResponse(response)
    else:#except:
        response['status'] = 0
        return JsonResponse(response)


def krackatwork():

    event = Event.objects.get(nameSlug = 'krackat')
    teams = Team.objects.filter(event = event)
    count = 0
    for team in teams:
        part = ""
        techprofile = team.teamLeader
        eventteams = Team.objects.filter(Q(members = techprofile) | Q(teamLeader = techprofile))
        for eventteam in eventteams:
            part += str(eventteam.event.eventName.encode("utf-8")) + ","
        workshopteams = WorkshopTeam.objects.filter(Q(members = techprofile) | Q(teamLeader = techprofile)).distinct()
        for workshopteam in workshopteams:
            part += str(workshopteam.workshop.title.encode("utf-8")) + ","
        startupteams = StartUpFair.objects.filter(teamLeader = techprofile)
        for startupteam in startupteams:
            part += "startupfair,"
        if str(techprofile.college.collegeWebsite) != "190" :
            url = sheetUrls["krackatdata"]
            dic = {}
            dic = {
            "name" : techprofile.user.first_name,
            "technexId" : techprofile.technexId,
            "college" : techprofile.college.collegeName,
            "mobileNumber" : techprofile.mobileNumber,
            "events" : part
            }
            print dic
            requests.post(url,data=dic)
    
@csrf_exempt
@user_passes_test(lambda u: u.is_staff)
def payment_summary(request):
    dic = {}
    total = 0
    dic['paysum'] = {}

    parentevents = ParentEvent.objects.all()
    for parent in parentevents:
        events = Event.objects.all().filter(parentEvent = parent)
        for event in events:
            dic['paysum'][event.eventName] = 0
            

    dic['paysum']['Ventura'] = 0
    dic['paysum']['StartUpBattle'] = 0

    sheet = sheetpayment.objects.all()
    for ticket in sheet:
        if "Registration" in ticket.ticketName and "Ventura" not in ticket.ticketName and "Kracket" not in ticket.ticketName and "Innovians" not in ticket.ticketName:
            techprofile = TechProfile.objects.filter(email = ticket.email)
            try:
                teams = Team.objects.all().filter(teamLeader = techprofile[0])
                for team in teams:
                        dic['paysum'][team.event.eventName] = dic['paysum'][team.event.eventName] + 1
            except:
                print "error"

        if "Ventura" in ticket.ticketName:
            dic['paysum']['Ventura'] = dic['paysum']['Ventura'] + 1

        if "Startupfair" in ticket.ticketName:
            dic['paysum']['StartUpBattle'] = dic['paysum']['StartUpBattle'] + 1
        total = total + 1

    dic['total'] = total-1
            
    return render(request,'paysum.html',dic)

@csrf_exempt
@user_passes_test(lambda u: u.is_staff)
def payment_report(request):
    response = {}
    if request.method == 'POST':
        dic =  request.POST
        data = dic['input']
        try:
            # user = User.objects.get(email = email)
            try:
                techprofile = TechProfile.objects.get(email=data)
            except:
                try:
                    techprofile = TechProfile.objects.get(technexId = data.upper())
                except:
                    techprofile = TechProfile.objects.get(mobileNumber = data)
            
            user = techprofile.user
            response['name'] = user.first_name 
            response['email'] = techprofile.email
            response['technexId'] = techprofile.technexId
            response['college'] = techprofile.college.collegeName
            response['number'] = techprofile.mobileNumber
            response['pay'] = []

            pay = sheetpayment.objects.all().filter(tech = techprofile)
            response['status'] = 1
            for payment in pay:
                p = []
                p.append(payment.ticketId)
                p.append(payment.ticketName)
                p.append(payment.ticketPrice)
                response['pay'].append(p) 

            if not response['pay']:
                response['status'] = 2

        except:
            response['status'] = 0

        return JsonResponse(response)
    else:
        return render(request,'payreport.html')

def sheetpaywithcollege(pro):

    dic = {
        "name" : pro.tech.user.first_name,
        "email" : pro.email,
        "technexId" : pro.tech.technexId,
        "College" : pro.tech.college,
        "ticketName" : pro.ticketName,
        "ticketId" : pro.ticketId,
        "ticketprice" : pro.ticketPrice,
        "registeredOn" : pro.timeStamp,
        }

    url = "https://script.google.com/a/technex.in/macros/s/AKfycbzi_JDir9HH9GWY6L6qZrL96CnytEcDyzR9t_M060mh7M5n7IY/exec"
    print(requests.post(url,data=dic))

def workshopsheet(pay):
    print(pay.ticketName)
    url = sheetUrls[str(pay.ticketName)]
    dic = {
            "name" : pay.tech.user.first_name,
            "email" : pay.email,
            "technexId" : pay.tech.technexId,
            "College" : pay.tech.college,
            "ticketName" : pay.ticketName,
            "ticketId" : pay.ticketId,
            "ticketprice" : pay.ticketPrice,
            "registeredOn" : pay.timeStamp,
            }

    print(requests.post(url,data=dic))


def paymentdata():
    # url = r'http://technex.in/static/Attendee_Report.xls'
    # tables = pd.read_html(url) # Returns list of all tables on page
    # table = tables[0]
    # table.to_csv('payment.csv')

    # df_new = pd.read_csv('payment.csv')
    # writer = pd.ExcelWriter('payment.xlsx')
    # df_new.to_excel(writer, index = False)
    # writer.save()

    rb = open_workbook('Attendee_Report.xlsx')
    s = rb.sheet_by_index(0)
    urls = sheetUrls["payments"]
    fail = 0
    try:
        beginIndex = sheetpayment.objects.latest('row').row + 2
    except:
        beginIndex = 1

    print beginIndex
    for i in range(beginIndex,s.nrows):#range(1,sheet.nrows)
        email = literal_eval(str(s.cell(i,1)).split(':')[1]).encode("utf-8")
        tx= literal_eval(str(s.cell(i,2)).split(':')[1]).encode("utf-8")
        print email,tx
        try:
            try:
                tp = TechProfile.objects.get(email__iexact = email)
            except:
                tp = TechProfile.objects.get(technexId = tx)
            pays = sheetpayment(tech = tp)
            pays.email = email
            pays.ticketId = literal_eval(str(s.cell(i,5)).split(':')[1]).encode("utf-8")
            # pays.row = literal_eval(str(s.cell(i,0)).split(':')[1])
            pays.row = i+100
            #pays.contact = literal_eval(str(s.cell(i,2)).split(':')[1])
            pays.ticketPrice = int(literal_eval(str(s.cell(i,6)).split(':')[1]))
            print pays.ticketPrice
            pays.timeStamp = literal_eval(str(s.cell(i,7))[5:].encode("utf-8")).encode("utf-8")
            ticketName = literal_eval(str(s.cell(i,4)).split(':')[1]).encode("utf-8")
            # if ticketName == "Registration - Without Accomodation" or ticketName == "Registration - Accommodation for workshop participants" or ticketName == "Registration - Accommodation only for workshop participants" or ticketName == "Registration + Free accommodation (only for workshop participants)":
            #     pays.ticketName = "Registration"
            # else:
            pays.ticketName = ticketName
            pays.save() # pays.save()

            # if "Registration" not in pays.ticketName and "Ventura" not in pays.ticketName and "Krackat" not in pays.ticketName and "Innovians" not in pays.ticketName and "test" not in pays.ticketName:
            #     workshopsheet(pays)

            # try:
            #     sheetpaywithcollege(pays)
            # except:
            #     pass
            # print tp.user.first_name
        except Exception as e:
            print email
            dic = {}
            #tpc = TechProfile.objects.filter(mobileNumber = str(literal_eval(str(s.cell(i,2)).split(':')[1])).split('.')[0]).count()

            dic = {
            'email' : email,
            'Technex Id' : tx,
            'name' :  literal_eval(str(s.cell(i,0)).split(':')[1]).encode("utf-8"),
            'ticketname' : literal_eval(str(s.cell(i,4)).split(':')[1]).encode("utf-8"),
            }

            # if tpc is 0:
            #     dic['status']=0
            # else:
            #     dic['status']=1
            print dic
            #requests.post(urls,data= dic)
            print e.message
            fail = fail + 1
    print fail

def spontypefill():
	rb = open_workbook('SponsorTypeData.xls')
	s = rb.sheet_by_index(0)
	for i in range(1,36):
		stype = literal_eval(str(s.cell(i,1)).split(':')[1]).encode("utf-8")
		order = int(literal_eval(str(s.cell(i,2)).split(':')[1]))
		spon = SponsorshipType(title = stype, order = order)
		spon.save()

def sponsorfill():
	rb  = open_workbook('SponsorData.xls')
	st = SponsorshipType.objects.all()
	s = rb.sheet_by_index(0)
	for i in range(1,58):
		index = int(literal_eval(str(s.cell(i,0)).split(':')[1]))
		title = literal_eval(str(s.cell(i,2)).split(':')[1]).encode("utf-8")
		order = int(literal_eval(str(s.cell(i,1)).split(':')[1]))
		imageLink = literal_eval(str(s.cell(i,3))[6:].encode("utf-8"))
		websiteLink = literal_eval(str(s.cell(i,4))[6:].encode("utf-8"))
		print literal_eval(str(s.cell(i,2)).split(':')[1])
		print imageLink
		print websiteLink
		spons = Sponsors(sponsorType = st[index-1], name = title, order = order, imageLink = imageLink, websiteLink = websiteLink)
		spons.save()	
		

def astro():
    quizs = quiz.objects.get(name = "Astro Quiz")
    url = sheetUrls["astroquizdata"]
    quizresponses = quizResponses.objects.filter(quiz = quizs).distinct()
    for quizresponse in quizresponses:
        quizteam = quizresponse.quizTeam
        dic = {}
        dic = {
        "quizTeamId" : quizteam.quizTeamId,
        "name1" : quizteam.name1,
        "name2" : quizteam.name2,
        "email1" : quizteam.member1Email,
        "email2" : quizteam.member2Email,
        "phone1" : quizteam.member1Phone,
        "phone2" : quizteam.member2Phone,
        }
        requests.post(url,data =dic)

@csrf_exempt
@login_required(login_url = '/register/')
def tshirt(request):
    response = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user
        tp = user.techprofile
        if tp.tshirtdata:
            response['status'] =0
            response['message'] = "You have already submitted the data for T-shirt"
            return JsonResponse(response)
        else:
            tp.tshirtsize= data['size']
            # tp.color = data['color']
            tp.gender = data['gender']
            tp.arrivaldate = data['date'].split('-')[2]
            tp.tshirtdata = True
            tp.save()
            suggestion = suggestions(tech = tp, suggestion = data['suggestions'])
            # for event in data['events']:
            #     even = Event.objects.get(eventName = event)
            #     tp.confirmpart.add(even)
            suggestion.save()
            tp.save()

            response['status'] = 1
            return JsonResponse(response)
    else:
        response['status'] = 0
        response['message'] = "Some error occured"
        return JsonResponse(response)



def fixEmail():
    from django.db.models import Count
    faulty = TechProfile.objects.values("email").annotate(Count('id')).order_by().filter(id__count__gt=1)
    print faulty.count()
    for fault in faulty:
        faltus = TechProfile.objects.filter(email = fault['email'])
        print faltus.count
        for faltu in faltus:
            if (Team.objects.filter(Q(teamLeader = faltu) | Q(members = faltu)).count() == 0) and (StartUpFair.objects.filter(teamLeader = faltu).count() == 0) and (quizTeam2.objects.filter(Q(member1Email = faltu.email) | Q(member2Email = faltu.email)).count() == 0) and  (WorkshopTeam.objects.filter(Q(teamLeader = faltu) | Q(members = faltu)).count() == 0) and (TechProfile.objects.filter(email = faltu.email).count() >1):
                a = raw_input("Press Y/N to delete! "+str(faltu.email)+"\n")
                if a == 'y':
                    faltu.delete()
                else:
                    print str(faltu.email)+"Not Deleted \n"

def tshirtList():
    payments = sheetpayment.objects.all().order_by("id")
    basetime = datetime.datetime.strptime('Mon Feb 9 01:00:00 IST 2018','%a %b %d %X IST %Y')
    sheetWale = []
    subject = "[Urgent] Technex T-shirt"
    body = '''
Greetings From Technex !

Kindly fill the form before 11:59 pm on 12 Feb.
Also if you have not registered on Technex website. Please register using this email address.
Claim your tshirts at http://www.technex.in/dashboard/#/tshirtinfo/ !
For any queries contact:
Yash Sharma +917565816969
    '''
    for payment in payments:
        time = datetime.datetime.strptime(payment.timeStamp,'%a %b %d %X IST %Y')
        if basetime > time:
            print "reached"
            if payment.ticketName == 'Innovians Technologies (Final Round) With Accomodation' or payment.ticketName == 'Innovians Technologies (Final Round)' or payment.ticketName == 'Registration - With Accomodation':
                send_email(payment.email,subject,body)
                print payment.id
            elif payment.ticketName == '3D Printing' or payment.ticketName == 'Android App Development' or payment.ticketName == 'Bridge Design' or payment.ticketName == 'Data Mining' or payment.ticketName == 'Digital Marketing' or payment.ticketName == 'Ethical Hacking' or payment.ticketName == 'Industrial Automation - PLC & SCADA' or payment.ticketName == 'Internet of Things' or payment.ticketName == 'Swarm Robotics' or payment.ticketName =='Vision Botics (Sixth Sense Technology)' or payment.ticketName =='Automobile':
                g = sheetpayment.objects.filter(email = payment.email).values_list('ticketName')
                if (u'Registration',) in g:
                    send_email(payment.email,subject,body)
                    print payment.id
    for sheetWala in sheetWale:
        shirt(sheetWala)



def shirt(payment):
    dic = {
    'ticketName' : payment.ticketName,
    'email' : payment.email,
    'contact' : payment.contact,
    'ticketPrice' : payment.ticketPrice,
    'timeStamp': payment.timeStamp
    }

    url = 'https://script.google.com/macros/s/AKfycbwXMM3Hd9oqbP6uAIopw_uqDxrwphl6RletLMcgIU6U4W4gB8oZ/exec'
    requests.post(url,data=dic)

def intellecxResult():
    quizs = quiz.objects.get(name = "Abcd")
    url = sheetUrls["intellecxresult"]
    quizresponses = quizResponses.objects.filter(quiz = quizs)
    for quizresponse in quizresponses:
        score = 0
        responses = chutiyapa.objects.filter(quiz = quizresponse)
        for response in responses:
            print response
            print str(response.fieldChutiyap)
            print str(response.question.integerAnswer)
            if str(response.fieldChutiyap) == str(response.question.integerAnswer):
                score = score+1
        team = quizresponse.quizTeam
        dic = {
        'teamId' : team.quizTeamId,
        'name1'  : team.name1.encode("utf-8"),
        'email1' : team.member1Email.encode("utf-8"), 
        'phone1' : team.member1Phone.encode("utf-8"),
        'score' : score,
        }
        try: 
            tp = TechProfile.objects.get(email__iexact = team.member1Email)
            dic['college1'] = tp.college.collegeName
        except:
            dic['college1'] = 0
        try:
            dic['name2'] = team.name2.encode("utf-8")
            dic['email2'] = team.member2Email.encode("utf-8")
            dic['phone2']  =  team.member2Phone.encode("utf-8")      
            try:
                tp = TechProfile.objects.get(email__iexact = team.member2Email)
                dic['college2'] = tp.college.collegeName
            except:
                dic['college2'] = 0
        except:
            dic['name2'] = 0
            dic['email2'] = 0
            dic['phone2'] = 0
            dic['college2'] = 0

        print score    
        print dic 
        requests.post(url, data = dic)        

            


def workshopWale():
    payments = sheetpayment.objects.all()
    thullu = []
    for payment in payments:
        if payment.ticketName == '3D Printing' or payment.ticketName == 'Android App Development' or payment.ticketName == 'Bridge Design' or payment.ticketName == 'Data Mining' or payment.ticketName == 'Digital Marketing' or payment.ticketName == 'Ethical Hacking' or payment.ticketName == 'Industrial Automation - PLC & SCADA' or payment.ticketName == 'Internet of Things' or payment.ticketName == 'Swarm Robotics' or payment.ticketName =='Vision Botics (Sixth Sense Technology)' or payment.ticketName =='Automobile':
            otherPaymentCount = sheetpayment.objects.filter(email = payment.email).count()
            if otherPaymentCount < 2:
                thullu.append(payment)

    for thula in thullu:
        sheetWorkshopWale(thula)

def sheetWorkshopWale(payment):
    dic = {
    'ticketName' : payment.ticketName,
    'email' : payment.email,
    'contact' : payment.contact,
    'ticketPrice' : payment.ticketPrice,
    'timeStamp': payment.timeStamp
    }

    url = 'https://script.google.com/macros/s/AKfycbxGZICcHWbLMgeQ7UqMosjALpXOPAgASeY9Cca3kL-bfoAFfz87/exec'
    requests.post(url,data=dic)


def coreteam(request):
    return HttpResponseRedirect('https://docs.google.com/forms/d/e/1FAIpQLSdrnLbzzwmcUcFKdIj7rb8ablEnjJRbs_0Po1PD4V8axizmSA/viewform')    

def exhibitionRegister(request):
    return HttpResponseRedirect('https://goo.gl/forms/XJxNsGjQkSevgko12')

def innovians(request):
    return HttpResponseRedirect('https://goo.gl/forms/w3kHCh9D0tzdsIds1')    

def eisystems(request):
    return HttpResponseRedirect('https://goo.gl/forms/aOX51iDJTsOMLGOH3')

def htindia(request):
    return HttpResponseRedirect('https://goo.gl/forms/nS1hLlU1RYXXoUO93')

def ccregister(request):
    return HttpResponseRedirect('https://goo.gl/forms/3WRcuXr3Ic0fQBmH2')

def talksregister(request):
    return HttpResponseRedirect('https://goo.gl/forms/DN7hBWjM2wgQPP7H2')

def digilnfy(request):
    return HttpResponseRedirect('https://goo.gl/forms/21xCtip3iM8sgsJC3')

def civilsimplified(request):
    return HttpResponseRedirect('https://goo.gl/forms/MZMSlXKPZZSIW9eJ3')

def techservices(request):
    return HttpResponseRedirect('https://goo.gl/forms/zho9oyNnA3GuGEuF2')

def paneldiscussion(request):
    return HttpResponseRedirect('https://goo.gl/forms/pU01YhJH7iJWtBBi2')

def quantfinance(request):
    return HttpResponseRedirect('https://goo.gl/forms/KxMHZ9SVg11ViSiA2')

def vmware(request):
    return HttpResponseRedirect('https://goo.gl/forms/LKaNbatyCGTVaVGO2')

def applink(request):
    return HttpResponseRedirect('https://play.google.com/store/apps/details?id=org.piratejester.technex17')

def start_up_battle(request):
    return HttpResponseRedirect('https://goo.gl/forms/CHEJPbJKDik5A6TO2')

def hurdle_mania(request):
    return HttpResponseRedirect('https://goo.gl/forms/ocfCpcb7bmrFUe9N2')
def ventura(request):
    return HttpResponseRedirect('https://goo.gl/forms/SvcTvEKN6i5Z80713')
def momentum(request):
    return HttpResponseRedirect('https://goo.gl/forms/1BkzDyjv9QNXkxnz1')
def modex(request):
    return HttpResponseRedirect('https://goo.gl/forms/CQV2REFaoKvsJKqU2')
def exploring_the_interstellar(request):
    return HttpResponseRedirect('https://goo.gl/forms/U0BP7n8GuttkfTMf1')
def greenX(request):
    return HttpResponseRedirect('https://goo.gl/forms/nXwgiJS7eYRwciDU2')
def vikalp(request):
    return HttpResponseRedirect('https://goo.gl/forms/nnKrxsWsuzWXfk7u2')

def Krackat(request):
    return HttpResponseRedirect('https://goo.gl/forms/4FcfDN9hLicnN5mv1')
def manthan(request):
    return HttpResponseRedirect('https://goo.gl/forms/0LWJYbWISYo1B0al1')
def astroquiz(request):
    return HttpResponseRedirect('https://goo.gl/forms/RhVP6eTWo6wMrsGX2')



def tshirtdatafill():
    tp = TechProfile.objects.filter(tshirtdata = True)
    url = sheetUrls["tshirt"]
    print tp.count()
    for t in tp:
        dic = {
        'name' : t.user.first_name.encode("utf-8"),
        'college' : t.college.collegeName,
        'email' : t.email.encode("utf-8"),
        'phone' : t.mobileNumber,
        'size' : t.tshirtsize.encode("utf-8"),
        'color' : t.color.encode("utf-8"),
        'date' : t.arrivaldate.encode("utf-8"),
        'gender' : t.gender.encode("utf-8")
        }   
        print dic
        requests.post(url, data=dic)

def parenetevenetdataerror():
    rb = open_workbook('ParentEventsData.xls')
    s = rb.sheet_by_index(0)
    for i in range(0,11):
        peventId = int(literal_eval(str(s.cell(i,1)).split(':')[1]))
        cName = literal_eval(str(s.cell(i,2)).split(':')[1]).encode("utf-8")
        description = literal_eval(str(s.cell(i,3)).split(':')[1]).encode("utf-8")
        order = int(literal_eval(str(s.cell(i,4)).split(':')[1]))
        nameSlug =  literal_eval(str(s.cell(i,9)).split(':')[1]).encode("utf-8")
        pevent = ParentEvent(parentEventId = peventId, categoryName = cName, description = description, order = order, nameSlug = nameSlug)
        pevent.save()

def eventdataerror():
    rb = open_workbook('eventsData.xls')
    s = rb.sheet_by_index(0)
    for i in range(0,47):
        eventId = int(literal_eval(str(s.cell(i,1)).split(':')[1]))
        eventOrder = int(literal_eval(str(s.cell(i,2)).split(':')[1]))
        eventName = literal_eval(str(s.cell(i,3)).split(':')[1]).encode("utf-8")
        parentEventSlug = literal_eval(str(s.cell(i,4)).split(':')[1]).encode("utf-8")
        print parentEventSlug
        parentEvent = ParentEvent.objects.get(nameSlug = parentEventSlug)
        description = literal_eval(str(s.cell(i,5)).split(':')[1]).encode("utf-8")
        prizeMoney = literal_eval(str(s.cell(i,7)).split(':')[1]).encode("utf-8")
        maxMembers = int(literal_eval(str(s.cell(i,8)).split(':')[1]))
        nameSlug = literal_eval(str(s.cell(i,9)).split(':')[1]).encode("utf-8")
        event = Event(eventId = eventId, eventOrder = eventOrder, eventName = eventName, parentEvent = parentEvent, description = description, prizeMoney = prizeMoney, maxMembers = maxMembers, nameSlug = nameSlug)
        event.save()


def eventoptionsfill():
    rb = open_workbook('EventOptionData.xls')
    s = rb.sheet_by_index(0)
    for i in range(0, 244):
        optionName = literal_eval(str(s.cell(i,1)).split(':')[1]).encode("utf-8")  
        optionDescription = literal_eval(str(s.cell(i,2))[6:].encode("utf-8"))
        event = Event.objects.get(eventId = int(literal_eval(str(s.cell(i,4)).split(':')[1])))
        eventOptionOrder = int(literal_eval(str(s.cell(i,3)).split(':')[1]))
        print optionName
        eventOption = EventOption(event = event, optionName = optionName,eventOptionOrder = eventOptionOrder, optionDescription = optionDescription)
        eventOption.save()


# def spontypefill():
#     rb = open_workbook('SponsorTypeData.xls')
#     s = rb.sheet_by_index(0)
#     for i in range(1,36):
#         stype = literal_eval(str(s.cell(i,1)).split(':')[1]).encode("utf-8")
#         order = int(literal_eval(str(s.cell(i,2)).split(':')[1]))
#         spon = SponsorshipType(title = stype, order = order)
#         spon.save()

# def sponsorfill():
#     rb  = open_workbook('SponsorData.xls')
#     st = SponsorshipType.objects.all()
#     s = rb.sheet_by_index(0)
#     for i in range(1,58):
#         index = int(literal_eval(str(s.cell(i,0)).split(':')[1]))
#         title = literal_eval(str(s.cell(i,2)).split(':')[1]).encode("utf-8")
#         order = int(literal_eval(str(s.cell(i,1)).split(':')[1]))
#         imageLink = literal_eval(str(s.cell(i,3))[6:].encode("utf-8"))
#         websiteLink = literal_eval(str(s.cell(i,4))[6:].encode("utf-8"))
#         print literal_eval(str(s.cell(i,2)).split(':')[1])
#         print imageLink
#         print websiteLink
#         spons = Sponsors(sponsorType = st[index-1], name = title, order = order, imageLink = imageLink, websiteLink = websiteLink)
#         spons.save()    




def initiative(request):
    if(get_flavour(request) == 'full' ):
        return render(request, 'initiativenew.html')
    else:
        return render(request, 'initiativemobilenew.html') 

def simulation(request):
    if(get_flavour(request) == 'full'):
        return render(request,"simulationnew.html")
    else:
        return render(request,"simulationmobile.html")


def exhibitions(request):
    if(get_flavour(request) == 'full'):
        return render(request,"exhibitionnew.html")
    else:
        return render(request,"exhibitionm.html")

def conclave(request):
    if(get_flavour(request) == 'full'):
        return render(request,"corporate-conclavenew.html")
    else:
        return render(request,"conclavenewm.html")

def sponsor(request):
    if(get_flavour(request) == 'full'):
        return render(request,"sponsor18d.html")
    else:
        return render(request,"sponsor18m.html")        

def college_data(names,ids,cities,states):
    for i in range(1,575):
        a=College.objects.create()
        a.collegeName=names[i]
        a.city=cities[i]
        a.state=states[i]
        a.status=True
        a.collegeWebsite=ids[i]
        a.save()

def fill_registrations():
    profiles = TechProfile.objects.all()
    for prof in profiles:
        spreadsheetfill_register(prof)

@user_passes_test(lambda u: u.is_staff)
def publicity(request):
    return render(request,"buttons.html")

# def recent_activities(request):
    
#     events = Event.objects.all()
#     eventobj = {}
#     for event in events:
        
#         eventobj[event.eventName] = Team.objects.filter(event = event).count()
#         print eventobj
#         # eventobj['count'] = Team.objects.filter(event = event).count()
#     workshops1 = WorkshopTeam.objects.all().order_by("-timestamp")
#     workshops=workshops1[:5]
#     teams1 = Team.objects.all().order_by("-timestamp")
#     teams=teams1[:5]
#     techprofiles1 = TechProfile.objects.all().order_by("-timestamp")
#     techprofiles=techprofiles1[:5]
#     a=max(eventobj, key=lambda k: eventobj[k])
#     print(a)
#     return render(request,'fbfeeds.html',{'max':a,'teams':teams,'workshops':workshops,'techprofiles':techprofiles})


@csrf_exempt
@login_required(login_url='/register/')
def recent_activities(request):
    user = None
    if request.user.is_authenticated():
        t = request.user.techprofile
        e = request.user.email
        college=t.college
        c=TechProfile.objects.filter(college=college).exclude(email=e)
        
    events = Event.objects.all()
    eventobj = {}
    for event in events:
        
        eventobj[event.eventName] = Team.objects.filter(event = event).count()
        print eventobj
        # eventobj['count'] = Team.objects.filter(event = event).count()
    workshops1 = WorkshopTeam.objects.all().order_by("-timestamp")
    workshops=workshops1[:5]
    teams1 = Team.objects.all().order_by("-timestamp")
    teams=teams1[:5]
    techprofiles1 = TechProfile.objects.all().order_by("-timestamp")
    techprofiles=techprofiles1[:20]
    a=max(eventobj, key=lambda k: eventobj[k])
    print (c)

    return render(request,'fbfeeds.html',{'people':c,'max':a,'teams':teams,'workshops':workshops,'techprofiles':techprofiles})


def createTechP(data,college):
    email = data[1]
    try:
        techProfile = TechProfile.objects.get(email = email)
        return 2
    except:
        try:
            techprofile = TechProfile.objects.get(technexId = data[3])
            return 3
        except:    
            bugUsername = User.objects.latest('id').id
            user = User.objects.create_user(username=str(bugUsername+1))
            techprofile = TechProfile(user = user,email = email)
    user.first_name = data[0]
    password = hash(data[1])
    user.set_password(password)
    user.save()
    techprofile.email = email
    techprofile.technexId = data[3]
    techprofile.college = college
    techprofile.mobileNumber = int(data[5])
    techprofile.year = int(data[4])
    techprofile.city = data[6]
    techprofile.save()
    print user.first_name
    return 1

def fix(start,end):
    book = open_workbook('Technex Registrations 2018.xlsx')
    sheet = book.sheet_by_index(0)
    error = {}
    error['email'] = []
    error['technexId'] = []
    for i in range(start,end):
        row = sheet.row_values(i)
        college = College.objects.filter(collegeName = row[2])
        if len(college) == 0:
            collegee = College.objects.create(collegeName = row[2])
        else:
                collegee = college[0]
        t = createTechP(row,collegee)
        if t==2:
            error['email'].append(i)
        elif t==3:
            error['technexId'].append(i)
    print error


workshopSheetName = ['',]
workshopTitle = ['', '']
workshopfiles = [{'workshoptitle': 'Voice Controlled Automation Using Amazon Alexa','sheetName':'Voice Controlled Automation Using Amazon Alexa.xlsx'},
{'workshoptitle': 'Bridge Design','sheetName':'Bridge Design.xlsx'},
{'workshoptitle': 'E-Commerce','sheetName':'E-Commerce.xlsx'},
{'workshoptitle': 'Digital Marketing','sheetName':'Digital Marketing.xlsx'},
{'workshoptitle': 'Augmented Reality','sheetName':'Augmented Reality.xlsx'},
{'workshoptitle': 'Sixthsense Robotics','sheetName':'Sixthsense Robotics.xlsx'},
{'workshoptitle': 'Android Application Development','sheetName':'Android Application Development.xlsx'},
{'workshoptitle': 'Ethical Hacking and Information Security','sheetName':'Ethical Hacking and Information Security.xlsx'},
{'workshoptitle': 'Automobile Mechanics and IC Engines','sheetName':'Automobile Mechanics and IC Engines.xlsx'},
{'workshoptitle': 'Autonomous Robotics (ArduBotics)','sheetName':'Autonomous Robotics (ArduBotics).xlsx'},
{'workshoptitle': 'Cryptocurrency','sheetName':'Cryptocurrency.xlsx'},
{'workshoptitle': 'Industrial Automation PLC and SCADA','sheetName':'Industrial Automation PLC and SCADA.xlsx'},
{'workshoptitle': 'Internet of Things','sheetName':'Internet of Things.xlsx'},
{'workshoptitle': 'Artificial Intelligence and Machine Learning','sheetName':'Artificial Intelligence and Machine Learning.xlsx'}] 
def workshoperror():
    for workshopdata in workshopfiles:
        book = open_workbook(workshopdata['sheetName'])
        sheet = book.sheet_by_index(0)
        print workshopdata['workshoptitle']
        workshop = Workshops.objects.get(title = workshopdata['workshoptitle'])
        
        for i in range(1,sheet.nrows):
            email = sheet.row_values(i)[1]
            try:
                workshopteam = WorkshopTeam.objects.get(teamName = email,workshop = workshop)
            except:
                try:
                    techProfile = TechProfile.objects.get(email = email)
                    workshopteam = WorkshopTeam(teamName = email,teamLeader = techProfile,workshop = workshop)
                    workshopteam.save()
                except:
                    print email
                        



def cap_email():
    t=TechProfile.objects.all()
    for tech in t:
        e=tech.email
        if not e.islower():
            print(e)

def cap_to_small_email():
    t=TechProfile.objects.all()
    for tech in t:
        e=tech.email
        if not e.islower():
            print(e)
            techp=TechProfile.objects.get(email=e)
            print(techp)
            
            f=e.lower()
            print(f)
            techp.email=f
            techp.save()
            techpro=TechProfile.objects.get(email=f)
            mail=techpro.email
            print(mail)

def two_email():
    t=TechProfile.objects.all()
    for tech in t:
        e=tech.email
        f=e.lower()
        if e!=f:
            try:
                techp=TechProfile.objects.get(email=e)
                techpro=TechProfile.objects.get(email=f)
                print(e)
            except:
                continue


def two_email2():
    t=TechProfile.objects.all()
    for tech in t:
        e=tech.email
        f=e.lower()
        if e==f:
        
            try:
                
                techpro=TechProfile.objects.get(email=f)
                
            except:
                print(f)

def temp_email():
    t=TechProfile.objects.all()
    for tech in t:
        e=tech.email
        f=e.lower()
        if e!=f:
            try:
                techpro=TechProfile.objects.get(email=f)
            except:
                print(e)
                techp=TechProfile.objects.get(email=e)
                techp.email=f
                techp.save()
                techpro=TechProfile.objects.get(email=f)
                mail=techpro.email
                print(mail)

def workshopdata():
    workshops = Workshops.objects.all()
    print 1
    for work in workshops:
        # wb = Workbook()
        w = Workbook()
        # m = 0
        Sheet1 = w.add_sheet('Sheet1')
        # ops = OffLineProfile.objects.filter(hostel = hostel)
        # Sheet1 = wb.add_sheet('sheet1')
        x = 0
        ops = OffLineProfile.objects.filter(workshop = work)
        for op in ops:
            Sheet1.write(x,0,op.techProfile.user.first_name)
            Sheet1.write(x,1,op.techProfile.email)
            Sheet1.write(x,2,op.techProfile.mobileNumber)
            Sheet1.write(x,3,op.techProfile.technexId)
            Sheet1.write(x,4,op.techProfile.college.collegeName)
            Sheet1.write(x,5,op.techProfile.city)
            x = x+1   
        y ="workshop_sheets/" + (work.title) + ".xls" 
        print "Hi"       
        w.save(y)

def print_workshopdata():
    profiles=OffLineProfile.objects.all()
    dic={}
    for pro in profiles:
        if pro.workshop:
            try: 
                dic[pro.workshop.title]=dic[pro.workshop.title]+1
            except:
                dic[pro.workshop.title]=1
    a=0

    for key in dic:
        print str(dic[key]) + " " + key
        a=a+ dic[key]

    print a



# def print_workshopdata_debug():
#     profiles=OffLineProfile.objects.all()
#     dic={}
#     for pro in profiles:
#         if pro.workshop:
#             try: 
#                 dic[pro.workshop.title]=dic[pro.workshop.title]+1
#             except:
#                 dic[pro.workshop.title]=1

#     for key in dic:
#         print str(dic[key]) + " " + key

def print_payment_data():
    transactions=Transaction.objects.all()
    basetime = timezone.make_aware(datetime.datetime.strptime('Wed Feb 14 18:00:00 IST 2018','%a %b %d %X IST %Y'))
    dic={}
    for trans in transactions:
        time =datetime.datetime.strptime(str(trans.timeStamp),'%a %b %d %X IST %Y')
        if time>basetime:
            try: 
                dic[trans.facility.name]=dic[trans.facility.name]+1
            except:
                dic[trans.facility.name]=1

    for key in dic:
        print str(dic[key]) + " " + key





# basetime = datetime.datetime.strptime('Mon Feb 9 01:00:00 IST 2017','%a %b %d %X IST %Y')
#     counter = 0
#     for payment in payments:
#         print "reached"
#         time = datetime.datetime.strptime(payment.timeStamp,'%a %b %d %X IST %Y')



def eventsheetfilling():
    events = Event.objects.all()
    for event in events:
        w = Workbook()
        m = 0
        Sheet1 = w.add_sheet('Sheet1')
        teams = Team.objects.filter(event = event)
        for team in teams:
            try:
                
                x = team.teamLeader
                tl = OffLineProfile.objects.get(techProfile = x)
                Sheet1.write(m,1,str(x.email))
                Sheet1.write(m,2,str(x.mobileNumber))
                m = m+1
                Sheet1.write(m,0,str(team.technexTeamId))
                ops = team.members.all()
                # ops = OffLineProfile.objects.filter(Q(techProfile = y))
                for op in ops:
                    try:
                        opg = OffLineProfile.objects.get(techProfile = op)
                        Sheet1.write(m,1,str(opg.techProfile.email))
                        Sheet1.write(m,2,str(opg.techProfile.mobileNumber))
                        m = m+1
                    except:
                        pass

            except:    
                ops = team.members.all()
                # ops = OffLineProfile.objects.filter(Q(techProfile = y))
                for op in ops:
                    try:
                        Sheet1.write(m,0,str(team.technexTeamId))
                        opg = OffLineProfile.objects.get(techProfile = op)
                        Sheet1.write(m,1,str(opg.techProfile.email))
                        Sheet1.write(m,2,str(opg.techProfile.mobileNumber))
                        m = m+1
                    except:
                        pass
            x = "event_sheets/" + event.eventName+".xls"
            w.save(x)

def hostelsheetfilling():
    #events = Event.objects.all()
    profile = OffLineProfile.objects.all()

    w = Workbook()
    m = 0
    Sheet1 = w.add_sheet('Sheet1')
    for pro in profile:
        Sheet1.write(m,0,pro.techProfile.user.first_name)
        Sheet1.write(m,1,pro.techProfile.college.collegeName)
        Sheet1.write(m,2,pro.techProfile.email)
        Sheet1.write(m,3,pro.techProfile.mobileNumber)
        Sheet1.write(m,5,pro.techProfile.technexId)
        try:
            Sheet1.write(m,4,str(pro.hostel.name))
        except:
            pass    
        m=m+1

    w.save("AccodWise2.xls")


def hostelsheetfilling1():
    #events = Event.objects.all()
    profile = OffLineProfile.objects.all()

    w = Workbook()
    m = 0
    Sheet1 = w.add_sheet('Sheet1')
    for pro in profile:
        try:
            Sheet1.write(m,2,str(pro.hostel.name))
        except:    
            Sheet1.write(m,0,pro.techProfile.user.first_name)
            Sheet1.write(m,1,pro.techProfile.college.collegeName)   
            Sheet1.write(m,2,pro.techProfile.email)
            Sheet1.write(m,3,pro.techProfile.mobileNumber) 
        m=m+1

    w.save("NoAccodWise.xls")  



def hostelsheetfilling2():
    #events = Event.objects.all()
    profile = OffLineProfile.objects.all()
    s = "BHU"
    w = Workbook()
    m = 0
    Sheet1 = w.add_sheet('Sheet1')
    for pro in profile:
        try:
            pro.hostel.name
            if pro.techProfile.college.collegeName.find(s):
                Sheet1.write(m,0,pro.techProfile.user.first_name)
                Sheet1.write(m,1,pro.techProfile.college.collegeName) 
                Sheet1.write(m,2,pro.techProfile.email)
                Sheet1.write(m,3,pro.techProfile.mobileNumber)

        except:    
            pass    
        m=m+1

    w.save("NoAccodBHUWise.xls") 

def offlinedata():
    wb = Workbook()
    ops = OffLineProfile.objects.all()
    Sheet1 = wb.add_sheet('Sheet1')
    x = 0
    for op in ops:
        Sheet1.write(x,0,op.techProfile.user.first_name)
        Sheet1.write(x,1,op.techProfile.email)
        Sheet1.write(x,2,op.techProfile.mobileNumber)
        Sheet1.write(x,3,op.techProfile.college.collegeName)
        Sheet1.write(x,4,op.techProfile.college.collegeWebsite)
        Sheet1.write(x,5,op.techProfile.city)
        x = x+1 

        
    y = 'allexternal.xls' 
    wb.save(y)
                   
def hello(request):
    return HttpResponse("Hello World !!")

def check_allotment():
    pay=sheetpayment.objects.all()
    a=[]
    basetime = datetime.datetime.strptime('Sun Feb 4 23:59:59 IST 2017','%a %b %d %X IST %Y')
    # counter = 0
    # for payment in payments:
    #     print "reached"
        # time = datetime.datetime.strptime(payment.timeStamp,'%a %b %d %X IST %Y')
    for p in pay:
        time = datetime.datetime.strptime(p.timeStamp,'%a %b %d %X IST %Y')
        if p.ticketName == "Registration + Accomodation" or p.ticketName == "Innovians Final of Zonal Round" or p.ticketName == "Technex Registration for Workshop(Free Accommodation)" or p.ticketName == "Startupfair Registration with accomodation" or p.ticketName=="Ventura Registration + Accommodation" or p.ticketName=="Krackat Registration + Accomodation"  or p.ticketName=="Technex Registration for Workshop with Accomodation":
            a.append(p)
        elif p.ticketName=="Technex Registration for Workshop without Accommodation" and time<basetime :
            a.append(p)


    print len(a)
    c=[]
    trans=Transaction.objects.filter(amount=200)
    for pro in trans:
        c.append(pro.creditor)


    print len(c)
    tech2=[]
    # final=[x for x in c and x in a ]
    for hi in a:
        tech2.append(hi.tech)
    for hi in tech2:
        if hi in c:
            final.append(hi)

    
    print len(final)


def wrokshop_pos_neg():
    desk=DeskTeam.objects.get(user__username="Tech")
    transactions=Transaction.objects.all()
    offline_trans=[]
    for trans in transactions:
        if trans.reciever !=desk:
            offline_trans.append(trans)


    workshops=[]
    work=Workshops.objects.all()
    for w in work:
        workshops.append(str(w.title))

    
    # work2=['E-Commerce', 'Digital Marketing', 'Sixthsense Robotics', 'Android Application Development', 'Ethical Hacking and Information Security', 'Internet of Things', 'Bridge Design', 'Cryptocurrency', 'Industrial Automation PLC and SCADA', 'Voice Controlled Automation Using Amazon Alexa', 'Autonomous Robotics (ArduBotics)', 'Artificial Intelligence and Machine Learning', 'Automobile Mechanics and IC Engines']

    

    pos=0
    neg=0
    for off in offline_trans:
        # print off.amount
        if off.facility.name in workshops:
            print off.amount
            if off.amount>0:
                pos=pos+off.amount
            else:
                print off.amount
                neg=neg+off.amount

def eventsheetfilling_one():
    events = Event.objects.all()
    w = Workbook()
    m = 0
    Sheet1 = w.add_sheet('Sheet1')
    for event in events:
        
        # Sheet1 = w.add_sheet('Sheet1')
        teams = Team.objects.filter(event = event)
        for team in teams:
            try:
                
                x = team.teamLeader
                tl = OffLineProfile.objects.get(techProfile = x)
                Sheet1.write(m,1,str(x.email))
                Sheet1.write(m,2,str(x.mobileNumber))
                m = m+1
                Sheet1.write(m,0,str(team.technexTeamId))
                ops = team.members.all()
                # ops = OffLineProfile.objects.filter(Q(techProfile = y))
                for op in ops:
                    try:
                        opg = OffLineProfile.objects.get(techProfile = op)
                        Sheet1.write(m,1,str(opg.techProfile.email))
                        Sheet1.write(m,2,str(opg.techProfile.mobileNumber))
                        m = m+1
                    except:
                        pass

            except:    
                ops = team.members.all()
                # ops = OffLineProfile.objects.filter(Q(techProfile = y))
                for op in ops:
                    try:
                        Sheet1.write(m,0,str(team.technexTeamId))
                        opg = OffLineProfile.objects.get(techProfile = op)
                        Sheet1.write(m,1,str(opg.techProfile.email))
                        Sheet1.write(m,2,str(opg.techProfile.mobileNumber))
                        m = m+1
                    except:
                        pass
        x = "event_sheets/" + "all_events.xls"
        w.save(x)


# def workshopsheetfilling_one():
#     events = Workshops.objects.all()
#     w = Workbook()
#     m = 0
#     Sheet1 = w.add_sheet('Sheet1')
#     for event in events:
        
#         # Sheet1 = w.add_sheet('Sheet1')
#         teams = WorkshopTeam.objects.filter(workshop = event)
#         for team in teams:
#             try:
                
#                 x = team.teamLeader
#                 tl = OffLineProfile.objects.get(techProfile = x)
#                 Sheet1.write(m,1,str(x.email))
#                 Sheet1.write(m,2,str(x.mobileNumber))
#                 m = m+1
#                 Sheet1.write(m,0,str(team.technexTeamId))
#                 ops = team.members.all()
#                 # ops = OffLineProfile.objects.filter(Q(techProfile = y))
#                 for op in ops:
#                     try:
#                         opg = OffLineProfile.objects.get(techProfile = op)
#                         Sheet1.write(m,1,str(opg.techProfile.email))
#                         Sheet1.write(m,2,str(opg.techProfile.mobileNumber))
#                         m = m+1
#                     except:
#                         pass

#             except:    
#                 ops = team.members.all()
#                 # ops = OffLineProfile.objects.filter(Q(techProfile = y))
#                 for op in ops:
#                     try:
#                         Sheet1.write(m,0,str(team.technexTeamId))
#                         opg = OffLineProfile.objects.get(techProfile = op)
#                         Sheet1.write(m,1,str(opg.techProfile.email))
#                         Sheet1.write(m,2,str(opg.techProfile.mobileNumber))
#                         m = m+1
#                     except:
#                         pass
#         x = "event_sheets/" + "all_events.xls"
#         w.save(x)


def profit():
    desk=DeskTeam.objects.get(user__username="Tech")
    transactions=Transaction.objects.all()
    offline_trans=[]
    for trans in transactions:
        if trans.reciever !=desk:
            offline_trans.append(trans)


    h=0

    for t in offline_trans:
        if t.amount!=200 and t.amount!=-200:
            h=h+t.amount
            print t.amount

    print h




def Contacts_new():
    wb = Workbook()
    ops = Team.objects.all()
    Sheet1 = wb.add_sheet('Sheet1')
    x = 0
    p=0
    for op in ops:
        if op.event.parentEvent.categoryName == "Supernova" or op.event.parentEvent.categoryName == "supernova":
            Sheet1.write(x,0,op.teamLeader.user.first_name)
            Sheet1.write(x,1,op.teamLeader.email)
            Sheet1.write(x,2,op.teamLeader.mobileNumber)
            Sheet1.write(x,3,op.teamLeader.college.collegeName)
            Sheet1.write(x,4,op.teamLeader.college.collegeWebsite)
            Sheet1.write(x,5,op.teamLeader.city)
            Sheet1.write(x,6,op.teamName)
            Sheet1.write(x,7,op.event.eventName)
            Sheet1.write(x,8,op.event.parentEvent.categoryName)
            teamMate = op.members.all()
            for tm in teamMate:
                p=p+1
                Sheet1.write(x+p,0,tm.user.first_name)
                Sheet1.write(x+p,1,tm.email)
                Sheet1.write(x+p,2,tm.mobileNumber)
                Sheet1.write(x+p,3,tm.college.collegeName)
                Sheet1.write(x+p,4,tm.college.collegeWebsite)
                Sheet1.write(x+p,5,tm.city)
                Sheet1.write(x+p,6,op.teamName)
                Sheet1.write(x+p,7,op.event.eventName)
                Sheet1.write(x+p,8,op.event.parentEvent.categoryName)

            
            x = x + p + 2
            p = 0

        
    y = 'all_contacts_new.xlsx' 
    wb.save(y)






