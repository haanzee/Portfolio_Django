from multiprocessing import context
from django.shortcuts import render, HttpResponseRedirect

# Create your views here.

def Index_View(request):
    context = {'index': 'active'}
    return render(request, 'webapp/index.html',context)

def Certification_View(request):
    context = {'certifications': 'active'}
    return render(request, 'webapp/certifications.html', context)

def Skills_View(request):
    context = {'skills': 'active'}
    return render(request, 'webapp/skills.html', context)

def Projects_View(request):
    context = {'projects': 'active'}       
    return render(request, 'webapp/projects.html', context)

def ProjectDetails_View(request):
    context = {'projectdet': 'active'}
    return render(request, 'webapp/projectdetails.html', context)

def Profile_View(request):
    context = {'profile': 'active'}
    return render(request, 'webapp/profile.html', context)

def Resume_View(request):
    context = {'resume': 'active'}
    return render(request, 'webapp/resume.html', context)
