import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("ddetails").sheet1

teams=Team.objects.all()
members=[]
for t in teams:
	m=t.members
	members.append(m)

work=WorkshopTeam.objects.all()
final=[]
for member in members:
	for w in work:
		if member.email!=w.teamName:
			final.append(member)

w = Workbook()
m = 0
sheet1 = w.add_sheet('Sheet1')


