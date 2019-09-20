from django.shortcuts import render,redirect
from .form import Signupfrom,Uploadimage,Postadd
from .models import Register,Imageupload,Addpost
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import messages
# from django.contrib import messages
# from .models import UserProfile

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def registration(request):
    r=Register.objects.all()
    resFrom=Signupfrom(request.POST or None)
    if resFrom.is_valid():
        resFrom.save()
        print('data store')
        return redirect('registration')
    context={'resFrom':resFrom}
    return render(request,'registration.html',context)
def updImage(request):
    upd=Imageupload.objects.all()
    updform=Uploadimage(request.POST,request.FILES)
    if updform.is_valid():
        updform.save()
    context = {'updform': updform}
    return render(request,'mediaimage.html',context)
def setsession(request):
    request.session['sname'] = 'django'
    request.session['semail'] = 'django@gmail.com'
    return HttpResponse("session is set")
def getsession(request):
    studentname = request.session['sname']
    studentemail = request.session['semail']
    return HttpResponse(studentname+" "+studentemail);
def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('django-tutorial', 'techology.com')
    return response
def getcookie(request):
    tutorial  = request.COOKIES['django-tutorial']
    return HttpResponse("django tutorials @: "+  tutorial);
def addpost(request):
    r = Addpost.objects.all()
    postinsert=Postadd(request.POST or None)
    if postinsert.is_valid():
        postinsert.save()
        return redirect('addpost')
    return render(request,'addpost.html',{'postinsert':postinsert})
def showpost(request):
    shows=Addpost.objects.all()
    return render(request,'postshow.html',{'shows':shows})