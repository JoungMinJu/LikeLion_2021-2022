from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request,'main/mainpage.html')

def showsecond(request):
    return render(request, 'main/second.html')

def showfirst(request):
    return render(request,'main/first.html')
