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
# import facebook
from Auth.models import *
from Auth.views import contextCall,send_email,send_sms_single

server = "http://www.technex.in/"
sheetUrls = {
	#Robonex
	"robowars":"https://script.google.com/a/technex.in/macros/s/AKfycbzxGmuCC-cVEHecvxM8IoctqxjuRjpSpa8r4qO8GLOlx4kgEKQ/exec", #Updated
	"pixelate":"https://script.google.com/a/technex.in/macros/s/AKfycbyj84WzvkzGgwe65KWrGrs7OvkpRjtMcwH6Ql4cV4JXu8yG0-WM/exec", #Updated
	"hurdlemania":"https://script.google.com/a/technex.in/macros/s/AKfycbyk6Q2cVW8amUdgSayqSxHKF9wUiXJMvt7pwFxaP-Wzm6aZwKJY/exec", #Updated
	"mazexplorer":"https://script.google.com/a/technex.in/macros/s/AKfycbzHY2kN1hsH8zWUx2LFy1TuIr0D_P-CB7Res2BgbYr8UBTVZTM/exec", #Updated
	#
	"open-software" : "https://script.google.com/macros/s/AKfycbxQeVLQzJ-l0HGdrovmvKRfStBmmrXzJlk5detmE6N037BzBAc6/exec",
	"open-hardware": "https://script.google.com/macros/s/AKfycbwE6p7LyUHApX7oTnsmiR-Vk_Q2x1YJQd5fYcfn9bTjfLq35Wg/exec",
	"green-tech": "https://script.google.com/macros/s/AKfycbxPWMx8KBwuNLcBeG23QCaZX7FJ5lOAjStMxQ15S4z57X2xEUQ/exec",
	#Byte-The-Bits
	"capture-the-flag" : "https://script.google.com/a/technex.in/macros/s/AKfycbz5LqfYQpbor-tepRlu471FH_bmXlQKbdkbQcONy0EQ0jMXO_M/exec", #Updated
	"appathon": "https://script.google.com/a/technex.in/macros/s/AKfycbxDM9__ELb9gDK-N7V_USeFfl0f6vNJTAR0EqgAzls0T2VQKkHZ/exec", #Updated
	"international-coding-marathon": "https://script.google.com/a/technex.in/macros/s/AKfycbz4IN_Lfpm0w7UWDJ83XlNhRnxXvnjL6k8kSqvj5ykgBhA3bPWe/exec", #Updated
	"mlware": "https://script.google.com/macros/s/AKfycbwfyM7gZ26iI17kQslhnw_1G_621t-XeDeuY8LBBcXiqN8ELHi_/exec",
	#Modex
	"modex" : "https://script.google.com/a/technex.in/macros/s/AKfycbwfziSXf-XUjwqXJybC8gGS72m0Wg-k3V4Do2JCoK4VNdn-rBE8/exec", #Updated (NEW)
	#Riqueza
	"economists-enigma": "https://script.google.com/a/technex.in/macros/s/AKfycbzTKcMBoQUL0o6kNtSECX8luZ2wAc3SFyv87Z6NC_lRfhZdKCs/exec", #Updated
	"manthan": "https://script.google.com/a/technex.in/macros/s/AKfycbwZonmT5tptNSEZpMWumK0P5e1GkNseGopiqY0eQQIDm_mbcDA/exec", #Updated
	"krackat": "https://script.google.com/a/technex.in/macros/s/AKfycbw9i2x2Upud6lw3zSEJZpGslYhclWEPoGMWu-solSAou4I7ny8/exec", #Updated
	"bulls-floor": "https://script.google.com/a/technex.in/macros/s/AKfycbx4tEAIoBe2yWy3cUN_hE7f6JW6HcGAjDbk7sifisnpoJt_djo/exec", #Updated
	"analiticity": "https://script.google.com/a/technex.in/macros/s/AKfycbwjXQ4hhWgON8oWMTeCpEMsIup_YPlouuoUqyiv__ufc5g5uQU-/exec", #Updated
	#Creatrix
	"2d":"https://script.google.com/macros/s/AKfycbwf1qvqJwVLgRNnD_JhZROI2r2AIrlOrTlxRAzAWRccS5pQerY/exec",
	"animaze":"https://script.google.com/macros/s/AKfycbxS-q0nnu3BfadEq-QWU_KuR8v2FMk5Ji40Y3gBDHGmZ_E9n_s/exec",
	"avant-garde":"https://script.google.com/macros/s/AKfycbzbMnYK0LUapV-62CKM3GrA61z8nEmPzJDnhbtUY2cXgQGX5vU/exec",
	"iso":"https://script.google.com/macros/s/AKfycbxM9pEcYkjnFKMVWoRCAy_HayzgLuxaXDDD-ccGGkCi_Qgz2xw/exec",
	"collage":"https://script.google.com/macros/s/AKfycbx-ElC8fhlP5h2lZucFVF01BzdMaPMW6GrsHfotZGYg-SOs_4Gj/exec",
	"minimize":"https://script.google.com/macros/s/AKfycbwYTV5c6Yw5MRy1OxII-U6A78YsWz_iNqFqIzlS_eb6NJ408tY/exec",
	#Supernova
	"exploring-interstellar":"https://script.google.com/a/technex.in/macros/s/AKfycbx0UoFd5lOjt0wUXWG4zkrmflUM0EIbFz5_n-BSUmBL_tNmdu4/exec", #Updated
	"astroquiz":"https://script.google.com/a/technex.in/macros/s/AKfycbwd_Q6vy_EVp0_mpsQlczzNyfclXtIMj8VPwG0-nd6adO9T3gLC/exec", #Updated
	"astrophotography":"https://script.google.com/a/technex.in/macros/s/AKfycbzYQmzwtPGLjXewjOUrXzbtgk2yUKGZRV5hAtC_Xi3rdNzh-FTv/exec", #Updated
	"scientists-utopia":"https://script.google.com/a/technex.in/macros/s/AKfycbwtvaYhFdCRFBC6P-81wz087gY2no1Qg6ypARkjT_FHTdyzYwtx/exec", #Updated
	#Pahal
	"aagaz":"https://script.google.com/a/technex.in/macros/s/AKfycbywznIjTwBSYK3QLNHeCaCeXd19_y9B3Scxi6KrKocip4kq5piP/exec", #Updated
	"sampann":"https://script.google.com/a/technex.in/macros/s/AKfycbxn2wNywiG6Zi4yqjVI2XryLkKBisvdXa7AC0RhrOLxQvUk1p4/exec", #Updated
	"swachch":"https://script.google.com/macros/s/AKfycbyiLuidIIPe8q1Cc2JRctAYg7GuTb0ilRdB2U288cC6kgQcGFQF/exec",
	"vision":"https://script.google.com/macros/s/AKfycbynUPef4u0AqxuGIaR_0_m35Ry6-KipzRkkQngaGjuTSuPupAU/exec",
	"greenx":"https://script.google.com/a/technex.in/macros/s/AKfycbxid8faLDNZguA_u-fjAlwV_wXy1jJtdbVqWWGYCS1Fw9VJo0c/exec", #Updated
	"saksham" : "https://script.google.com/a/technex.in/macros/s/AKfycbyi-O51gnbwMu4EQrH6i_E-9egJBTtEXLIowIK5LO7_onXbWCqK/exec", #Updated (NEW)
	"vikalp" : "https://script.google.com/a/technex.in/macros/s/AKfycbyvux0-8B8uE2a6uN-o9F-Nd3S0VI4_qCgwl3xPBVzuUBLkWOs/exec", #Updated (NEW)
	#Ascension
	"drone-tech": "https://script.google.com/a/technex.in/macros/s/AKfycbxW3Sh25DzIT8_Akg6yrWIO4GAJSR2LT_i5FRzsCiRrqlOJ-gJo/exec", #Updated
	"daeroglisseur": "https://script.google.com/a/technex.in/macros/s/AKfycbxtfBt1ytJFysy0br719IP8lUTNheAGU6GilmPXknBnDt2L3rw/exec", #Updated
	"la-trajectoire":"https://script.google.com/a/technex.in/macros/s/AKfycbwOqjMYTF8uQPI_lbtzDZuRDw73GU6v5zr0BxQpu2lAJbk-RnPG/exec", #Updated
	"momentum":"https://script.google.com/a/technex.in/macros/s/AKfycbwtxdtodY8WUmM01IQGD8rJuO7XXwE8Q__9gbFzLF5epghZTQ8/exec", #Updated
	#Extreme-Engineering
	"axelerate": "https://script.google.com/a/technex.in/macros/s/AKfycbyDiFjest66TfNsRlVjQNU5YbMY0DKUf56v8ryu-DqXVTRzi_Q/exec", #Updated
	"goldbergs-alley": "https://script.google.com/a/technex.in/macros/s/AKfycbwoGV_VrDOueYNobdte9AH_mmb7UmpdIorACwMeapDm0pr6Eo0h/exec", #Updated
	"bridgeit": "https://script.google.com/a/technex.in/macros/s/AKfycbw04ckemnWPfGIPn40X0MQroRc7uRX7CLicqcpMm8w-zyu-pgY/exec", #Updated
	"hydracs": "https://script.google.com/a/technex.in/macros/s/AKfycbw9TQ5PY8dG8ucZqiMeM5WH7PPKIfAMkyzfnrZczeiHcpAFh0g/exec", #Updated
	#Game-Dungeon
	"cs-go" : "https://script.google.com/macros/s/AKfycbz2rizF0A3Ok97_nMSTnUA9oekEG4fNUrpIOb0ovNS6TgNDr6Dz/exec",
	#Dih-Design-Contest
	"classroom-furniture" : "https://script.google.com/macros/s/AKfycbyD1yAphlQUv1qVFlsj325iQvhvvJUkwMTs4pR79hkCG-JcTZDH/exec",
	"classroom-cooling" : "https://script.google.com/macros/s/AKfycbx2y0dAhHHaH97HWYmdQuVUyYYgYF8MhKXCQqbWgVWS2-p_lGc/exec",
	"classroom-sound-absorber" : "https://script.google.com/macros/s/AKfycbxFS5uSJPrrVZPTVNSsiuGvFPdjlcVFCZQkv1Ht9cHmFxokK2zi/exec",
	"hostel-room-furniture": "https://script.google.com/macros/s/AKfycbwImpuQnhpOsHN98KqYCDQj0HGD3z_TpTjEKU_90v_6t7E03Gw/exec",
	"mess-furniture": "https://script.google.com/macros/s/AKfycbx25ucmWGPX4LGcwSDhTcobu8EX9ZsWqokB0kq-D8qVgRlRvtpO/exec",





}

@csrf_exempt
def eventRegistration(request):
	response = {}
     
	if request.method == 'POST':
		data = json.loads(request.body)
		print data
		event = Event.objects.get(nameSlug = data['eventSlug'])
		print "here"
		try:
			# print "here"
			team = Team.objects.get(teamName = data['teamName'], event = event)
			response['status'] = 0
			response['error'] = "TeamName Already exists"
			return JsonResponse(response)
		except:
			try:
				teamLeader = TechProfile.objects.get(technexId = data['teamLeaderEmail'])
			except:
				teamLeader = TechProfile.objects.get(email = data['teamLeaderEmail'])
			users = []
			# print "here"
			for member in data['members']:
				try:	
					try:
						user = TechProfile.objects.get(email = member)
						users.append(user)
					except:
						user = TechProfile.objects.get(technexId = member)
						users.append(user)
				except:
					response['status'] = 0
					response['error'] = 'Member not Registered('+member+')'
					return JsonResponse(response)
				
			users = list(set(users))
			try:
				try:
					team = Team.objects.get(teamLeader = teamLeader,event = event)
					response['status'] = 0
					response['error'] = 'You have Already registered for this event!!'
					return JsonResponse(response)
				except:
					team = Team.objects.get(event = event, members = teamLeader)
					response['status'] = 0
					response['error'] = 'You have Already registered for this event !!'
			except:
				for u in users: 
					try:
						try:
							team = Team.objects.get(event = event, members = u)
							response['status'] = 0
							response['error'] = u.email+' Already registered for this event !!!'
							return JsonResponse(response)
						except:
							team = Team.objects.get(event = event, teamLeader = u)
							response['status'] = 0
							response['error'] = u.email+' Already registered for this event !!!'
							return JsonResponse(response)
					except:
						try:
							if teamLeader == u:
								users.remove(u)
						except:
							pass
				team = Team(teamLeader = teamLeader,event = event, teamName = data['teamName'])
				team.save()
				team.technexTeamId = "TM"+str(1000+team.teamId)
				team.save()
			subject = "[Technex'18] Successful Registration"
			body = '''
Dear %s,

Thanks for registering for %s Technex'18.

Your Team Details Are
Team Name- %s
Team Leader- %s
Team Members- %s


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
				team.members.add(user)
			send_email(teamLeader.email,subject,body%(teamLeader.user.first_name,event.eventName.capitalize(),team.teamName,teamLeader.email,memberEmails))
			message=" Team Registration successful for team name "+ str(team.teamName) + " . Visit www.fb.com/technex for updates. \nRegards\nTeam Technex"
			# send_sms_single(message,str(teamLeader.mobileNumber))
			for user in users:
				send_email(user.email,subject,body%(user.user.first_name,event.eventName.capitalize(),team.teamName,teamLeader.email,memberEmails))
			response['status'] = 1
			spreadsheetfill_register(team)
			return JsonResponse(response)
	else:
		response['status'] = 0
		return render(request, 'eventRegistration.html',contextCall(request))
		#return JsonResponse(response)


def teamLeave(request):
	response = {}
	if request.method == 'POST':
		data = request.POST #json.loads(request.body)
		print data
        try:
        	team = Team.objects.get(teamId = data['identifier'])
        	team.members.remove(request.user.techprofile)
        	response['status'] = 1
        except:
        	response['status'] = 0
		return JsonResponse(response)
	else:
		response['status'] = 0
		response['error'] = 'Invalid request'
		return JsonResponse(response)

@csrf_exempt
def teamDelete(request):
	response = {}
	if request.method == 'POST':
		data = json.loads(request.body)
		if 1:#try:
			print data['identifier']
			team = Team.objects.get(teamLeader = request.user.techprofile,technexTeamId = data['identifier'])
			spreadsheetfill_delete(team)
			send_email("events@technex.in","Team Delete Mail",str(str(team.technexTeamId)+"  "+team.event.eventName+"  "+team.teamName))
			team.delete()
			response['status'] = 1
		else:#except:
			response['status'] = 0
		return JsonResponse(response)
	else:
		response['status'] = 0
		response['error'] = 'Invalid request'			
		return JsonResponse(response)

def memberDelete(request):
	response = {}
	if request.method == 'POST':
		data = request.POST
		if True:
			member = TechProfile.objects.get(email = data['identifier'])
			team = Team.objects.get(teamLeader = request.user.techprofile, teamId = data['teamId'])
			team.members.remove(member)
			response['status'] = 1
		else:
			response['status'] = 0
		return JsonResponse(response)
	else:
		response['status'] = 0
		response['error'] = 'Invalid request'
		return JsonResponse(response)

#@login_required('/')
def event(request):
	if request.method == 'POST':
		print request.POST['members']
		return HttpResponse(request.body)
	else:
		return render(request, 'eventRegistration.html')


def spreadsheetfill_register(team):
	members = team.members.all()
	#print members[0].email.encode("utf-8")
	#print members[0].college.collegeName
	#for m in team.members.all():
	#	members.append(m.email.encode("utf-8"))
	dic = {
	"teamName":team.teamName,
	"leaderEmail":team.teamLeader.email,
	"leaderMobile":str(team.teamLeader.mobileNumber),
	"leaderCollege":team.teamLeader.college.collegeName,
	"teamId":team.technexTeamId
	}
	try:
		dic['member1'] = members[0].email.encode("utf-8")
		dic['college1'] = members[0].college.collegeName 
		dic['mobile1'] = members[0].mobileNumber
	except:
		dic['member1'] = 0
		dic['college1'] = 0
		dic['mobile1'] = 0
	try:
		dic['member2'] = members[1].email.encode("utf-8")
		dic['college2'] = members[1].college.collegeName
		dic['mobile2'] = members[1].mobileNumber
	except:
		dic['member2'] = 0
		dic['college2'] = 0
		dic['mobile2'] = 0
	try:
		dic['member3'] = members[2].email.encode("utf-8")
		dic['college3'] = members[2].college.collegeName
		dic['mobile3'] = members[2].mobileNumber
	except:
		dic['member3'] = 0
		dic['college3'] = 0
		dic['mobile3'] = 0
	try:
		dic['member4'] = members[3].email.encode("utf-8")
		dic['college4'] = members[3].college.collegeName
		dic['mobile4'] = members[3].mobileNumber
	except:
		dic['member4'] = 0
		dic['college4'] = 0
		dic['mobile4'] = 0
	print dic
	url = sheetUrls[team.event.nameSlug.encode("utf-8")]
	requests.post(url,data=dic)
 	
def spreadsheetfill_delete(team):
	#members = team.members.all()
	#print members[0].email.encode("utf-8")
	#print members[0].college.collegeName
	#for m in team.members.all():
	#	members.append(m.email.encode("utf-8"))
	dic = {
	"teamName":team.teamName,
	"leaderEmail":team.teamLeader.email,
	"leaderMobile":str(team.teamLeader.mobileNumber),
	"leaderCollege":team.teamLeader.college.collegeName,
	"teamId":team.technexTeamId,
	"teamDelete":1
	}
	print dic
	url = sheetUrls[team.event.nameSlug.encode("utf-8")]
	requests.post(url,data=dic)
