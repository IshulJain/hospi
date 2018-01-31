import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
from Auth.views import *



rb = open_workbook('regwithoutpay (2).xlsx')
s = rb.sheet_by_index(0)
for i in range(0,s.nrows):
    email = literal_eval(str(s.cell(i,1)).split(':')[1]).encode("utf-8")
    tp = TechProfile.objects.get(email__iexact = email)
    try:
        sheetpayment.objects.get(tech = tp)
        print("this guy is asshole" + str(tp))
    except:
        pass