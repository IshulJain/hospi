import os
from django.core.wsgi import get_wsgi_application
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import *
from Auth.views import *

url = "https://script.google.com/a/technex.in/macros/s/AKfycbxrH97fDg5QAzcPpMOyqykBIgs7s8OJJdpFdNBSHVW_5jyEnWu3/exec"
teams = Team.objects.all()

for team in teams:
	memberss = []
	for mem in team.members.all():
		memberss.append(mem)
	memberss.append(team.teamLeader)
	for member in memberss:
		pay = sheetpayment.objects.filter(tech = member)
		if len(pay) == 0 and member.college.collegeWebsite != "190":
			dic = {
				"name": member.user.first_name,
				"technexId":member.technexId,
				"college":member.college,
				"mobileNumber":member.mobileNumber,
				"email":member.email,
			}
			print(requests.post(url,data=dic))
