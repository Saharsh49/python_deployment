from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from college.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.

def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
       form=SignUpForm(request.POST)
       if form.is_valid():
           print("User login available")
           #form.save()

       user=form.save()
       user.set_password(user.password)
       user.save()
       return HttpResponseRedirect('/accounts/login')
    return render(request,'college/signup.html',{'form':form})


def home(request):
 return render(request,'college/home.html')

@login_required
def btech1(request):
  return render(request,'college/btech1.html')

@login_required
def btech2(request):
  return render(request,'college/btech2.html')

@login_required
def btech3(request):
  return render(request,'college/btech3.html')

def logout(request):
    return render(request,'college/logout.html')
