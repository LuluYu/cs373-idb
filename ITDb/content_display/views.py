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
	all_cities = False

	# get city by city_id type
	if(city_id!=None):
		if city_id.isdigit():
			# city_id is an int, thus an id
			city = Cities.objects.get(id=city_id)
		else:
			# city_id is a string, thus a name
			city = Cities.objects.get(name=city_id)
	else:
		# city_id is empty, so they want all cities
		all_cities = True
		city = Cities.objects.all()

	# generate json string
	if all_cities:
	    json_city = '['
	    for c in city:
	        json_city += jsonify_city(c)+','
	    json_city = json_city[0:-1]+']'
	else:
		json_city = jsonify_city(city)

	# send to view
	template = loader.get_template('api.html')
	context = Context({
		'json_str':json_city,
	})
	return HttpResponse(template.render(context))

def jsonify_city(city):
    return '{"id":'+str(city.id)+',"name":"'+city.name+'","description":"'+city.description+'"}'

# --------------
#	languages
# --------------
def api_languages(request,lang_id=None):
    all_languages = False

    # get language by language_id type
    if (language_id!=None):
        if lang_id.isdigit():
            # lang_id is an int, thus an id
            language = Languages.objects.get(id=lang_id)
        else:
            # lang_id is a string, thus a name
            language = Languages.objects.get(name=lang_id)
    else:
        # lang_id is empty, so they want all languages
        all_languages = True
        language = Languages.objects.all()

    # generate json string
    if all_languages:
        json_language = '['
        for l in language:
            json_language += jsonify_language(l)+','
        json_language = json_language[0:-1]+']'
    else:
        json_language = jsonify_language(language)

    # send to view
	template = loader.get_template('api.html')
	context = Context({
		'json_str':json_language,
	})
	return HttpResponse(template.render(context))

def jsonify_language(language):
    return '{"id":'+str(language.id)+',"name":'+language.name+'","description":'+language.description+'"}'

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
