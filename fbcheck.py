import os
from django.core.wsgi import get_wsgi_application
import requests


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import *
uids = [
	"267878550314239",
	"262478540838588",
	"504963769904268",
	"239318923163037",
	"1005882789524032",
	"1404873316198342",
	"1318732261583267",
	"176995352901981",
	"911733435670846",
	"1164981566894151",
	"727824143975425",
	"1122338601179430",
	"1498440296941600",
]
for key in range(0,len(uids)-1):
	fb = FbReach.objects.get(uid=uids[key])
	print(fb.accessToken)
	r = requests.post("https://graph.facebook.com/me?access_token=" + fb.accessToken)
	print(r.text)