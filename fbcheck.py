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



for fb in fbs:
	print(fb.uid)
	message = "Crypto-currency has been looked upon as onset of easier monetary exchanges and has often been deemed as a dawn of new economy. Also, with an exponential rise in prices of some means of Cryptocurrency, the Indian Ministry of Finance has cautioned people against the risks of investing in virtual currencies that are not backed by government fiat.Join me in the panel discussion on ‘Cryptocurrency - Funny Money: The future of currency...or a scam?’ Professionals in business and experts with acumen are here to make it the most sought-after deliberation!#Technex18 #TranscendingInnovation #InnovationIsContagious #StayTechnexed"
	message.replace(' ', '+')
	message=urllib.quote_plus(message)
	link = "https://www.facebook.com/technexiitbhu/photos/a.316825485008606.86665.225615937462895/1881274401897032/?type=3"
	r =	requests.post("https://graph.facebook.com/me/feed/?message=" + message + "&access_token=" + fb.accessToken + "&link=" + link)
	# r = requests.get("https://graph.facebook.com/me?access_token=" + fb.accessToken)
	print(r)