import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
from Auth.views import *
techp=TechProfile.objects.all()
pay = sheetpayment.objects.all()
final=[]
for t in techp:
	c=0
	for p in pay:
		if t==p.tech:
			c==1
			break

	if c==0:
		final.append(t)

print(final[:5])

for mem in final:

	dic = {
	        "name" : mem.user.first_name,
	        "email" : mem.email,
	        "college" : mem.college.collegeName,
	        "technexId" : mem.technexId,
	        "year" : mem.year,
	        "mobileNumber" : mem.mobileNumber,
	        "city" : mem.city
	        }

	url = "https://script.google.com/a/technex.in/macros/s/AKfycbwgg6rfk29Yhenn4zSNqc_2lSrciVMM3ixqbpS_9cQkSNvPzl0/exec" #tech@technex.in
	    #url='https://script.google.com/a/technex.in/macros/s/AKfycbykHL9khnVUO0cM_pQ8W7MJ-avy_K8Go8d0K21HRlLFsgR1CrI/exec' #events@technex.in
	print(requests.post(url,data=dic))



