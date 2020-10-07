from django.shortcuts import render

# Create your views here.
def loadMainPage(request):
    context = {
        'all_accounts_types':None
    }
    
    return render(request,'index.html',context)

def customError400(request, exception):
    return render(request, '400.html')


def customError404(request, exception):
    return render(request, '404.html')


def customError500(request):
    return redirect('http://www.onlydispatch.com')