import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
from Auth.views import *

techp=TechProfile.objects.all()
teams=Team.objects.all()
workshopteams=WorkshopTeam.objects.all()

members=[]
for team in teams:
	team_members=team.members.all()
	# print(m)
	leader=team.teamLeader
	# print(leader)
	for mem in team_members:
		members.append(mem)
	members.append(leader)
memberss=list(set(members))

workmem=[]
for workshopteam in workshopteams:
	workmem.append(workshopteam.teamLeader)
workmems=list(set(workmem))

total_reg=workmems+memberss
total_reg=list(set(total_reg))


no_reg = [x for x in techp if x not in total_reg]
final=[]
for no_regobj in no_reg:
	pays = sheetpayment.objects.filter(tech = no_reg)
	print pays
	if len(pays) == 0 and not no_reg.college.collegeWebsite == "190":
		final.append(no_regobj)	
		print no_regobj.user.first_name

for mem in final:

	dic = {
	        "name" : mem.user.first_name,
	        "email" : mem.email,
	        "college" : mem.college.collegeName,
	        "technexId" : mem.technexId,
	        "year" : mem.year,
	        "mobileNumber" : mem.mobileNumber,
	        "city" : mem.city,
	        }

	url = "https://script.google.com/a/technex.in/macros/s/AKfycbwx8RQasAIvjEIy-ewy9maEgdMWYWxiKCoD4GE0rX_RgUf1vFHb/exec" #tech@technex.in
	    #url='https://script.google.com/a/technex.in/macros/s/AKfycbykHL9khnVUO0cM_pQ8W7MJ-avy_K8Go8d0K21HRlLFsgR1CrI/exec' #events@technex.in
	print(requests.post(url,data=dic))