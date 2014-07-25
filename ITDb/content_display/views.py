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
    cities = []
    error = False
    etype = ""

    # get city by city_id type
    try:
        # list all cities
        temp = Cities.objects.all()

        for c in temp:
            coords = c.coords.split(",")
            k = {"name":c.name,"id":c.id,"x":coords[0],"y":coords[1]}
            cities.append(k)
    except Exception as e:
        error = True
        etype = e.__class__.__name__


	# send to view
    template = loader.get_template('index.html')
    context = Context({
		'cities':cities
	})
    return HttpResponse(template.render(context))


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

    #get city by city_id type

    if(city_id!=None):
        if city_id.isdigit():
            #city id  is an int,
            city.append(Cities.objects.get(id=city_id))
        else:
            #city id is a string, thus a name
            city.append(Cities.objects.get(name=city_id))
    else:
        #list all cities
        city = Cities.objects.all()



    json_city = "["
    if(len(city) != 0):
        for c in city:
            json_city += '{"id": '+str(c.id)+', "name": "'+c.name+'", "description": "'+c.description+'"},'
        json_city = json_city[0:-1] +"]"
    else:
        json_city = '{Error 400: " No such city exist in the in the database."}'

    #send to view
    template = loader.get_template('api.html')
    context = Context({
        'json_list':json_city,
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



    json_lang = "["
    if(len(language) != 0):
        for l in language:
            json_lang  += '{"id": '+str(l.id)+', "name": "'+l.name+'", "description": "'+l.description+'"},'
        json_lang = json_lang[0:-1]+"]"
    else:
        json_lang = '{Error 400: "No such language exists in the database."}'

    template = loader.get_template('api.html')
    context = Context({
        'json_list':json_lang,
    })
    return HttpResponse(template.render(context))

# --------------
#	activities
# --------------
def api_activities(request,acts_id=None):
    act = []


    if(acts_id!=None):
        if(acts_id.isdigit()):
            act.append(Activities.objects.get(id=acts_id))
        else:
            act.append(Activities.objects.filter(name=acts_id))
    else:
        act = Activities.objects.all()


    json_act = "["
    if(len(act)):
        for a in act:
            json_act  += '{"id": '+str(a.id)+', "name": "'+a.name+'", "description": "'+a.description+'"},'
        json_act = json_act[0:-1]+"]"
    else:
        json_act = '{Error 400: "No such activity exists in the database."}'


    template = loader.get_template('api.html')
    context = Context({
        'json_list':json_act,
    })
    return HttpResponse(template.render(context))

def view_city(request, city_id=None) :
    city = None
    haserror = False

    try:
        if(city_id.isdigit()) :
            city = Cities.objects.get(id=city_id)
            coords = city.coords.split(",")
        else :
            city = Cities.objects.get(name=city_id)
    except Exception:
        haserror = True

    template = loader.get_template('city_template.html')
    context = Context({
        'city':city,
        'cx':coords[0],
        'cy':coords[1],
        'error':haserror
    })

    return HttpResponse(template.render(context))

def view_lang(request, lang_id=None):
    lang = None
    haserror = False
    error_type = ""

    try:
        if(lang_id.isdigit()):
            lang = Languages.objects.get(id=lang_id)
        else:
            lang = Languages.objects.get(name=lang_name)
    except Exception as e:
        error_type = e.__class__.__name__
        haserror = True

    template = loader.get_template('lang_template.html')
    context = Context({
        'lang' : lang,
        'error': haserror,
        'etype':error_type,
    })
    return HttpResponse(template.render(context))

def view_activities(request, acts_id=None):
    acts = None
    haserror = False
    error_type = ""

    try:
        if(acts_id.isdigit()):
            acts = Activities.objects.get(id=acts_id)
        else:
            typename = acts_id
            acts = Activities.objects.get(name=typename)
    except Exception as e:
        haserror = True
        error_type = e.__class__.__name__

    template = loader.get_template('act_template.html')
    context = Context({
        'acts':acts,
        'pictures':acts.pictures.split(","),
        'error':haserror,
        'etype': error_type,
    })
    return HttpResponse(template.render(context))

def all_cities(request):
    cities = []
    pictures = {}
    haserror = False
    error_type = ""

    try:
        cities = Cities.objects.all()

        for c in cities:
            pictures[c.name] = c.pictures.split(",")

    except Exception as e:
        haserror = True
        error_type = e.__class__.__name__

    template = loader.get_template('city_all.html')
    context = Context({
        'cities':cities,
        'pictures':pictures,
        'error':haserror,
        'etype':error_type,
    })
    return HttpResponse(template.render(context))


def all_activities(request):
    acts = []
    pictures = {}
    haserror = False
    error_type = ""

    try:
        acts = Activities.objects.all()

        for a in acts:
            pictures[a.name] = a.pictures.split(",")

    except Exception as e:
        haserror = True
        error_type = e.__class__.__name__

    template = loader.get_template('act_all.html')
    context = Context({
        'acts':acts,
        'pictures':pictures,
        'error':haserror,
        'etype':error_type,
    })
    return HttpResponse(template.render(context))


def all_langs(request):
    langs = []
    haserror = False
    error_type = ""

    try:
        langs = Languages.objects.all()
    except Exception as e:
        haserror = True
        error_type = e.__class__.__name__

    template = loader.get_template('lang_all.html')
    context = Context({
        'langs':langs,
        'error':haserror,
        'etype':error_type,
    })
    return HttpResponse(template.render(context))