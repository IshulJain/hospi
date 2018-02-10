# import os
# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
# application = get_wsgi_application()
# from Auth.views import paymentdata

# paymentdata()


import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.views import *

payment = sheetpayment.objects.all()
url = "https://script.google.com/a/technex.in/macros/s/AKfycbzi_JDir9HH9GWY6L6qZrL96CnytEcDyzR9t_M060mh7M5n7IY/exec"
for pro in payment:
	if pro.row > 2554:
		dic = {
		"name" : pro.tech.user.first_name,
		"email" : pro.email,
		"technexId" : pro.tech.technexId,
		"College" : pro.tech.college,
		"ticketName" : pro.ticketName,
		"ticketId" : pro.ticketId,
		"ticketprice" : pro.ticketPrice,
		"registeredOn" : pro.timeStamp,
		}
		print(requests.post(url,data=dic))
