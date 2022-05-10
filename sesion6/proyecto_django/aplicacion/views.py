from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def index(request):
    return HttpResponse("Hello, world")
	
def paginaweb(request):
    return HttpResponse("Hello, world")
    
def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>La hora actual es %s.</body></html>" % now
	return HttpResponse(html)
	
def vista(request):
	now = datetime.datetime.now()
	html = "<html><body>La hora actual es %s.</body></html>" % now
	return render(request,'plantilla.html',{'nombre':'Usuario'})


