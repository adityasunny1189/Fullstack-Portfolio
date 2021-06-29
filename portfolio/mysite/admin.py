from django.contrib import admin
from .models import Tag, Project, Achievement, Certificate, Contact, Qualification, Experience, Skill

# Register your models here.

admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(Achievement)
admin.site.register(Certificate)
admin.site.register(Contact)
admin.site.register(Qualification)
admin.site.register(Experience)
admin.site.register(Skill)