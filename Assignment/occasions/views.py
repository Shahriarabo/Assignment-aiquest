from django.shortcuts import render

# Create your views here.
def occasions(request):
    return render(request, 'occasions/birthday.html')


def any(request):
    return render(request, 'occasions/any.html')


def thank(request):
    return render(request, 'occasions/thank.html')

