from django.shortcuts import render
from .models import customer_info


# Create your views here.
def service(requrat):
    svc = customer_info.objects.all()
    return render(requrat, 'service/service.html', {'sd': svc})




