from django.conf.urls import patterns, include, url

urlpatterns = patterns('',  
                       url(r'^$',     'contact.views.hello'),
                       url(r'^list$', 'contact.views.json_list'),
                       url(r'^post$', 'contact.views.json_post'),
)
