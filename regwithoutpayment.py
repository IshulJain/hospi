import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
from Auth.views import *



# rb = open_workbook('reg_withoutanything.xlsx')
# s = rb.sheet_by_index(0)
# for i in range(0,s.nrows):
#     email = literal_eval(str(s.cell(i,1)).split(':')[1]).encode("utf-8")
#     tp = TechProfile.objects.filter(email = email)
#     try:
#         try:
#             pay = sheetpayment.objects.get(tech = tp[0])
#         except:
#             pay = sheetpayment.objects.get(tech = tp)
#         print(pay.tech.technexId)
#         print(pay.tech.email)
#         print(pay.email)
#         print("this guy is asshole" + str(tp))
#     except:
#         pass
techp=TechProfile.objects.all()
teams=Team.objects.all()
workshopteams=WorkshopTeam.objects.all()

members=[]
for team in teams:
    team_members=team.members.all()
    # print(m)
    leader=team.teamLeader
    # print(leader)
    for mem in team_members:
        members.append(mem)
    members.append(leader)
memberss=list(set(members))

workmem=[]
for workshopteam in workshopteams:
    workmem.append(workshopteam.teamLeader)
workmems=list(set(workmem))

total_reg=workmems+memberss
total_reg=list(set(total_reg))


rb = open_workbook('reg_withoutanything.xlsx')
s = rb.sheet_by_index(0)
for i in range(0,s.nrows):
    email = literal_eval(str(s.cell(i,1)).split(':')[1]).encode("utf-8")
    tp = TechProfile.objects.filter(email = email)
    if tp not in total_reg:
        pass
    else:
        print(pay.tech.technexId)
        print(pay.tech.email)
        print(pay.email)
        print("this guy is asshole" + str(tp))




        