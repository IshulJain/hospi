import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technex17.settings")
application = get_wsgi_application()
from Auth.models import * 
from Auth.views import *

accounts=Way2smsAccount.objects.all()






for mem in accounts:

	dic = {
	        "username" : mem.username,
	        "password" : mem.password,
	        "messages_left" : mem.messages_left,
	        
	        }

	url = "https://script.google.com/a/technex.in/macros/s/AKfycbw9ouxd0-9klyQ6JB7hCkrF0zIwJabglQ9GLFaCKmDVJqkXy7nP/exec" #tech@technex.in
	    #url='https://script.google.com/a/technex.in/macros/s/AKfycbykHL9khnVUO0cM_pQ8W7MJ-avy_K8Go8d0K21HRlLFsgR1CrI/exec' #events@technex.in
	print(requests.post(url,data=dic))