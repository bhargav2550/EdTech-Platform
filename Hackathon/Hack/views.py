from django.shortcuts import render,redirect
from Hack.forms import HackathonRegistrationForm,UserForm
from Hack.models import Hacka,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
#@login_required
def createhackathon(request):
    form =HackathonRegistrationForm()
    if request.method=="POST":
        form=HackathonRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect("/")
    return render(request,"Hack/createHack.html",{"form":form})

def user_login(request):
    form = UserForm()
    if request.method == "POST":
        user = request.POST["Username"]
        password = request.POST["Password"]
        check = User.objects.filter(Username = user).exists()
        check2 = User.objects.filter(Password = password).exists()
        if not check or not check2:
            #raise ValidationError("Please Sign Up First!")
            return redirect(regist)
        else:
            return redirect(gethackathons)
    return render(request,"Hack/base3.html",{"form":form})

#@login_required
def gethackathons(request):
    hackathons = Hacka.objects.all()
    return render(request,"Hack/index.html",{"hackathons":hackathons})
#registration to the page
def regist(request):
    form = UserForm()
    if request.method =="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(gethackathons)
    return render(request,"Hack/base2.html",{"form":form})
def index(request):
    return render(request,"Hack/base.html")
def logout(request):
    return render(request,"Hack/logout.html")
