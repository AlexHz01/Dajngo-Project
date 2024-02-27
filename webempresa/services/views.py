from django.shortcuts import render, HttpResponse
from .models import Service

def services(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})