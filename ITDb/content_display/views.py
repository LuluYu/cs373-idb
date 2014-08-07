# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import Context, RequestContext
#from django.views.generic.base import TemplateView #with helloTemplate Class
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.template import Context,loader
from content_display.models import Cities, Languages, Activities, languages_spoken_in
from django.shortcuts import render
#import urllib2
import urllib
import json

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
            json_act  += '{"id": '+str(a.id)+', "name": "'+a.name+'", "description": "'+a.description+'", "city": '+str(a.city.id)+'},'
        json_act = json_act[0:-1]+"]"
    else:
        json_act = '{"Error 400": "No such activity exists in the database."}'


    template = loader.get_template('api.html')
    context = Context({
        'json_list':json_act,
    })
    return HttpResponse(template.render(context))


# ---------
#   about
# ---------
def about (request):
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


    template = loader.get_template('about.html')
    context = Context({
        'languages':languages,
        'error':haserror,
        'etype':error_type,
        'cities':cities,
        'activities':activities
    })
    return HttpResponse(template.render(context))


def view_city(request, city_id=None) :
    city = None
    cities = []
    languages = []
    activities = []
    haserror = False
    act=[]
    cover = ""
    pictures = {}
    lang_spoken =[]
    videos= {}

    if(city_id.isdigit()) :
        city = get_object_or_404(Cities, id= city_id)
        #city = Cities.objects.get(id=city_id)
    else :
        city = get_object_or_404(Cities, name=city_id)
        #city = Cities.objects.get(name=city_id)

    act = Activities.objects.filter(city = city.id)
    coords = city.coords.split(",")
    lang_spoken = languages_spoken_in.objects.filter(cities = city.id)
    cover = city.pictures.split(",")[0]
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
        'videos':videos,
        'cover':cover,
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

    if(lang_id.isdigit()):
        #lang = Languages.objects.get(id=lang_id)
        lang = get_object_or_404(Languages, id=lang_id)
    else:
        lang = get_object_or_404(Languages, name=lang_id)
        #lang = Languages.objects.get(name=lang_id)

    cities_in = languages_spoken_in.objects.filter(languages = lang.id)

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
    city_acts = []

    if(acts_id.isdigit()):
        acts = get_object_or_404(Activities, id=acts_id)
        #acts = Activities.objects.get(id=acts_id)
    else:
        typename = acts_id
        acts = get_object_or_404(Activities, name = typename)
        #acts = Activities.objects.get(name=typename)

    cities = Cities.objects.all()
    languages = Languages.objects.all()
    activities = Activities.objects.all()
    city_acts = Activities.objects.filter(city_id = acts.city_id)
    template = loader.get_template('act_template.html')
    context = Context({
        'acts':acts,
        'pictures':acts.pictures.split(","),
        'error':haserror,
        'etype': error_type,
        'cities':cities,
        'languages':languages,
        'activities':activities,
        'city_acts' :city_acts
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
            pictures[c.name] = c.pictures.split(",")[0]

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
            pictures[a.name] = a.pictures.split(",")[0]

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
        'activities':activities,
    })
    return HttpResponse(template.render(context))


#------------
# Search
#------------

def search(request, query=""):
    navlanguages = []
    navcities= []
    navactivities = []
    haserror = False
    error_type = ""

    query1 = query.upper()
    try:
        navlanguages = Languages.objects.all()
        navcities = Cities.objects.all()
        navactivities = Activities.objects.all()
    except Exception as e:
        haserror = True
        error_type = e.__class__.__name__

    #send to view
    template = loader.get_template('search.html')

    sql = "SELECT DISTINCT * FROM content_display_cities WHERE name collate utf8_general_ci LIKE '%"+query1+"%' OR description LIKE '%"+query1+"%' OR country LIKE '%"+query1+"%'"
    c = Cities.objects.raw(sql)
    sql2 = "SELECT DISTINCT * FROM content_display_activities WHERE name collate utf8_general_ci LIKE '%"+query1+"%' OR description LIKE '%"+query1+"%' OR type_activity LIKE '%"+query1+"%'"
    a = Activities.objects.raw(sql2)
    sql3 = "SELECT DISTINCT * FROM content_display_languages WHERE name collate utf8_general_ci LIKE '%"+query1+"%' OR description LIKE '%"+query1+"%'"
    l = Languages.objects.raw(sql3)

    # ---------
    #   OR
    # ---------
    s = query1.split()
    sql4 = "SELECT DISTINCT * FROM content_display_cities WHERE name collate utf8_general_ci LIKE '%" + ("%' OR name LIKE '%".join(s)) + "%' OR description LIKE '%" + ("%' OR description LIKE '%".join(s)) +"%' OR country LIKE '%" + ("%' OR country LIKE '%".join(s))+"%'"
    co = Cities.objects.raw(sql4)
    sql5 = "SELECT DISTINCT * FROM content_display_activities WHERE name collate utf8_general_ci LIKE '%" + ("%' OR name LIKE '%".join(s)) +"%' OR description LIKE '%" + ("%' OR description LIKE '%".join(s)) +"%' OR type_activity LIKE '%" + ("%' OR type_activity LIKE '%".join(s))+"%'"
    ao = Activities.objects.raw(sql5)
    sql6 = "SELECT DISTINCT * FROM content_display_languages WHERE name collate utf8_general_ci LIKE '%" + ("%' OR name LIKE '%".join(s)) + "%' OR description LIKE '%" + ("%' OR description LIKE '%".join(s)) +"%'"
    lo = Languages.objects.raw(sql6)

    ccount = 0
    acount = 0
    lcount = 0

    cocount = 0
    aocount = 0
    locount = 0

    try:
        ccount = len(list(c)) if (list(c) is not None) else 0
        # if(list(c) is None):
        #     ccount = 0
        # else:
        #     ccount = len(list(c))
    except AttributeError:
        ccount = 0

    try:
        if(list(a) is None):
            acount = 0
        else:
            acount = len(list(a))
    except AttributeError:
        acount = 0

    try:
        if(list(l) is None):
            lcount = 0
        else:
            lcount = len(list(l))
    except AttributeError:
        lcount = 0

    try:
        if(list(co) is None):
            cocount = 0
        else:
            cocount = len(list(co))
    except AttributeError:
        cocount = 0

    try:
        if(list(ao) is None):
            aocount = 0
        else:
            aocount = len(list(ao))
    except AttributeError:
        aocount = 0

    try:
        if(list(lo) is None):
            locount = 0
        else:
            locount = len(list(lo))
    except AttributeError:
        locount = 0

    if(query == ""):
        context = Context({
            'blank':True,
            'navcities':navcities,
            'navlanguages':navlanguages,
            'navactivities':navactivities
        })
    else:
        context = Context({
            'navcities':navcities,
            'navlanguages':navlanguages,
            'navactivities':navactivities,
            'blank':False,
            'query':query,
            'cities':c,
            'ccount':ccount,
            'cbool':ccount>0,
            'activities':a,
            'acount':acount,
            'abool':acount>0,
            'languages':l,
            'lcount':lcount,
            'lbool':lcount>0,
            'co': co,
            'cocount':cocount,
            'cobool':cocount>0,
            'ao': ao,
            'aocount':aocount,
            'aobool':aocount>0,
            'lo': lo,
            'locount':locount,
            'lobool':locount>0

        })

    return HttpResponse(template.render(context))

def ut_api(request) :

    template = loader.get_template('ut_api.html')
    #response = urllib2.urlopen('https://gitagrep.pythonanywhere.com/rest/colleges/')
    #html = response.read()
    #content = json.loads(html)
    response = urllib.request.urlopen('https://gitagrep.pythonanywhere.com/rest/colleges/')
    html = response.read().decode("utf-8")
    content = json.loads(html)
    c = Cities.objects.all()
    a = Activities.objects.all()
    l = Languages.objects.all()

    context = Context({
        'content':content,
        'cities':c,
        'activities':a,
        'languages':l
    })

    return HttpResponse(template.render(context))

def error404(request) :
    return render_to_response('404.html', context_instance=RequestContext(request))

