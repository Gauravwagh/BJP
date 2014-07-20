from django.conf.urls import patterns





urlpatterns = patterns('facebook.views',
                            (r'^$', 'fb_app_login'),   
                                                        
                       )
