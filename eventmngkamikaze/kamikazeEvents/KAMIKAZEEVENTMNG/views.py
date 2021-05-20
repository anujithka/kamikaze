from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hi(request):
    return render(request,'KAMIKAZEEVENTMNG/First.html')
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