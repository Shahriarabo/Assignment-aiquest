from django.shortcuts import render

# Create your views here.
def home(request):
    my = 'MD.Abdulla Al Shahriar'
    study = 'Ai-quest'
    batch = 4
    home = 'Kotchandpur'
    info = {'name': my, 'student': study, 'batch': batch, 'town': home}
    return render(request, 'home/home.html', info)