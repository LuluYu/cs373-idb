# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
#from django.views.generic.base import TemplateView #with helloTemplate Class


def hello_template (request):
    name = "Jesus"
    t = get_template('hello_class.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)

def index (request):
    return render_to_response('index.html')


# cities 

def lijiang_China (request):
    return render_to_response('lijiang_China.html')

def capeTown_SouthAfrica (request):
    return render_to_response('capeTown_SouthAfrica.html')

def chichen_Itza_Mexico (request):
    return render_to_response('chichen_Itza_Mexico.html')

# activities 

def sceneries (request):
    return render_to_response('sceneries.html')

def historical (request):
    return render_to_response('historical.html')

def housing (request):
    return render_to_response('housing.html')

# languages 

def chinese (request):
    return render_to_response('chinese.html')

def english (request):
    return render_to_response('english.html')

def spanish (request):
    return render_to_response('spanish.html')