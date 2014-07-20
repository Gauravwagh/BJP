from django.conf.urls import patterns,url,include
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from settings import OUR_APPS,SITE_ROOT


import os

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BJP.views.home', name='home'),
    # url(r'^BJP/', include('BJP.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('userview.views',url(r'^$', 'home'),)

for app in OUR_APPS:
    urlpatterns += patterns('',url(r'^'+app+'/', include(app+'.urls',app_name=app)),)
    

urlpatterns += patterns('',
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(SITE_ROOT, 'templates/media')}),)