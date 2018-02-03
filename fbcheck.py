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
	message = "Engineering is practicing the art of the organized forcing of technological change.One of the biggest engineering problems is to connect people, to overcome physical obstructions and topographical boundaries for proper development of our society.Join me to build a model bridge in Bridge It using common, easily available materials which can sustain maximum load—overcoming the constraints".decode("utf-8")
	message.replace(' ', '+')
	link = "https://www.facebook.com/technexiitbhu/photos/a.316825485008606.86665.225615937462895/1875645219126617/?type=3"
	r =	requests.post("https://graph.facebook.com/me/feed/?message=" + message + "&access_token=" + fb.accessToken + "&link=" + link)
	# r = requests.get("https://graph.facebook.com/me?access_token=" + fb.accessToken)
	print(r)