import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import *

for key in uids:
	fb = FbReach.objects.get(uid=uids[key])
	print(fb.accessToken)
	r = requests.post("https://graph.facebook.com/me?access_token=" + fb.accessToken)
	print(r)