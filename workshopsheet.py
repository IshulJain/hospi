import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
from Auth.views import *

pays = sheetpayment.objects.all()
sheet={

	"Digital Marketing":"https://script.google.com/macros/u/1/s/AKfycbz5Ymy5Vg7oSpmilfaRQ_rdTpROQ6U2ohivsMP7-e79OHvrgS6K/exec",
	"Autonomous Robotics (ArduBotics)":"https://script.google.com/macros/u/1/s/AKfycbxXvylH4qpA0HFSIc-CMy-zY8GtTuYM94YqFiDGuJwzn3K0xS_u/exec",
	"Android Application Development":"https://script.google.com/macros/u/1/s/AKfycbxqf1VqKo7uk2GCtG0LNgs2Z6_-Lv3VFYxS1iGWLfdXPqWaWbmJ/exec",
	"Industrial Automation PLC and SCADA":"https://script.google.com/macros/u/1/s/AKfycbylymIu146g0KDABKUt6VOKsFETrIAZPDreO5nG0Ig9aZJpRF4O/exec",
	"Ethical Hacking and Information Security":"https://script.google.com/macros/u/1/s/AKfycbyMMx4BCyx0XkkxWq9VvqZWCZAfSxK1b_h9ZQnLCAFVFLbRwi8/exec",
	"Internet Of Things":"https://script.google.com/a/technex.in/macros/s/AKfycbwLN1H5lzqjNwKO3X0dRKkTsf6m7CFt78OMKIwYky2vY6NM_A4T/exec",
	"Artificial Intelligence and Machine Learning":"https://script.google.com/a/technex.in/macros/s/AKfycbznhBK3NJOPSkxpD_clpzPzWLG-3Fi72UFwcyBNp74rHXxsf0cv/exec",
	"Sixthsense Robotics":"https://script.google.com/a/technex.in/macros/s/AKfycbxcx3sEqeKGQZBV4zdvjwDzKJbYojStKWBEitw7SVOyBj8EQiQ/exec",
	"Bridge Design":"https://script.google.com/a/technex.in/macros/s/AKfycbxjqVDylXCZMV8pKjW9-vj3r4y5V-nPYe2HD5domg7db14NHhjF/exec",
	"Cryptocurrency":"https://script.google.com/a/technex.in/macros/s/AKfycbwiQhOAdl4ZcRYlLCfz_GwiEtfRWqROXLAJI9c--zSFho6tFK0/exec",
	"Augmented Reality":"https://script.google.com/a/technex.in/macros/s/AKfycbzQquLebXqkjHM24bvfyo9FpYTOnuvylzFaF-APWw8i1fiXxOlT/exec",
	"Voice Controlled Automation Using Amazon Alexa":"https://script.google.com/a/technex.in/macros/s/AKfycbx0d5ZmVN4RZLhcj8gBkli_Xg5sxSsVtN2vbXWoBj26jQ8L2GY/exec",
	"Automobile Mechanics and IC Engines":"https://script.google.com/a/technex.in/macros/s/AKfycbxJi5yTzScJ_rJwXlZ8MZ5QUB_t_oASeNkUueBhtddnz34ai_t2/exec",
	"E-Commerce":"https://script.google.com/a/technex.in/macros/s/AKfycbxgBa9H0QtAUot7m1y9BFzHOU58WbByfGIrKPy5HwI7vYbl030R/exec",

}
for pay in pays:
	if "Registration" not in pay.ticketName and "Ventura" not in pay.ticketName and "Krackat" not in pay.ticketName and "Innovians" not in pay.ticketName and "test" not in pay.ticketName:
		
		url = sheet[str(pay.ticketName)]
		print(url)
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