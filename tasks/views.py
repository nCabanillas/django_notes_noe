from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Task 

# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})
    else:
        
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objests.create_user(request.POST["username"],password=request.POST["password1"])
            except IntegrityError:
                return render(request, 'signup.html', {"form":UserCreationForm, "error":"Username already taken."})
    
    return render(request, 'signup.html', {"form": UserCreationForm, "error":"Passwords did not match."})

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html')