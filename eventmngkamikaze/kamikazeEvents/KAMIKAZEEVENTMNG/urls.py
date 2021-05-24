from django.urls import path
from . import views
urlpatterns = [
    path('', views.hi),
    path ('userlogin.html',views.login, name="ulogin"),
path ('usersignup.html',views.signup, name="usignup"),
    path('userhome.html',views.home, name="uhome"),
    path('EventCreator.html',views.ecreate, name="eventcreate"),
    path('EventRegister.html',views.eregister, name="eventregister"),
path('EventRegister1.html',views.eregister, name="eventregister1"),


]
