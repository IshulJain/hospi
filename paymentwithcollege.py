import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
from Auth.views import *


pay = sheetpayment.objects.all()
for pro in pay:
    
    dic = {
        "name" : pro.tech.user.first_name,
        "email" : pro.email,
        "technexId" : pro.tech.technexId,
        "College" : pro.tech.college,
        "Ticket Name" : pro.ticketName,
        "Ticket Id" : pro.ticketId,
        "Ticket Price" : pro.ticketPrice,
        "Registered On" : pro.timeStamp,
        }

    url = "https://script.google.com/a/technex.in/macros/s/AKfycbwIXDuKjAipVNAWj8cjVAQrurLg7nWLU1s7nDCZD41yhSucG4I/exec" #tech@technex.in
    #url='https://script.google.com/a/technex.in/macros/s/AKfycbykHL9khnVUO0cM_pQ8W7MJ-avy_K8Go8d0K21HRlLFsgR1CrI/exec' #events@technex.in
    requests.post(url,data=dic)
