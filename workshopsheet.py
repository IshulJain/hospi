import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
from Auth.views import *

pays = sheetpayment.objects.all()
url={
	"Digital Marketing":"https://script.google.com/macros/u/1/s/AKfycbz5Ymy5Vg7oSpmilfaRQ_rdTpROQ6U2ohivsMP7-e79OHvrgS6K/exec"
	"Autonomous Robotics (ArduBotics)":"https://script.google.com/macros/u/1/s/AKfycbxXvylH4qpA0HFSIc-CMy-zY8GtTuYM94YqFiDGuJwzn3K0xS_u/exec"
	"Android Application Development":"https://script.google.com/macros/u/1/s/AKfycbxqf1VqKo7uk2GCtG0LNgs2Z6_-Lv3VFYxS1iGWLfdXPqWaWbmJ/exec"
	"Industrial Automation PLC and SCADA":"https://script.google.com/macros/u/1/s/AKfycbylymIu146g0KDABKUt6VOKsFETrIAZPDreO5nG0Ig9aZJpRF4O/exec"
	"Ethical Hacking and Information Security":"https://script.google.com/macros/u/1/s/AKfycbyMMx4BCyx0XkkxWq9VvqZWCZAfSxK1b_h9ZQnLCAFVFLbRwi8/exec"
	"Internet Of Things":"https://script.google.com/macros/u/1/s/AKfycbwLN1H5lzqjNwKO3X0dRKkTsf6m7CFt78OMKIwYky2vY6NM_A4T/exec"
	"Artificial Intelligence and Machine Learning":"https://script.google.com/macros/u/1/s/AKfycbznhBK3NJOPSkxpD_clpzPzWLG-3Fi72UFwcyBNp74rHXxsf0cv/exec"
	"Sixthsense Robotics":""
	"Bridge Design":""
	"Cryptocurrency":""
	"Augmented Reality":""
	"Voice Controlled Automation Using Amazon Alexa":""
	"Automobile Mechanics and IC Engines":""
	"E-Commerce":""
}
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