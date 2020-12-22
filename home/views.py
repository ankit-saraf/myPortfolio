from django.shortcuts import render
from .models import *

def index(request):
    introduction = Introduction.objects.all()
    skills = TechnicalSkills.objects.order_by('rank')
    laf = Laf.objects.order_by('rank')
    timeline = Timeline.objects.order_by('rank')
    projects = Project.objects.order_by('rank')
    context = {'introduction':introduction, 'skills':skills, 'laf':laf, 'timeline':timeline,'projects':projects}
    
    return render(request, './home/home.html', context)
