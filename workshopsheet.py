import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
from Auth.views import *

pays = sheetpayment.objects.all()

for pay in pays:
    if "Registration" in pay.ticketName and "Ventura" not in pay.ticketName and "Kracket" not in pay.ticketName and "Innovians" not in pay.ticketName:
    	
    	url = sheet[pay.ticketName]

		dic = {
	        "name" : pay.tech.user.first_name,
	        "email" : pay.email,
	        "technexId" : pay.tech.technexId,
	        "College" : pay.tech.college,
	        "ticketName" : pay.ticketName,
	        "ticketId" : pay.ticketId,
	        "ticketprice" : pay.ticketPrice,
	        "registeredOn" : pay.timeStamp,
	        }

	    print(requests.post(url,data=dic))