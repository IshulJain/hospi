import os
from django.core.wsgi import get_wsgi_application
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import *
from Auth.views import *

url = "https://script.google.com/a/technex.in/macros/s/AKfycbybsllkn-T7-FMDB2avLBelNPaUZMCx0G1a7iIUA0TCKYpw8VEV/exec"
teams = WorkshopTeam.objects.all()
memberss = []

for team in teams:
	memberss.append(team.teamLeader)

members = list(set(memberss))

for member in members:
	pay = sheetpayment.objects.filter(tech = member)
	if len(pay) == 0 and member.college.collegeWebsite != "190" and "Registration" not in pays.ticketName and "Ventura" not in pays.ticketName and "Krackat" not in pays.ticketName and "Innovians" not in pays.ticketName and "test" not in pays.ticketName:
		dic = {
			"name": member.user.first_name,
			"technexId":member.technexId,
			"college":member.college,
			"mobileNumber":member.mobileNumber,
			"email":member.email,
		}
		print(requests.post(url,data=dic))



teams = Team.objects.all()
dic={}
total = 1
for team in teams:
	if team.event.nameSlug in dic:
		total = 1 + total
		dic[team.event.nameSlug] = 1 + dic[team.event.nameSlug]
	else:
		
		dic[team.event.nameSlug] = 1

for key in dic:
	print(key + " " + str(dic[key]))

print("total :" + str(total))
