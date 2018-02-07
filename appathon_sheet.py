import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
from Auth.views import *

# def spreadsheetfill_delete(team):
# 	#members = team.members.all()
# 	#print members[0].email.encode("utf-8")
# 	#print members[0].college.collegeName
# 	#for m in team.members.all():
# 	#	members.append(m.email.encode("utf-8"))
# 	dic = {
# 	"teamName":team.teamName,
# 	"leaderEmail":team.teamLeader.email,
# 	"leaderMobile":str(team.teamLeader.mobileNumber),
# 	"leaderCollege":team.teamLeader.college.collegeName,
# 	"teamId":team.technexTeamId,
# 	"teamDelete":1
# 	}
# 	print dic
# 	url = "https://script.google.com/a/technex.in/macros/s/AKfycbwVePylbCmmP_8zn5iX51Prw468DtjU-fzlIgNfSHPdS1zw5aTz/exec"
# 	print(requests.post(url,data=dic))

def fill_teams():
    teams = Team.objects.all()
    for team in teams:
        spreadsheetfill_register(team)

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
	url = "https://script.google.com/a/technex.in/macros/s/AKfycbwVePylbCmmP_8zn5iX51Prw468DtjU-fzlIgNfSHPdS1zw5aTz/exec"
	print(requests.post(url,data=dic))

fill_teams()