from django.shortcuts import render
from .models import Portafolio
# Create your views here.
def portafolio(request):
    projects = Portafolio.objects.all()
    return render(request, 'portafolio/portafolio.html', {'projects':projects})
