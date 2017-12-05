import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import *  


def college_data(names,ids,cities,states):
    for i in range(1,575):
        a=College()
        a.collegeName=names[i]
        a.city=cities[i]
        a.state=states[i]
        a.status=True
        a.collegeWebsite=ids[i]
        a.save()


import xlrd
file_location="college-list.xlsx"
workbook=xlrd.open_workbook(file_location) 
sheet=workbook.sheet_by_index(0)
name=[sheet.cell_value(r,1) for r in range(0,575)]
ids=[sheet.cell_value(r,2) for r in range(0,575)]
ids=map(int, ids)
city=[sheet.cell_value(r,4) for r in range(0,575)]
state=[sheet.cell_value(r,5) for r in range(0,575)]
college_data(name,ids,city,state)
