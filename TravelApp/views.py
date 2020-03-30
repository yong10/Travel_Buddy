from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt


def index(request):
    return render(request, "main.html")

def addUser(request):
    user = User.objects.all()
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/main")
    else:
        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        User.objects.create(name=request.POST['name'], user_name=request.POST['user_name'], password=hash1)
        user = User.objects.get(user_name = request.POST['user_name'])
        request.session['user'] = user.id
        return redirect("/travel")

def logUser(request):
    user = User.objects.filter(user_name=request.POST['user_name'])
    errors = {}
    if not user:
        errors['user_name'] = "Invalid username or password"
    else:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user'] = logged_user.id
            return redirect("/travel")
        else:
            errors['password'] = "Invalid username or password"

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/main")
    else:
        request.session['user'] = logged_user.id
        return redirect("/travel")

def travel(request):
    if 'user' not in request.session:
        return redirect("/main")
    context ={
        'travels': Travel.objects.filter(join=request.session['user']),
        'loggedin': User.objects.get(id=request.session['user']),
        'allTravel': Travel.objects.all() 
    }
    return render(request, "travels.html", context)

def createTrip(request):
    return render(request, "createTrip.html")

def addTrip(request):
    if 'user' not in request.session:
        return redirect("/main")
    errors = Travel.objects.travel_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/travel/create")
    else:
        u = User.objects.get(id=request.session['user'])
        Travel.objects.create(destination=request.POST['destination'], start=request.POST['start'], end=request.POST['end'], desc=request.POST['desc'], creator=u)
        return redirect('/travel')

def travelInfo(request, id):
    context = {
        'travelinfo': Travel.objects.get(id = id),
        'others': User.objects.filter(join=id).exclude(id=Travel.objects.get(id=id).creator_id)
    }
    return render(request, "travelinfo.html", context)

def join(request, id):
    if 'user' not in request.session:
        return redirect("/main")
    #How can I make people to join#
    #t =Travel.objects.get(id = id)
    #t.join.add(User.objects.get(id=request.session['user']))
    t =Travel.objects.get(id = id)
    u = User.objects.get(id=request.session['user'])
    u.join.add(t)
    return redirect('/travel')

def logout(request):
    request.session.clear()
    return redirect('/main')