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
    url(r'^Lijiang_China/$', 'content_display.views.lijiang_China'),
    url(r'^Chinese/$', 'content_display.views.chinese'),
    url(r'^English/$', 'content_display.views.english'),
    url(r'^sceneries/$', 'content_display.views.sceneries'),
    url(r'^Cape_Town_South_Africa/$', 'content_display.views.capeTown_SouthAfrica'),
    url(r'^historical/$', 'content_display.views.historical'),
    url(r'^Chichen_Itza_Mexico/$', 'content_display.views.chichen_Itza_Mexico'),


)
