from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views import View

from .models import Project, Achievement
from .forms import ContactForm
# Create your views here.

def index(request):
    projects = Project.objects.all()
    allprojects = {}
    for project in projects:
        project_tags = project.tags.all()
        allprojects[project] = project_tags
    
    achievements = Achievement.objects.all()
    allachievements = {}
    for achievement in achievements:
        achievement_tags = achievement.tags.all()
        allachievements[achievement] = achievement_tags
        
    return render(request, 'index.html', { 
        'projects': allprojects,
        'achievements': allachievements
    })

class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html', {
            'form': form
        }) 

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print('Form Submitted')
            print(form)
            form.save()
            return HttpResponseRedirect('')
        return render(request, 'contact.html', {
            'form': form
        })  