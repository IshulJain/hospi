import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
from Auth.views import *
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials


# # use creds to create a client to interact with the Google Drive API
# scope = ['https://spreadsheets.google.com/feeds']
# creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
# client = gspread.authorize(creds)

# # Find a workbook by name and open the first sheet
# # Make sure you use the right name here.
# sheet = client.open("ddetails").sheet1

teams=Team.objects.all()
members=[]
for t in teams:
	m=t.members.all()
	leader=t.teamLeader
	for mem in m:
		members.append(mem)
	
	members.append(leader)
	print(members)
	
	

work=WorkshopTeam.objects.all()
final=[]
for member in members:
	for w in work:
		if member.technexId!=w.teamLeader.technexId:
			final.append(member)


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

	url = "https://script.google.com/a/technex.in/macros/s/AKfycbwIXDuKjAipVNAWj8cjVAQrurLg7nWLU1s7nDCZD41yhSucG4I/exec" #tech@technex.in
	    #url='https://script.google.com/a/technex.in/macros/s/AKfycbykHL9khnVUO0cM_pQ8W7MJ-avy_K8Go8d0K21HRlLFsgR1CrI/exec' #events@technex.in
	    requests.post(url,data=dic)
