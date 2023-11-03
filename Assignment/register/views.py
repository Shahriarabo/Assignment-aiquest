from django.shortcuts import render, HttpResponseRedirect
from . forms import Userform
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.
def register(request):
    if request.method == "POST":
        info = Userform(request.POST)
        if info.is_valid():
            info.save()
    else:
        info = Userform()
        
    return render(request, 'register/register.html', {'user': info})



# login Forms
def loginform(request):
    if request.method == 'POST':
        info = AuthenticationForm(request= request, data= request.POST)
        if info.is_valid():
            username= info.cleaned_data['username']
            userpassword= info.cleaned_data['password']
            user = authenticate(username = username, password = userpassword) 
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/register/submited')
            
    else:        
        info = AuthenticationForm()
    return render(request , 'register/login.html', {'user': info})

# successfully login 
def submit(request):
    return render(request, 'register/welcome.html')





# logout forms

def logoutforms(request):
    logout(request)
    return HttpResponseRedirect('/register/login')




# change password form 
def change_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            info = PasswordChangeForm(user = request.user, data=request.POST) 
            if info.is_valid():
                info.save()
                update_session_auth_hash(request, info.user)
                return HttpResponseRedirect('/register/change')
        else:
            info = PasswordChangeForm(user = request.user)
            return render(request, 'register/password.html',{'user':info})      
    
    else:
        return HttpResponseRedirect('/register/login')            
   


# successfully old password change 
def change(request):
    return render(request, 'register/change.html')



# successfully password change without old password
def withoutold(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            info = SetPasswordForm(user = request.user, data=request.POST) 
            if info.is_valid():
                info.save()
                update_session_auth_hash(request, info.user)
                return HttpResponseRedirect('/register/change')
        else:
            info = SetPasswordForm(user = request.user)
            return render(request, 'register/withoutoldpass.html',{'user':info})      
    
    else:
        return HttpResponseRedirect('/register/login')            
   



    