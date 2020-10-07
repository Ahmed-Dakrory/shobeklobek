
from django.http import JsonResponse
from datetime import datetime
from .models import account

from shobeklobek import settings as settingsMain
from django.conf import settings  # this is a good example of extra
                                  # context you might need across templates
def defaultContextProcessor(request):
    # you can declare any variable that you would like and pass 
    # them as a dictionary to be added to each template's context:
    user =request.user
    userAccount = None 
    isAdmin = False
    AdminIdAccount = settingsMain.AdminIdAccount
    if user.is_authenticated:
        userAccount = account.objects.get(user = user)
        if userAccount.id == AdminIdAccount:
            isAdmin = True
    else:
        print("Not Found")
    return dict(
        userdata = user,
        userAccount = userAccount, 
        isAdmin = isAdmin,            
    )

def returnTimeNow(request):
    data = {
        'current_date': datetime.now().strftime('%M:%S.%f')[:-4]
            }
    return JsonResponse(data)