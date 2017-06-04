from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
#from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from .forms import SignUpForm 

def home(request):
	user = Profile.objects.all()
	return render(request,'core/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('core/home.html')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})