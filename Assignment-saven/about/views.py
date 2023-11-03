from django.shortcuts import render

# Create your views here.
def about(request):
    infrometion = {'info': ['Abdulla', 'Jhenaida', 'student', 'Magura']}
    return render(request, 'about/about.html', infrometion)