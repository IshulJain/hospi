import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
from Auth.views import *

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
	url = "https://script.google.com/a/technex.in/macros/s/AKfycbwVePylbCmmP_8zn5iX51Prw468DtjU-fzlIgNfSHPdS1zw5aTz/exec"
	print(requests.post(url,data=dic))

def fill_teams():
    teams = Team.objects.all()
    for team in teams:
        spreadsheetfill_register(team)