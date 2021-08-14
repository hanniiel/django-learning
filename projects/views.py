from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def projects(request):
    msg = 'holis from bcknd'
    number = 11
    context = {'message':msg,'number':number}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    return render(request,'projects/single-project.html')