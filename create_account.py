import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import *  

def create_account(usernames,password):

	for i in range(0,36):
		ac=Way2smsAccount.objects.filter(username=username)

		if len(ac)==0:

			a=Way2smsAccount()
			a.username=usernames[i]
			a.password=password[i]
			a.save()
		else:
			print(username+ "already there")

import xlrd
file_location="way2sms contacts.xlsx"
workbook=xlrd.open_workbook(file_location) 
sheet=workbook.sheet_by_index(0)
username=[sheet.cell_value(r,0) for r in range(0,36)]
usernames = [chr(n) for n in username]

password=[sheet.cell_value(r,1) for r in range(0,36)]
create_account(usernames,password)
