from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',

    # EventMenu
    url(r'^eventmenu/list$',                  'event.view_eventmenu.eventmenu_list'),
    url(r'^eventmenu/show/(?P<id>[\d]+)$',    'event.view_eventmenu.eventmenu_show'),
    url(r'^eventmenu/add$',                   'event.view_eventmenu.eventmenu_add'),
    url(r'^eventmenu/edit/(?P<id>[\d]+)$',    'event.view_eventmenu.eventmenu_edit'),
    url(r'^eventmenu/delete/(?P<id>[\d]+)$',  'event.view_eventmenu.eventmenu_delete'),
    url(r'^eventmenu/test$',                  'event.view_eventmenu.eventmenu_test'),

    # Catch all view
    url(r'^(?P<title>[\w\-_./]+)$',   'event.views.missing_view'),

)
