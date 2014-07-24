# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
#from django.views.generic.base import TemplateView #with helloTemplate Class
from django.http import HttpResponse, Http404
from django.template import Context,loader
from content_display.models import Cities, Languages, Activities

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

# api

# --------------
#	cities
# --------------
def api_cities(request,city_id=None):
	city = []

	# get city by city_id type
	if(city_id!=None):
		if city_id.isdigit():
			# city_id is an int, thus an id
			city.append(Cities.objects.get(id=city_id))
		else:
			# city_id is a string, thus a name
			city.append(Cities.objects.get(name=city_id))
	else:
		# city_id is empty, so they want all cities
		city = Cities.objects.all()


	# send to view
	template = loader.get_template('api.html')
	context = Context({
		'json_list':city,
	})
	return HttpResponse(template.render(context))

# --------------
#	languages
# --------------
def api_languages(request,lang_id=None):
    language = []

    if(lang_id!=None):
        if (lang_id.isdigit()):
            language.append(Languages.objects.get(id=lang_id))
        else:
            language.append(Languages.objects.get(name=lang_id))
    else:
        language = Languages.objects.all()

    template = loader.get_template('api.html')
    context = Context({
        'json_list':language,
    })
    return HttpResponse(template.render(context))

# --------------
#	activities
# --------------
def api_activities(request,acts_id=-1):
	template = loader.get_template('api.html')
	context = Context({
		'type':'activities',
		'acts_id':acts_id,
	})
	return HttpResponse(template.render(context))
