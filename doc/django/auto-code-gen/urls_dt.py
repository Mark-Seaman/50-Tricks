from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',

    # Data_Type
    url(r'^data_type/list$',                  'event.view_data_type.data_type_list'),
    url(r'^data_type/show/(?P<id>[\d]+)$',    'event.view_data_type.data_type_show'),
    url(r'^data_type/add$',                   'event.view_data_type.data_type_add'),
    url(r'^data_type/edit/(?P<id>[\d]+)$',    'event.view_data_type.data_type_edit'),
    url(r'^data_type/delete/(?P<id>[\d]+)$',  'event.view_data_type.data_type_delete'),
    url(r'^data_type/test$',                  'event.view_data_type.data_type_test'),

    # Catch all view
    url(r'^(?P<title>[\w\-_./]+)$',   'event.views.missing_view'),

)
