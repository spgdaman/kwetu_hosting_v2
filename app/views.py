from django.shortcuts import render, redirect
import datetime as dt
from .models import *
from .forms import *

# Create your views here.
def home(request):
    date = dt.date.today()
    assets = Assets.objects.all()
    return render(request, 'home.html' ,{"date":date, 'assets':assets})

def profile(request):
    date = dt.date.today()
    current_user = request.user
    # profile = Profile.objects.get(user=current_user.id)
    assets = Assets.objects.all()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    return render(request, 'profile/profile.html', locals() )

def edit_profile(request):
    date = dt.date.today()
    current_user = request.user
    #profile = Profile.objects.get(user=current_user.id)
    if request.method == 'POST':
        return redirect('profile')
        signup_form = EditForm(request.POST, request.FILES,instance=request.user.profile) 
        if signup_form.is_valid():
            signup_form.save()
            
    else:
        signup_form =EditForm() 
        
    return render(request, 'profile/edit_profile.html', {"date": date, "form": signup_form, "profile":profile})    