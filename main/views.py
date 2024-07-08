from django.shortcuts import render
from django.conf import settings

def index(request): 
    context = {"name":settings.DATA["NAME"],
               "about_me":settings.DATA["ABOUT"]}
    return render(request, 'main/index.html', context)
def project(request):
    context={"projects":settings.DATA["PROJECTS"]}
    return render(request, 'main/project.html',context)

def language(request):
    context={"languages":settings.DATA["LANGUAGE"]}
    return render(request, 'main/language.html',context)