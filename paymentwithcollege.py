import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
from Auth.views import *


pay = sheetpayment.objects.all()
p=pay[0]
for pro in p:
    print(pro)
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

    # url = "https://script.google.com/a/technex.in/macros/s/AKfycbxX16VxFckPcIaZ5sr0Yjmy9-LPymm8nwXOhMN62aLbirltmt3i/exec" #tech@technex.in
    # #url='https://script.google.com/a/technex.in/macros/s/AKfycbykHL9khnVUO0cM_pQ8W7MJ-avy_K8Go8d0K21HRlLFsgR1CrI/exec' #events@technex.in
    # print(requests.post(url,data=dic))
