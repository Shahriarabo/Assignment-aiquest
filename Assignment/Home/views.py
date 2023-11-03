from django.shortcuts import render

# Create your views here.
def Home(requrat):
    return render(requrat, 'home/home.html')