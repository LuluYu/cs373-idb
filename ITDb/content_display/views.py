# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
#from django.views.generic.base import TemplateView #with helloTemplate Class
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.template import Context,loader
from content_display.models import Cities, Languages, Activities, languages_spoken_in

def hello_template (request):
    name = "Jesus"
    t = get_template('hello_class.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)

def index (request):
    cities = []
    activities = []
    languages = []
    error = False
    etype = ""

    # get city by city_id type
    try:
        # list all cities
        temp = Cities.objects.all()
        activities = Activities.objects.all()
        languages = Languages.objects.all()

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
		'cities':cities,
		'activities':activities,
		'languages':languages
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
    try:
        if(city_id!=None):
            if city_id.isdigit():
                #city id  is an int,
                tempc = Cities.objects.get(id=city_id)
                city.append(tempc)
            else:
                #city id is a string, thus a name
                city.append(Cities.objects.get(name=city_id))
        else:
            #list all cities
            city = Cities.objects.all()
    except ObjectDoesNotExist:
        pass

    json_city = "["
    if(len(city) != 0):
        for c in city:
            json_city += '{"id": '+str(c.id)+', "name": "'+c.name+'", "description": "'+c.description+'"},'
        json_city = json_city[0:-1] +"]"
    else:
        json_city = '{"Error 400": " No such city exist in the in the database."}'

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

    try:
        if(lang_id!=None):
            if (lang_id.isdigit()):
                language.append(Languages.objects.get(id=lang_id))
            else:
                language.append(Languages.objects.get(name=lang_id))
        else:
            language = Languages.objects.all()
    except ObjectDoesNotExist:
        pass

    json_lang = "["
    if(len(language) != 0):
        for l in language:
            json_lang  += '{"id": '+str(l.id)+', "name": "'+l.name+'", "description": "'+l.description+'"},'
        json_lang = json_lang[0:-1]+"]"
    else:
        json_lang = '{"Error 400": "No such language exists in the database."}'

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

    try:
        if(acts_id!=None):
            if(acts_id.isdigit()):
                act.append(Activities.objects.get(id=acts_id))
            else:
                act.append(Activities.objects.filter(name=acts_id))
        else:
            act = Activities.objects.all()
    except ObjectDoesNotExist:
        pass

    json_act = "["
    if(len(act) != 0):
        for a in act:
            json_act  += '{"id": '+str(a.id)+', "name": "'+a.name+'", "description": "'+a.description+'"},'
        json_act = json_act[0:-1]+"]"
    else:
        json_act = '{"Error 400": "No such activity exists in the database."}'


    template = loader.get_template('api.html')
    context = Context({
        'json_list':json_act,
    })
    return HttpResponse(template.render(context))




def view_city(request, city_id=None) :
    city = None
    cities = []
    languages = []
    activities = []
    haserror = False
    act=[]
    pictures = {}


    lang_spoken =[]
    videos= {}



    try:
        if(city_id.isdigit()) :
            city = Cities.objects.get(id=city_id)
            coords = city.coords.split(",")
        else :
            city = Cities.objects.get(name=city_id)

        act = Activities.objects.filter(city = city.id)

        lang_spoken = languages_spoken_in.objects.filter(cities = city.id)

    except Exception:
        haserror = True


    videos[city.name] = city.videos.split(",")[0]

    for a in act :
        pictures[a.name] = a.pictures.split(",")[0]

    cities = Cities.objects.all()
    languages = Languages.objects.all()
    activities = Activities.objects.all()
    template = loader.get_template('city_template.html')
    context = Context({
        'city':city,
        'cx':coords[0],
        'cy':coords[1],
        'error':haserror,
        'languages':languages,
        'activities':activities,
        'cities':cities,
        'act': act,
        'pictures': pictures,
        'lang_spoken': lang_spoken,
        'videos':videos
    })

    return HttpResponse(template.render(context))

def view_lang(request, lang_id=None):
    lang = None
    haserror = False
    error_type = ""
    cities = []
    languages = []
    activities = []
    cities_in = []

    try:
        if(lang_id.isdigit()):
            lang = Languages.objects.get(id=lang_id)
        else:
            lang = Languages.objects.get(name=lang_id)

        cities_in = languages_spoken_in.objects.filter(languages = lang.id)
    except Exception as e:
        error_type = e.__class__.__name__
        haserror = True

    cities = Cities.objects.all()
    languages = Languages.objects.all()
    activities = Activities.objects.all()
    template = loader.get_template('lang_template.html')
    context = Context({
        'lang' : lang,
        'error': haserror,
        'etype':error_type,
        'cities':cities,
        'activities':activities,
        'languages':languages,
        'cities_in':cities_in
    })
    return HttpResponse(template.render(context))

def view_activities(request, acts_id=None):
    acts = None
    haserror = False
    error_type = ""
    cities = []
    languages = []
    activities = []

    try:
        if(acts_id.isdigit()):
            acts = Activities.objects.get(id=acts_id)
        else:
            typename = acts_id
            acts = Activities.objects.get(name=typename)
    except Exception as e:
        haserror = True
        error_type = e.__class__.__name__

    cities = Cities.objects.all()
    languages = Languages.objects.all()
    activities = Activities.objects.all()
    template = loader.get_template('act_template.html')
    context = Context({
        'acts':acts,
        'pictures':acts.pictures.split(","),
        'error':haserror,
        'etype': error_type,
        'cities':cities,
        'languages':languages,
        'activities':activities
    })
    return HttpResponse(template.render(context))

def all_cities(request):
    cities = []
    pictures = {}
    haserror = False
    error_type = ""
    languages =[]
    activities = []

    try:
        cities = Cities.objects.all()

        for c in cities:
            pictures[c.name] = c.pictures.split(",")

    except Exception as e:
        haserror = True
        error_type = e.__class__.__name__

    languages = Languages.objects.all()
    activities = Activities.objects.all()
    template = loader.get_template('city_all.html')
    context = Context({
        'cities':cities,
        'pictures':pictures,
        'error':haserror,
        'etype':error_type,
        'languages':languages,
        'activities':activities
    })
    return HttpResponse(template.render(context))


def all_activities(request):
    activities = []
    pictures = {}
    haserror = False
    error_type = ""
    cities = []
    languages = []

    try:
        activities = Activities.objects.all()
        cities = Cities.objects.all()
        languages = Languages.objects.all()

        for a in activities:
            pictures[a.name] = a.pictures.split(",")

    except Exception as e:
        haserror = True
        error_type = e.__class__.__name__


    cities = Cities.objects.all()
    languages = Languages.objects.all()
    template = loader.get_template('act_all.html')
    context = Context({
        'activities':activities,
        'pictures':pictures,
        'error':haserror,
        'etype':error_type,
        'languages': languages,
        'cities': cities
    })
    return HttpResponse(template.render(context))


def all_langs(request):
    languages = []
    haserror = False
    error_type = ""
    cities= []
    activities = []

    try:
        languages = Languages.objects.all()
        cities = Cities.objects.all()
        activities = Activities.objects.all()
    except Exception as e:
        haserror = True
        error_type = e.__class__.__name__


    template = loader.get_template('lang_all.html')
    context = Context({
        'languages':languages,
        'error':haserror,
        'etype':error_type,
        'cities':cities,
        'activities':activities
    })
    return HttpResponse(template.render(context))


#------------
# Search
#------------

def search(request, query=""):
    #send to view
    template = loader.get_template('search.html')

    sql = "SELECT DISTINCT * FROM content_display_cities WHERE name LIKE '%"+query+"%' OR description LIKE '%"+query+"%'"
    c = Cities.objects.raw(sql)
    sql = "SELECT DISTINCT * FROM content_display_activities WHERE name LIKE '%"+query+"%' OR description LIKE '%"+query+"%' OR type_activity LIKE '%"+query+"%'"
    a = Activities.objects.raw(sql)
    sql = "SELECT DISTINCT * FROM content_display_languages WHERE name LIKE '%"+query+"%' OR description LIKE '%"+query+"%'"
    l = Languages.objects.raw(sql)

    if(query==""):
        context = Context({
            'blank':True,
        })
    else:
        context = Context({
            'blank':False,
            'query':query,
            'cities':c,
            'ccount':len(list(c)),
            'cbool':len(list(c))>0,
            'activities':a,
            'acount':len(list(a)),
            'abool':len(list(a))>0,
            'languages':l,
            'lcount':len(list(l)),
            'lbool':len(list(l))>0,
        })

    return HttpResponse(template.render(context))