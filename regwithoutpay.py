import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
from Auth.views import *
# techp=TechProfile.objects.all()
# pay = sheetpayment.objects.all()
# final=[]
# for t in techp:
# 	c=0
# 	for p in pay:
# 		if t==p.tech:
# 			c==1
# 			break

# 	if c==0:
# 		final.append(t)

# print(final[:5])

teams=Team.objects.all()
members=[]
for t in teams:
	m=t.members.all()
	# print(m)
	leader=t.teamLeader
	# print(leader)
	for mem in m:
		members.append(mem)
	
	members.append(leader)
	# print(members)

memberss=list(set(members))

work=WorkshopTeam.objects.all()
workmem=[]
for w in work:
	workmem.append(w.teamLeader)

workmems=list(set(workmem))
techp=workmems+memberss
techp=list(set(techp))

pay = sheetpayment.objects.all()
final=[]
# for t in techp:
# 	c=0
# 	for p in pay:
# 		if t==p.tech:
# 			c==1
# 			break

# 	if c==0:
# 		final.append(t)
for techpobj in techp:
	pays = sheetpayment.objects.filter(tech = techpobj)
	print pays
	if len(pays) == 0 and not techpobj.college.collegeWebsite == "190":
		final.append(techpobj)	
		print techpobj.user.first_name

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

	url = "https://script.google.com/a/technex.in/macros/s/AKfycbxMmNuFsjqR5UZvhDg9UthvB8dUr61KGilCa1U9M_NGjUhx9qA/exec" #tech@technex.in
	    #url='https://script.google.com/a/technex.in/macros/s/AKfycbykHL9khnVUO0cM_pQ8W7MJ-avy_K8Go8d0K21HRlLFsgR1CrI/exec' #events@technex.in
	print(requests.post(url,data=dic))



