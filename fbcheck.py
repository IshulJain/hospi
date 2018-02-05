import os
from django.core.wsgi import get_wsgi_application
import requests
import json
import urllib

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import *
from Auth.views import *

fbs = FbReach.objects.all()

urls = [
	"",
]

for fb in fbs:
	message = urllib.quote_plus('#Staytechnexed')
	message.replace(' ', '+')
	for url in urls:
		link = url
		r =	requests.post("https://graph.facebook.com/me/feed/?message=" + message + "&access_token=" + fb.accessToken + "&link=" + link)
		# r = requests.get("https://graph.facebook.com/me?access_token=" + fb.accessToken)
		print(r)