import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
from Auth.views import *

teams=Team.objects.all()

for team in teams:
	members=[]
	team_members=team.members.all()
	event=team.event
	# print(m)
	leader=team.teamLeader
	# print(leader)
	for mem in team_members:
		members.append(mem)
	members.append(leader)

	for member in members:
		final=[]
		pays = sheetpayment.objects.filter(tech = member)
		if len(pays) == 0 and not member.college.collegeWebsite == "190":
			final.append(member)	
			print member.user.first_name
		if len(final) != 0:
			print(member.email)
			print(team.event)




			# for mem in final:
			# 	dic = {
	  #       "name" : mem.user.first_name,
	  #       "email" : mem.email,
	  #       "college" : mem.college.collegeName,
	  #       "technexId" : mem.technexId,
	  #       "year" : mem.year,
	  #       "mobileNumber" : mem.mobileNumber,
	  #       "city" : mem.city,
	  #       "events":event
	  #       }

			# url = "https://script.google.com/a/technex.in/macros/s/AKfycbwx8RQasAIvjEIy-ewy9maEgdMWYWxiKCoD4GE0rX_RgUf1vFHb/exec" #tech@technex.in
			    #url='https://script.google.com/a/technex.in/macros/s/AKfycbykHL9khnVUO0cM_pQ8W7MJ-avy_K8Go8d0K21HRlLFsgR1CrI/exec' #events@technex.in
			# print(requests.post(url,data=dic))


# memberss=list(set(members))

# workmem=[]
# for workshopteam in workshopteams:
# 	workmem.append(workshopteam.teamLeader)
# workmems=list(set(workmem))

# total_reg=workmems+memberss
# total_reg=list(set(total_reg))


# no_reg = [x for x in techp if x not in total_reg]
# final=[]
# for member in memberss:
# 	pays = sheetpayment.objects.filter(tech = member)
# 	# print pays
# 	if len(pays) == 0 and not member.college.collegeWebsite == "190":
# 		final.append(member)	
# 		print member.user.first_name

# for mem in final:
# 	events=mem.event
# 	print events
# 	print("next")

	# dic = {
	#         "name" : mem.user.first_name,
	#         "email" : mem.email,
	#         "college" : mem.college.collegeName,
	#         "technexId" : mem.technexId,
	#         "year" : mem.year,
	#         "mobileNumber" : mem.mobileNumber,
	#         "city" : mem.city,
	#         "events":mem
	#         }

	# url = "https://script.google.com/a/technex.in/macros/s/AKfycbwx8RQasAIvjEIy-ewy9maEgdMWYWxiKCoD4GE0rX_RgUf1vFHb/exec" #tech@technex.in
	#     #url='https://script.google.com/a/technex.in/macros/s/AKfycbykHL9khnVUO0cM_pQ8W7MJ-avy_K8Go8d0K21HRlLFsgR1CrI/exec' #events@technex.in
	# print(requests.post(url,data=dic))
