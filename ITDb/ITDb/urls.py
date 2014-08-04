from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ITDb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello_template/$', 'content_display.views.hello_template'),
    url(r'^index/$', 'content_display.views.index'),
    url(r'^$', 'content_display.views.index'),

    # cities
    url(r'^Lijiang_China/$', 'content_display.views.lijiang_China'),
    url(r'^Chichen_Itza_Mexico/$', 'content_display.views.chichen_Itza_Mexico'),
    url(r'^Cape_Town_South_Africa/$', 'content_display.views.capeTown_SouthAfrica'),

    #Template for cities
    url(r'^cities/$', 'content_display.views.all_cities'),
    url(r'^cities/(?P<city_id>[a-zA-Z0-9-\s]+)/$', 'content_display.views.view_city'),

    # activities
    url(r'^sceneries/$', 'content_display.views.sceneries'),
    url(r'^historical/$', 'content_display.views.historical'),
    url(r'^housing/$', 'content_display.views.housing'),

    #Template for activities
    url(r'^activities/$', 'content_display.views.all_activities'),
    url(r'^activities/(?P<acts_id>[a-zA-Z0-9-\s]+)/$', 'content_display.views.view_activities'),

    # languages
    url(r'^Chinese/$', 'content_display.views.chinese'),
    url(r'^English/$', 'content_display.views.english'),
    url(r'^Spanish/$', 'content_display.views.spanish'),

    #Template for language
    url(r'^languages/$', 'content_display.views.all_langs'),
    url(r'^languages/(?P<lang_id>[a-zA-Z0-9-\s]+)/$', 'content_display.views.view_lang'),

    # api
    # list of all objects
    url(r'^api/cities/$', 'content_display.views.api_cities', name="api"),
    url(r'^api/languages/$', 'content_display.views.api_languages', name="api"),
    url(r'^api/activities/$', 'content_display.views.api_activities', name="api"),

    # particular objects
    url(r'^api/cities/(?P<city_id>[a-zA-Z0-9-\s]+)/$', 'content_display.views.api_cities', name="api"),
    url(r'^api/languages/(?P<lang_id>[a-zA-Z0-9-\s]+)/$', 'content_display.views.api_languages', name="api"),
    url(r'^api/activities/(?P<acts_id>[a-zA-Z0-9-\s]+)/$', 'content_display.views.api_activities', name="api"),

    # search
    url(r'^search/$','content_display.views.search'),
    url(r'^search/(?P<query>[a-zA-Z0-9-\s]+)/$','content_display.views.search'),

    #Git-A-Grep API
    url(r'^ut_api/$', 'content_display.views.ut_api'),


)
