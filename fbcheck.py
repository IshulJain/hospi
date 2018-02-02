import os
from django.core.wsgi import get_wsgi_application
import requests
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import *
from Auth.views import *

fbs = FbReach.objects.all()



for fb in fbs:
	print(fb.uid)
	message = "Technex in partnership with Samsung Research Institute Bangalore presents Hackathon wherein you will get to solve problems which developers face"
	message.replace(' ', '+')
	link = "https://www.facebook.com/technexiitbhu/photos/a.316825485008606.86665.225615937462895/1904778652879940/?type=3"
	r =	requests.post("https://graph.facebook.com/me/feed/?message=" + message + "&access_token=" + fb.accessToken + "&link=" + link)
	# r = requests.get("https://graph.facebook.com/me?access_token=" + fb.accessToken)
	print(r)