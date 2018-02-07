import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
from Auth.views import *

# teams = Team.objects.all()
# dic={}
# for team in teams:
# 	if team.event.nameSlug in dic:
# 		dic[team.event.nameSlug] = 1 + dic[team.event.nameSlug]
# 	else:
# 		dic[team.event.nameSlug] = 1

# for key in dic:
# 	print(key + " " + str(dic[key])) 


def fill_teams():
	teams = Team.objects.all()
	for team in teams:
		if team.event.nameSlug=="appathon":
			
	
			spreadsheetfill_register(team)

def spreadsheetfill_register(team):
	members = team.members.all()
	#print members[0].email.encode("utf-8")
	#print members[0].college.collegeName
	#for m in team.members.all():
	#	members.append(m.email.encode("utf-8"))
	if team.event.nameSlug=="appathon":
		dic = {
		"teamName":team.teamName,
		"leaderEmail":team.teamLeader.email,
		"leaderMobile":str(team.teamLeader.mobileNumber),
		"leaderCollege":team.teamLeader.college.collegeName,
		"leaderName" :  team.teamLeader.user.first_name,
		"teamId":team.technexTeamId
		}
		try:
			dic['member1'] = members[0].email.encode("utf-8")
			dic['college1'] = members[0].college.collegeName 
			dic['mobile1'] = members[0].mobileNumber
			dic['name1'] = members[0].user.first_name
		except:
			dic['member1'] = 0
			dic['college1'] = 0
			dic['mobile1'] = 0
			dic['name1'] = 0
		try:
			dic['member2'] = members[1].email.encode("utf-8")
			dic['college2'] = members[1].college.collegeName
			dic['mobile2'] = members[1].mobileNumber
			dic['name2'] = members[1].user.first_name
		except:
			dic['member2'] = 0
			dic['college2'] = 0
			dic['mobile2'] = 0
			dic['name2'] = 0
		try:
			dic['member3'] = members[2].email.encode("utf-8")
			dic['college3'] = members[2].college.collegeName
			dic['mobile3'] = members[2].mobileNumber
			dic['name3'] = members[2].user.first_name
		except:
			dic['member3'] = 0
			dic['college3'] = 0
			dic['mobile3'] = 0
			dic['name3'] = 0
		try:
			dic['member4'] = members[3].email.encode("utf-8")
			dic['college4'] = members[3].college.collegeName
			dic['mobile4'] = members[3].mobileNumber
			dic['name4'] = members[3].user.first_name
		except:
			dic['member4'] = 0
			dic['college4'] = 0
			dic['mobile4'] = 0
			dic['name4'] = 0
		# print dic
		if team.members.all().count()==4:
			url = "https://script.google.com/a/technex.in/macros/s/AKfycbyt8pRm_MEs6uW_DCRD2uxGhUt2guofhP2_b2lNKUBfxau9sPs/exec"
			
		else:
			url = "https://script.google.com/a/technex.in/macros/s/AKfycbwVePylbCmmP_8zn5iX51Prw468DtjU-fzlIgNfSHPdS1zw5aTz/exec"
		print(requests.post(url,data=dic))

fill_teams()