from django.shortcuts import render
from KAMIKAZEEVENTMNG.models import Ureg
from django.http import HttpResponse

# Create your views here.
def hi(request):
    if request.method== 'POST':
        if request.POST.get('name') and request.POST.get('uname') and request.POST.get('email') and request.POST.get('phno') and request.POST.get('pswd') and request.POST.get('cpswd'):
         saverecord=Ureg()
        saverecord.name=request.POST.get('name')
        saverecord.uname=request.POST.get('uname')
        saverecord.email=request.POST.get('email')
        saverecord.phno=request.POST.get('phno')
        saverecord.pswd=request.POST.get('pswd')
        saverecord.cpswd=request.POST.get('cpswd')
        saverecord.save()
    else:
        return render(request,'KAMIKAZEEVENTMNG/usersignup.html')

def login(request):
    return  render(request,'KAMIKAZEEVENTMNG/userlogin.html')
def signup(request):
    return render(request,'KAMIKAZEEVENTMNG/usersignup.html')
def home(request):
    return render(request,'KAMIKAZEEVENTMNG/userhome.html')
def ecreate(request):
    return render(request,'KAMIKAZEEVENTMNG/EventCreator.html')
def eregister(request):
    return render(request,'KAMIKAZEEVENTMNG/EventRegister.html')
def eregister(request):
    return render(request,'KAMIKAZEEVENTMNG/EventRegister1.html')