from django.shortcuts import render
from contact.forms import Registesion
from django.http import HttpResponseRedirect
from . models import Singup


# Create your views here.
def contact(request):
    return render(request, 'contact/contact.html')


def forms(request):
    if request.method == 'POST':
        info = Registesion(request.POST)
        if info.is_valid():
            f_name = info.cleaned_data['frist_name']
            l_name = info.cleaned_data['last_name']
            email = info.cleaned_data['email']
            passw = info.cleaned_data['password']
            c_passw = info.cleaned_data['comfrom_password']
            count = info.cleaned_data['which_one_flowers']
            comment = info.cleaned_data['comment']
            check_box = info.cleaned_data['Agree_to_terms_and_conditions']
            check_shop = info.cleaned_data['Do_you_want_to_buy_flowers_in_my_shop']
            
            show_data = Singup(frist_name=f_name, last_name=l_name, email= email, password= passw, comfrom_password= c_passw, which_one_flowers= count, comment= comment, Agree_to_terms_and_conditions= check_box, Do_you_want_to_buy_flowers_in_my_shop= check_shop)
            
            show_data.save()
            
            return HttpResponseRedirect('/contact/submited')
        
    else:
        info = Registesion(auto_id=True)
        
    return render(request, 'contact/forms.html', {'form': info})


def submit(request):
    return render(request, 'contact/welcome.html')
